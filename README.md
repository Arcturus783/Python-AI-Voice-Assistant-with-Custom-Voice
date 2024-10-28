# Python AI Voice Assistant with Custom Voice

This is a quick tutorial on creating a basic Gemini voice assistant with a *custom* voice (because the default voice sounds like Ultron having a really bad day). Note that I did this with Windows and VS Code, however, it is possible on a Macbook (the concept will be the same but you'll have to find another way to download the voice). The assistant is Gemini itself, so it can write stories, recipes, answer questions, and access information from the internet.

## Preparation

### Imports

You'll need the following libraries:
- pyttsx3 (for text to speech)
- speech_recognition (for speech to text)
- google.generativeai (for...well, hopefully this one is clear)

If you have PIP, run the following statements in a terminal (such as Command Prompt) to install the necessary libraries:

`pip install pyttsx3`
`pip install SpeechRecognition`
`pip install google-generativeai`


### Gemini API Key

Visit [this](https://aistudio.google.com/app/apikey) link to get an API key for Gemini. It's completely free although there are some limitations, so it may not be ideal for production code.

### (Optionally) Get a Custom Voice

Warning - this was the longest part for me. For simplicity's sake, I'll only describe getting a Microsoft-made voice on a Windows (ideally 10 or higher) laptop, however in theory you could get a voice engine from the internet as well.

1. On your laptop, use **Ctrl + Windows + N** to open your Narrator settings (or do it manually, but that's boring).
2. Choose from the options under "Choose a Voice" *or* the options shown when you click "Add natural voices".
3. When the voice installs, open Command Prompt or another terminal.
4. Run the following command to open the Windows Registry: `regedit`
5. Check the following path: `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens`. If you installed your voice of choice in step 2, you should see a folder for that voice in tokens (hint: look for the voice name, like "Mark").
6. Check the following path: `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens`. If you see the voice file there, move on to the next section. If not, keep going through these steps.
7. In the first path you checked, right click on your voice of choice and click "Export". Create a .reg file for it.
8. In File Explorer, double click and open the .reg file - it will warn you to be careful when messing with registries, click "yes" or "continue".
9. Go back to step 6.
10. If somehow this doesn't help you, I'd recommend asking an AI assistant (ironic, I know). I use (Claude)[claude.ai], but Gemini will also be helpul for troubleshooting the problem.

## Writing Code

At this point, you're ready to write your program. This repository includes simple, command-line-based programs you can use, however, I'll briefly go over the most basic use case.

First, write in your import statements:

```
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
```

Next, create an instance of Gemini (with your API key from earlier):

```
genai.configure(api_key = "INSERT_API_KEY_HERE")
gemini = genai.GenerativeModel('gemini-pro')
```

Create your essential speech-to-text components:

```
r = sr.Recognizer()
mic = sr.Microphone()
```

Capture user input - the library will start listening after the listen() method is called when it hears speaking and will stop when the speaking stops:

```
print("Listening...\n")
r.adjust_for_ambient_noise(source)
audio = r.listen(source)
print("Please wait...\n")
```

Identify what the user just asked/said:

`text = r.recognize_google(audio)`

Make a call to Gemini with what the user just asked/said:

`response = gemini.generate_content(text)`

Initialize your text-to-speech engine:

`engine = pyttsx3.init()`

Set the voice for the engine:

`engine.setProperty('voice', engine.getProperty('voices')[1].id)`
Note - if this isn't setting the voice correctly, look at the comments at the top of the Custom Voice program in this repository.

Have the engine say what Gemini responded with:

```
engine.say(response.text)
engine.runAndWait()
```

## Conclusion

Hopefully, you were able to make this program work! If not, try looking at the program file for the default voice (it's almost the same as for a custom voice). If you need additional troubleshooting resources, look up specific questions you may have pertaining to the libraries *or* ask an AI chatbot like [Claude](claude.ai) or [Gemini](https://gemini.google.com/app).
