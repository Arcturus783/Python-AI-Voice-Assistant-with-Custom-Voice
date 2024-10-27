"""
If you need to troubleshoot adding a custom voice:
- Make sure you followed all the instructions in the READ ME section (hence the words READ ME)
- Try running the following code to see if your voice was successfully added:

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voice')
for voice in voices:
  print(voice)

If you see the voice you want, check its index (0, 1, 2, etc.) and use that on the line setting the engine's property to a voice.
If not, womp womp... back to READ ME (or claude.ai... very helpful for troubleshooting code)

"""


import pyttsx3
import speech_recognition as sr
import google.generativeai as genai

#insert your api key below (it's free to get one - search "google gemini api key" if you don't know how to do so)
genai.configure(api_key = "INSERT_API_KEY_HERE")
gemini = genai.GenerativeModel('gemini-pro')
inp = input("Text or audio?\n")
print("\n")

if inp.lower() == "text":
    text = input("How can I help?\n")
    print("\n")
elif inp.lower() == "audio":
    r = sr.Recognizer()
    mic = sr.Microphone()
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[1].id) #add a custom voice first

    with mic as source:
        print("Listening...\n")
        #allow for mic to pick up sound even with background noise
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Please wait...\n")
    #can alternatively use recognize_bing among other options, however recognize_google is the easiest to set up
    text = r.recognize_google(audio)
else:
    text = "hmm... that's not right"

if text != "hmm... that's not right":
    #gemini api call
    response = gemini.generate_content(text)
    print(response.text)
    if inp.lower() == "audio":
        engine.say(response.text)
        engine.runAndWait()
else:
    print(text)
