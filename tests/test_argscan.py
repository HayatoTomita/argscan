import unittest
import sys
import os
import yaml
from io import StringIO

# プロジェクトのルートディレクトリをPythonパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from argscan import main

class TestArgscan(unittest.TestCase):
    def setUp(self):
        # テスト用の出力をキャプチャするためのStringIO
        self.output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        # 標準出力を元に戻す
        sys.stdout = self.original_stdout
        self.output.close()

    def test_extract_args_from_test_cli(self):
        # テスト用CLIファイルのパス
        test_cli_path = os.path.join(os.path.dirname(__file__), '..', 'test_cli.py')
        
        # argscanを実行
        sys.argv = ['argscan.py', test_cli_path]
        main()
        
        # 出力を取得
        output = self.output.getvalue()
        
        # 出力をYAMLとしてパースし、期待される値と比較
        parsed_output = yaml.safe_load(output)
        expected_values = {
            'name': '',
            'age': 0
        }
        
        self.assertEqual(parsed_output, expected_values)

if __name__ == '__main__':
    unittest.main() 