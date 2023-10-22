import openai
import gradio
import config

import gtts
from playsound import playsound

from transformers import pipeline
import numpy as np




openai.api_key = config.MYAPIKEY

messages = [{"role": "system", "content": "You just want to be friends with whoever talks to you. You must always keep the conversation going."}]
#TODO: Have the bot start the conversation. 


def CustomChatGPT(user_input, history):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    tts = gtts.gTTS(ChatGPT_reply)
    tts.save("chatGPT.mp3")
    playsound("chatGPT.mp3")

    return ChatGPT_reply




demo = gradio.ChatInterface(fn=CustomChatGPT, title = "AI Application")

demo.launch(share=True)

# demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "AI Application")



# transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

# def transcribe(audio):
#     sr, y = audio
#     y = y.astype(np.float32)
#     y /= np.max(np.abs(y))

#     return transcriber({"sampling_rate": sr, "raw": y})["text"]


# demo = gradio.Interface(
#     transcribe,
#     gradio.Audio(source="microphone"),
#     "text",
# )

# demo.launch()





# demo = gradio.ChatInterface(fn=CustomChatGPT)

# demo = gradio.ChatInterface(
#     fn=CustomChatGPT, 

# )


