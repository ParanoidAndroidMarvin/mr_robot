import pyttsx4

from threading import Thread
from config import VOICE_ID

engine = pyttsx4.init()
engine.setProperty('voice', VOICE_ID)
engine.setProperty('rate', 175)


def say(text: str) -> None:
    print("[COMPUTER] Says: \"" + text + "\"")
    thread = Thread(target=_say, args=(text,))
    thread.start()
    thread.join()


def _say(text):
    engine.say(text)
    engine.runAndWait()