from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="moonshotai/kimi-k2-instruct-0905")
