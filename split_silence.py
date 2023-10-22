import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


r = sr.Recognizer(); 
mic = sr.Microphone(); 


with mic as source:
    audio = r.listen(source)


print(r.recognize_google(audio))


# def transcribe_audio(path):
#     with sr.AudioFile(path) as source: 
#         audio_listened = r.record(source)

#         text = r.recognize_google(audio_listened)

#     return text


# def get_large_audio_transcription_on_silence(path):
#     return 1