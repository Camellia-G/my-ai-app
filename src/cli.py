import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="My First CLI Tool")

    parser.add_argument("--model",default="deepseek-chat",help="Enter the model you want to use")
    parser.add_argument("--name", help="Enter your name", required=True)
    parser.add_argument("--age", type=int, help="Enter your age")
    parser.add_argument("--action")
    parser.add_argument("--task",default="random")
    return parser.parse_args()

def validate_args(args):
    try:
        if args.name is None:
            raise ValueError("--name is required")
        if args.age <=0:
            raise ValueError("--age is invalid")
    except ValueError as e:
        print(f"Error: {e}")
        return False
    return True

