import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
apikey=os.getenv("key")

llm=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1.5,
    max_tokens=100,
    reasoning_effort="low",
    api_key=apikey
)

# while True:
#     temp="Create a {context} on {topic} for {audience}"
#     finalpt=temp.format(audience=input("a"),topic=input("t"),context=input("c"))
#     result=llm.invoke(finalpt)
#     print(result.content) # it stores AIMESSAGE 