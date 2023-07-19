from gpt4all import GPT4All
from config import LANGUAGE_MODEL

model = GPT4All(LANGUAGE_MODEL)
session = []


def generate_answer(text: str) -> str:
    print("[COMPUTER] Understood: \"" + text + "\"")
    global session
    with model.chat_session():
        model.current_chat_session = session
        output = model.generate(text, top_k=5)
        session = model.current_chat_session
        return output
