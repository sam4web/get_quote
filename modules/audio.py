import pyttsx3
import random


def get_rand(len):
    rand = random.randint(0, len - 1)
    return rand


# pyttsx3 engine init
engine = pyttsx3.init()
voices = engine.getProperty("voices")

# changing voice
voice = voices[get_rand(len(voices))]
engine.setProperty("voice", voice.id)

# speech rate
rate = engine.getProperty("rate")
engine.setProperty("rate", rate - 50)


# return name of the speaker
def get_voice_name(voice):
    info = voice.name
    name = info.split(" ")[1]
    country = info[info.find("(") + 1 : -1]
    return name


def audio_say(text):
    engine.say(text)
    engine.runAndWait()


def audio_save(text, file_name):
    engine.save_to_file(text, f"{file_name}.mp3")
    engine.runAndWait()
