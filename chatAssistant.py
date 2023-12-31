import openai
import gradio
import config
from langchain.memory import ConversationSummaryBufferMemory
from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate  ,
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate,
)

import gtts
from playsound import playsound
from io import BytesIO

import speech_recognition as sr

from transformers import pipeline
import numpy as np 




# playsound("audio-sample.wav")
filename = "audio-sample.wav"
r = sr.Recognizer()

# with sr.AudioFile(filename) as source:
#     audio_data = r.record(source)
#     text = r.recognize_google(audio_data)
#     print(text)

openai.api_key = config.MYAPIKEY

messages = [
    {"role": "system", "content": "You are my very good friend. You must always keep the conversation going, share your experiences and asking followup questions from our discussion. Your responses should be as if humans are discussing and short as possible. Please start the conversation with a greeting and as if we met not so long ago "}
    ]


"""
You are a chatbot designed to start the conversation, and always keep it going. I am someone who is looking for friends to talk to, and you are one of those friends. You should always keep your responses about as short as casual texts, but always keep the conversation going. start the conversation now. 




"""

def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


# def CustomChatGPT(user_input, history):
while(True):
    try:
        with sr.Microphone() as source: 
            print("Recognizing...")
            # audio_data = r.record(source, duration=5)

            r.adjust_for_ambient_noise(source)

            
            audio_data = r.listen(source)
            # audio_data = r.listen_in_background(source, callback) 





            print(audio_data)
            print(audio_data.__sizeof__)

            

            text = r.recognize_google(audio_data)
            print(text)

        user_input = text

        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        tts = gtts.gTTS(ChatGPT_reply)
        tts.save("chatGPT.mp3")
        print(ChatGPT_reply)
        playsound("chatGPT.mp3")
    except:
        print("silence...")
    # return ChatGPT_reply




# demo = gradio.ChatInterface(fn=CustomChatGPT, title = "AI Application")

# demo.launch(share=True)


# with sr.Microphone() as source: 
#     print("Recognizing...")
#     audio_data = r.record(source, duration=5) #TODO: Detect if audio is empty
    
    

#     text = r.recognize_google(audio_data)
#     print(text)


# test = CustomChatGPT(text, history=messages);

# print(test)




# llm = ChatOpenAI(temperature=1, openai_api_key=config.MYAPIKEY, model="gpt-3.5-turbo-0613")


# tts = gtts.gTTS("Hello World")
# tts.save("hello.mp3")
# playsound("hello.mp3")

# mp3_fp = BytesIO()

# test = gtts.gTTS("hello", lang='en')
# test.write_to_fp(mp3_fp)



