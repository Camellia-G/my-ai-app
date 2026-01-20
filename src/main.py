import os
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="My First CLI Tool")

    parser.add_argument("--name", help="Enter your name", required=True)
    parser.add_argument("--age", type=int, help="Enter your age")
    parser.add_argument("--repeat",type=int)

    return parser.parse_args()


def main() :
    
    print("Projrct:\n")
    print(f"Current Directory:{os.getcwd()}")
    try:
        args = parse_args()
        if args.repeat is None or args.repeat <= 0:
            raise ValueError("--repeat must be apositive integer")
        for i in range(args.repeat):
            print(f"Hello, {args.name}!")
        if args.age <=0:
            raise ValueError("--age is invalid")
        print(f"Next year you will be {args.age + 1}")
        
    except ValueError as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
