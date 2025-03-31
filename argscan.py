import ast
import yaml
from typing import Dict, Any, List
import argparse
import sys

def get_default_value(arg_type: str) -> Any:
    """引数の型に応じたデフォルト値を返す"""
    type_mapping = {
        'str': '',
        'int': 0,
        'float': 0.0,
        'bool': False,
        'list': [],
        'tuple': (),
        'dict': {},
    }
    return type_mapping.get(arg_type, None)

def extract_argparse_args(source_code: str) -> Dict[str, Any]:
    """argparseのコードから引数情報を抽出"""
    tree = ast.parse(source_code)
    args_info = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr == 'add_argument':
                # 引数名を取得
                arg_name = None
                arg_type = 'str'  # デフォルトは文字列
                
                for keyword in node.keywords:
                    if keyword.arg == 'type':
                        if isinstance(keyword.value, ast.Name):
                            arg_type = keyword.value.id
                    elif keyword.arg == 'dest':
                        if isinstance(keyword.value, ast.Constant):
                            arg_name = keyword.value.value
                
                # 位置引数から引数名を取得
                if not arg_name and node.args:
                    arg = node.args[0]
                    if isinstance(arg, ast.Constant):
                        arg_name = arg.value.strip('-')
                
                if arg_name:
                    args_info[arg_name] = get_default_value(arg_type)
    
    return args_info

def main():
    parser = argparse.ArgumentParser(description='argparseのコードを解析してYAMLを生成')
    parser.add_argument('input_file', help='解析するPythonファイルのパス')
    parser.add_argument('--output', '-o', help='出力するYAMLファイルのパス（省略時は標準出力）')
    
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        args_info = extract_argparse_args(source_code)
        
        yaml_data = yaml.dump(args_info, allow_unicode=True, sort_keys=False)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(yaml_data)
        else:
            print(yaml_data)
            
    except Exception as e:
        print(f'エラーが発生しました: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main() 