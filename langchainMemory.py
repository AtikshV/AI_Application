import openai
import gradio
import config
from langchain.memory import ConversationSummaryMemory, ChatMessageHistory
from langchain.llms import OpenAI




memory = ConversationSummaryMemory(llm=OpenAI(temperature=0, openai_api_key=config.MYAPIKEY), return_messages=True)
memory.save_context({"input": "hi"}, {"output": "whats up"})


# print(memory.load_memory_variables({}))

# messages = memory.chat_memory.messages
# previous_summary = ""
# print(memory.predict_new_summary(messages, previous_summary))

history =  ChatMessageHistory()
history.add_user_message("hello!") 
history.add_ai_message("Hey there! How's your day going? Any exciting plans ahead?")

memory = ConversationSummaryMemory.from_messages(
    llm=OpenAI(temperature=0, openai_api_key=config.MYAPIKEY),
    buffer="The human greets the AI and the AI responds by asking how the human's day is going and if they have any exciting plans ahead.",
    chat_memory=history,
    return_messages = True, 
    verbose=True
)

print(memory.buffer)






