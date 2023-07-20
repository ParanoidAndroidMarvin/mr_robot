import pyttsx4

from threading import Thread
from config import TTS_VOICE_ID
from output import print_computer

engine = pyttsx4.init()
engine.setProperty('voice', TTS_VOICE_ID)
engine.setProperty('rate', 175)


def say(text: str) -> None:
    print_computer("\"" + text + "\"")
    thread = Thread(target=_say, args=(text,))
    thread.start()
    thread.join()


def _say(text):
    engine.say(text)
    engine.runAndWait()
