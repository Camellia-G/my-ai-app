import os
from openai import OpenAI

class ChatSession:
    def __init__(self,model="deepseek-chat"):
        self.client=OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
        )
        self.model=model
        self.messages=[
            {"role":"system","content":"你是一个专业的开发助手。"}
        ]

    def chat(self,user_input:str):
        self.messages.append({"role":"user","content":user_input})

        try:
            response=self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                stream=True
            )
            print("🤖 AI: ", end="", flush=True)
            full_reply=""
            for chunk in response:
                content=chunk.choices[0].delta.content
                if content:
                    print(content,end="",flush=True)
                    full_reply+=content
            print("\n")
            self.messages.append({"role":"assistant","content":full_reply})
        except Exception as e:
            print(f"\n❌ 聊天出错: {e}")