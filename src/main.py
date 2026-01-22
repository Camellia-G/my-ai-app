import os
from cli import parse_args, validate_args
from core import OutPut

def main() :
    
    print("------Project:")
    print(f"Current Directory:{os.getcwd()}")
    args = parse_args()
    if not validate_args(args):
        exit()
    OutPut(args)


if __name__ == "__main__":
    main()
