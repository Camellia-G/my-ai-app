import os
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="My First CLI Tool")

    parser.add_argument("--name", help="Enter your name", required=True)
    parser.add_argument("--age", type=int, help="Enter your age",required=True)

    return parser.parse_args()


def main() :
    
    print("Projrct:\n")
    print(f"Current Directory:{os.getcwd()}")

    args = parse_args()
    print(f"Hello, {args.name}!")
    if args.age is not None:
        print(f"Next year you will be {args.age + 1}")


if __name__ == "__main__":
    main()
