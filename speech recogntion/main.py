import speech_recognition as sr

r = sr.Recognizer()

    
def speech():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
                
        try:
            print("Text: "+r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")
while True:
    i=input()
    if i =="0":
        break
    else:
        speech()
    
