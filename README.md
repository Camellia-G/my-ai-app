# My AI App

A Python project。

## project structure

```
my-ai-app/
├── src/
│   ├── __init__.py
│   ├── main.py          # Main entry point
│   ├── cli.py           # Command-line argument parsing
│   ├── core.py          # Core functionality (random sentences, AI suggestions, chat mode)
│   └── ai_engine.py     # AI chat engine
├── tests/
│   └── test_cli.py      # Test files
├── .env                 # Environment variables configuration
├── .gitignore
├── requirements.txt
└── README.md
```

## Tech Stack
Language: Python 3.10+  
Version Control: Git&GitHub


## installation

1. git clone https://github.com/your-username/my-ai-app.git
cd my-ai-app
2. create a `.env` file and add your API key
    API_KEY=you_api_key

## Usage
Run the application from the project root：
```bash
python src/main.py --name Camellia --age 22 --task ai-sug 
```

Learning Progress:

Day 1:   
    (1) set up a Python project and commit the project files using git  
    (2) learn how to use argparse, including ArgumentParser()、add_argument()、parse_args()  
    (3) Added validation and error handling for invalid input values (e.g. age <= 0, repeat <= 0)
Day 2:  
    (1) clarify env and request logic  
    (2) integrate DeepSeek API  
Day 3:  
    (1) integrate ai-chat  
    (2) test cli.py  

## Args

Command-line arguments:

```
Argument Structure:
├── --name (required)
│   └── Type: string
│   └── Description: User's name
│
├── --age (optional)
│   └── Type: int
│   └── Description: User's age, must be > 0
│
├── --model (optional)
│   └── Default: "deepseek-chat"
│   └── Description: Specify the AI model to use
│
├── --action (optional)
│   ├── "quote"
│   │   └── Function: Display quote information (random sentence or AI suggestion based on --task)
│   └── "ai-chat"
│       └── Function: Start AI chat mode (interactive conversation)
│
└── --task (optional)
    ├── Default: "random"
    ├── "random"
    │   └── Function: Get random sentence from Hitokoto API
    └── "ai-sug"
        └── Function: Get AI study/work suggestions (requires --age parameter)
```   

    