import openai
import gradio
import config

openai.api_key = config.MYAPIKEY

messages = [{"role": "system", "content": "You just want to be friends with whoever talks to you. You must always keep the conversation going."}]

def CustomChatGPT(user_input, history):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "AI Application")

demo = gradio.ChatInterface(fn=CustomChatGPT)


# demo = gradio.ChatInterface(fn=CustomChatGPT, title = "AI Application")

demo.launch(share=True)