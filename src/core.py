import os
import requests

from ai_engine import ChatSession
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def random_sentence():
    response=requests.get("https://v1.hitokoto.cn/")
    if response.status_code == 200:
        data  = response.json()
        print(f"A wonderful sentence: {data['hitokoto']}")
        print(f"From: {data['from']}")

def get_ai_suggestion(args):
    key=os.getenv("DEEPSEEK_API_KEY")
    client=OpenAI(
        api_key=key,
        base_url="https://api.deepseek.com"
    )
    try:
        print("🤖 AI thinking...")
        response = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "system", "content": "你是一个幽默的人生导师。"},
                {"role":"user","content":f"I am a studenet.{args.age} years old.give me some suggestions about studying or working.Do not ask me any questions.answer me in English.use 150 words."}
            ],
            stream=False
        )
        
        content=response.choices[0].message.content
        print(f"\n✨ AI's suggestion: {content}")
    except Exception as e:
        print(f"❌ AI not work: {e}")

def get_info(args):
    if(args.task=="random"):
        random_sentence()
    if(args.task=="ai-sug"):
        get_ai_suggestion(args)

def start_chat_mode():
    session=ChatSession()
    print("--- 已进入 AI 聊天模式 (输入 'quit' 退出) ---")
    while True:
        user_input = input("👤 You:")
        if user_input.lower() in ['quit','exit','quit()']:
            print("Bye!")
            break
        if not user_input.strip():
            continue
        session.chat(user_input)


def OutPut(args):
    print(f"Hello, {args.name}!")
    print(f"Next year you will be {args.age + 1}")
        
    if(args.action=="quote"):
        get_info(args)
    elif(args.action=="ai-chat"):
        start_chat_mode()
