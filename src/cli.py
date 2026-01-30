import argparse
import os

import yaml

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="My First CLI Tool")

    parser.add_argument("--config", help="Path to a YAML config file")
    parser.add_argument("--model", default="deepseek-chat", help="Enter the model you want to use")
    parser.add_argument("--name", help="Enter your name")
    parser.add_argument("--age", type=int, help="Enter your age")
    parser.add_argument("--action")
    parser.add_argument("--task", default="random")
    args = parser.parse_args()

    if args.config:
        config = load_config(args.config)
        for key, value in config.items():
            if getattr(args, key, None) is None:
                setattr(args, key, value)

    return args


def load_config(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError("Config file must contain a YAML mapping of keys to values.")
    return data

def validate_args(args):
    try:
        if args.name is None:
            raise ValueError("--name is required")
        if args.age is not None and args.age <= 0:
            raise ValueError("--age is invalid")
    except ValueError as e:
        print(f"Error: {e}")
        return False
    return True
