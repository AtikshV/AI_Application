def speak(): 
    playsound("chatGPT.mp3")

def threadedSpeech():
    if __name__ == "__main__": 
        p = multiprocessing.Process(target=speak, args=())
        p.start()

        while p.is_alive(): 
            if keyboard.is_pressed("esc"): 
                p.terminate()
            else: 
                continue
        
        p.join()

