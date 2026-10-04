import asyncio
import os
import httpx
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

class ChatService:
    def __init__(self,prompt:str):
        api_key=os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        self.api_key=api_key
        self.base_url="https://openrouter.ai/api/v1"
        self.prompt=prompt
        self.client=AsyncOpenAI(
                api_key=os.getenv("OPENROUTER_API_KEY"),
                base_url="https://openrouter.ai/api/v1"
            )
        self.prompt=prompt

    async def chatbot(self,model:str="nvidia/nemotron-3-ultra-550b-a55b:free"):
        response=await self.client.chat.completions.create(
            model=model,
            messages=[
                {"role":"system","content":"Chat Assistant"},
                {"role":"user","content":self.prompt}
            ]



        )

        return response.choices[0].message.content


async def main():
    prompt=input("Please ask your Query")
    service=ChatService(prompt)
    reply=await service.chatbot()
    print(reply)


if __name__=="__main__":
    asyncio.run(main())

    

        



    

    

   
