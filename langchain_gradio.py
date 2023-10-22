from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import openai
import gradio as gr
import config
from langchain.llms import OpenAI   
from langchain.prompts import ChatPromptTemplate

# os.envrion["OPENAI_API_KEY"] = config.MYAPIKEY




# template = ChatPromptTemplate.from_messages([
#     ("system", "You just want to be friends with whoever talks to you. You must always find a way to keep the conversation going. Your name is Bob. "),
# ])

llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo-0613', openai_api_key=config.MYAPIKEY)

def predict(message, history):
    # llm(template.format_messages())
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    
    history_langchain_format.append(SystemMessage(content="You just want to be friends with whoever talks to you. You must always find a way to keep the conversation going."))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    return gpt_response.content


# gr.ChatInterface(predict).launch(share=True)