import os
import argparse
import requests
from dotenv import load_dotenv

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="My First CLI Tool")

    parser.add_argument("--model",default="deepseek-chat",help="Enter the model you want to use")
    parser.add_argument("--name", help="Enter your name", required=True)
    parser.add_argument("--age", type=int, help="Enter your age")
    parser.add_argument("--repeat",type=int)

    return parser.parse_args()

def get_info():
    response=requests.get("https://v1.hitokoto.cn/")
    if response.status_code == 200:
        data  = response.json()
        print(f"A wonderful sentence: {data['hitokoto']}")
        print(f"From: {data['from']}")

def main() :
    
    print("Projrct:\n")
    print(f"Current Directory:{os.getcwd()}")
    try:
        args = parse_args()
        print(f"Hello, {args.name}!")
        if args.age <=0:
            raise ValueError("--age is invalid")
        print(f"Next year you will be {args.age + 1}")
        
        load_dotenv()
        key=os.getenv("MY_SECRET_KEY")
        print(f"LoadedKey: {key}")

        get_info()

    except ValueError as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
