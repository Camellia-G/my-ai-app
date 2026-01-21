# My AI App

A Python project。

## project structure

```
my-ai-app/
├── src/
│   ├── __init__.py
│   └── main.py
├── .env
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
## Args 
--name、--age、--model、--action(quote)、--task(ai-sug or random)   


Learning Progress:

Day 1:   
    (1) set up a Python project and commit the project files using git  
    (2) learn how to use argparse, including ArgumentParser()、add_argument()、parse_args()  
    (3) Added validation and error handling for invalid input values (e.g. age <= 0, repeat <= 0)
Day 2:  
    (1) clarify env and request logic  
    (2) integrate DeepSeek API  