# argscan

argparseを使用したPythonスクリプトから引数情報を抽出し、YAMLファイルを生成するツールです。

このプロジェクトは [Cursor](https://cursor.sh/) を使用して開発されました。

## 機能

- argparseのコードを解析し、引数名と型を抽出
- 型に応じた適切なデフォルト値を生成
- YAML形式での出力

## インストール

```bash
# uvを使用してインストール
uv venv
.venv/Scripts/activate  # Windowsの場合
source .venv/bin/activate  # Unix系の場合
uv pip install -e .
```

## 使用方法

```bash
# 基本的な使用方法
python -m argscan 入力ファイル.py

# 出力ファイルを指定する場合
python -m argscan 入力ファイル.py -o 出力ファイル.yaml
```

### 入力ファイルの例（test_cli.py）

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='テスト用CLI')
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--age', type=int, required=True)
    
    args = parser.parse_args()
```

### 出力例

```yaml
name: ""
age: 0
```

## 対応している型

- str: 空文字列 (`""`)
- int: `0`
- float: `0.0`
- bool: `false`
- list: `[]`
- tuple: `()`
- dict: `{}`

## 開発

```bash
# テストの実行
python -m pytest tests -v
```

## ライセンス

MITライセンス
