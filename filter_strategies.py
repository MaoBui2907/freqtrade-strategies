import ast
import glob
import shutil
import os
from tqdm import tqdm

def get_class_name(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        root = ast.parse(f.read())
    
    for node in ast.walk(root):
        if isinstance(node, ast.ClassDef):
            return node.name


def main():
    with open('errors.txt', 'r', encoding='utf-8') as f:
        errors = f.read().splitlines()
    raw_strategies = glob.glob('raws/*/*.py')
    shutil.rmtree('strategies/', ignore_errors=True)
    os.makedirs('strategies/', exist_ok=True)
    shutil.rmtree('errors/', ignore_errors=True)
    os.makedirs('errors/', exist_ok=True)
    for strategy in tqdm(raw_strategies):
        if get_class_name(strategy) not in errors:
            shutil.copy(strategy, 'strategies/')
        else:
            shutil.copy(strategy, 'errors/')
        

if __name__ == '__main__':
    main()