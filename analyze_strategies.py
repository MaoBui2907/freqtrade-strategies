import ast
import glob
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

class CommentRemover(ast.NodeTransformer):
    def visit_Expr(self, node):
        if isinstance(node.value, ast.Str):
            return None
        return node

class FunctionExtractor(ast.NodeVisitor):
    def __init__(self):
        self.functions = {}

    def visit_FunctionDef(self, node):
        function_name = node.name
        function_code = ast.unparse(node)
        self.functions[function_name] = function_code
        self.generic_visit(node)

def load_strategy(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
    tree = CommentRemover().visit(tree)

    function_extractor = FunctionExtractor()
    function_extractor.visit(tree)
    functions = function_extractor.functions
    code = ast.unparse(tree)
    return code, functions


def find_lookahead_bias(functions: dict[str, str]):
    llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model="gpt-4o-mini")
    class LookaheadBias(BaseModel):
        issues: list[str]
    parser = PydanticOutputParser(pydantic_object=LookaheadBias)
    prompt = PromptTemplate(
        input_variables=['functions'],
        template='''You are a Freqtrade Bot Expert. You are given a strategy to analyze. The strategy has the following functions:\n\n{functions}\n\nAnalyze the strategy and identify if there is any lookahead bias in the strategy. If there is any lookahead bias, explain how it can be removed.\n{format_instruction}''',
        partial_variables={'format_instruction': parser.get_format_instructions()},
    )
    max_retry = 3
    while max_retry > 0:
        try:
            prompt_value = prompt.invoke(input={'functions': functions})
            response = llm.invoke(input=prompt_value)
            lookahead_bias = parser.invoke(response)
            break
        except Exception as e:
            print(e)
            max_retry -= 1
    return lookahead_bias


def analyze_strategy(code: str):
    llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model='gpt-4o-mini')
    class StrategyAnalysis(BaseModel):
        indicators: list[str]
        explain: str
        example: str
        strength: str
        weakness: str
        suggestion: str
        keywords: list[str]
    parser = PydanticOutputParser(pydantic_object=StrategyAnalysis)
    prompt = PromptTemplate(
        input_variables=['strategy'],
        template='''You are a Freqtrade Bot Expert. You are given a strategy to analyze. The strategy is as follows:\n\n{strategy}\n\nAnalyze the strategy and provide your insights on the strategy. Understand and explain the logic behind the strategy. Also give some keywords that help in understanding the strategy.\n{format_instruction}''',
        partial_variables={'format_instruction': parser.get_format_instructions()},
    )
    max_retry = 3
    while max_retry > 0:
        try:
            prompt_value = prompt.invoke(input={'strategy': code})
            response = llm.invoke(input=prompt_value)
            analysis = parser.invoke(response)
            break
        except Exception as e:
            print(e)
            max_retry -= 1

    return analysis

if __name__ == '__main__':
    from dotenv import load_dotenv
    import json
    load_dotenv()
    for f in glob.glob('filtered/ichi*.py'):
        code, functions = load_strategy(f)
        analysis = analyze_strategy(code)
        with open(f.replace('filtered', 'analysis').replace('.py', '.json'), 'w', encoding='utf-8') as _f:
            json.dump(analysis.model_dump(), _f, indent=4)
        lookahead_bias = find_lookahead_bias(functions)
        with open(f.replace('filtered', 'analysis').replace('.py', '_lookahead_bias.json'), 'w', encoding='utf-8') as _f:
            json.dump(lookahead_bias.model_dump(), _f, indent=4)
        with open(f.replace('filtered', 'analysis').replace('.py', '_functions.json'), 'w', encoding='utf-8') as _f:
            json.dump(functions, _f, indent=4)
        with open(f.replace('filtered', 'analysis').replace('.py', '_code.py'), 'w', encoding='utf-8') as _f:
            _f.write(code)