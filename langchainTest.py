import openai
import gradio
import config
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate  ,
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate,
)

openai.api_key = config.MYAPIKEY

text = "What would be a good company name for a company that makes colorful socks?"
humanMsg = [HumanMessage(content=text)]

llm = OpenAI(openai_api_key=config.MYAPIKEY)
chat_model = ChatOpenAI(openai_api_key=config.MYAPIKEY)

print(chat_model.predict_messages(humanMsg))



# prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
# prompt.format(product="colorful socks") 

# print(chat_model.predict_messages(prompt))


