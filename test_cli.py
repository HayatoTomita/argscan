import argparse

def main():
    parser = argparse.ArgumentParser(description='テスト用CLI: 名前と年齢を表示')
    parser.add_argument('--name', type=str, required=True, help='表示する名前')
    parser.add_argument('--age', type=int, required=True, help='表示する年齢')
    
    args = parser.parse_args()
    
    print(f'こんにちは、{args.name}さん！')
    print(f'あなたは{args.age}歳ですね。')
    
    if args.age >= 20:
        print('成人ですね！')
    else:
        print('未成年ですね！')

if __name__ == '__main__':
    main() 