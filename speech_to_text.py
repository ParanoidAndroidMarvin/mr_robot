import sounddevice as sd
import sys
import json

from queue import Queue
from vosk import Model, KaldiRecognizer
from output import print_computer, print_human
from config import (
    WAKE_WORDS,
    STT_LANGUAGE,
)

queue = Queue()

samplerate = sd.query_devices(sd.default.device[0], "input")["default_samplerate"]
wake_word_collection = ["\"" + word + "\"" for wake_word in WAKE_WORDS for word in wake_word.split(" ")]

# Language Model
model = Model(lang=STT_LANGUAGE)
recognizer = KaldiRecognizer(model, samplerate)
recognizer_idle = KaldiRecognizer(model, samplerate, '[' + ', '.join(wake_word_collection) + ', "[unk]"]')


def _record_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    queue.put(bytes(indata))


def wait_for_wakeup():
    print_computer("Sleeping...")
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
    print_computer("Listening...")
    try:
        with sd.RawInputStream(dtype='int16', channels=1, callback=_record_callback):
            while True:
                data = queue.get()
                if recognizer.AcceptWaveform(data):
                    recognizer_result = recognizer.Result()
                    prompt = json.loads(recognizer_result)["text"]
                    if not prompt == "":
                        print_human("\"" + prompt + "\"")
                        return prompt

    except Exception as e:
        print(str(e))
