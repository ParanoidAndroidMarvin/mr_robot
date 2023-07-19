import sounddevice as sd
import sys
import json

from queue import Queue
from vosk import Model, KaldiRecognizer
from config import WAKE_WORDS, LANGUAGE

queue = Queue()

samplerate = sd.query_devices(sd.default.device[0], "input")["default_samplerate"]
wake_word_collection = ["\"" + word + "\"" for wake_word in WAKE_WORDS for word in wake_word.split(" ")]

# Language Model
model = Model(lang=LANGUAGE)
recognizer = KaldiRecognizer(model, samplerate)
recognizer_idle = KaldiRecognizer(model, samplerate, '[' + ', '.join(wake_word_collection) + ', "[unk]"]')


def _record_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    queue.put(bytes(indata))


def wait_for_wakeup():
    print("[COMPUTER] Sleeping...")
    try:
        with sd.RawInputStream(dtype='int16', channels=1, callback=_record_callback):
            while True:
                data = queue.get()
                if not recognizer_idle.AcceptWaveform(data):
                    result = json.loads(recognizer_idle.PartialResult())["partial"]
                    if any(wake_word in result for wake_word in WAKE_WORDS):
                        recognizer_idle.Reset()
                        break
                else:
                    recognizer_idle.Reset()

    except Exception as e:
        print(str(e))


def listen() -> str:
    print("[COMPUTER] Listening...")
    try:
        with sd.RawInputStream(dtype='int16', channels=1, callback=_record_callback):
            while True:
                data = queue.get()
                if recognizer.AcceptWaveform(data):
                    recognizer_result = recognizer.Result()
                    result = json.loads(recognizer_result)["text"]
                    if not result == "":
                        return result

    except Exception as e:
        print(str(e))