import os
from cli import parse_args, validate_args
from core import OutPut

def main() :
    
    print("------Project:")
    print(f"Current Directory:{os.getcwd()}")
    args = parse_args()
    validate_args(args)
    OutPut(args)


if __name__ == "__main__":
    main()
