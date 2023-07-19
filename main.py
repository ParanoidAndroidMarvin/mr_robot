from config import BANNER, SLEEP_WORDS
from text_to_speech import say
from text_generator import generate_answer, reset_conversation_memory
from speech_to_text import wait_for_wakeup, listen
from colorama import Fore, Style
from time import sleep

# Setup console styling
print(Fore.GREEN + Style.BRIGHT)


def main():
    sleep(.5)
    print(BANNER)
    try:
        sleeping = True
        while True:
            # Wait for WAKE_WORD
            if sleeping:
                reset_conversation_memory()
                wait_for_wakeup()
                sleeping = False

            # Process prompt and generate answer
            prompt = listen()
            answer = generate_answer(prompt)
            sleep(1.5)  # Crashes otherwise with larger models
            say(answer)

            # Go to sleep on SLEEP_WORD
            if any(sleep_word in prompt for sleep_word in SLEEP_WORDS):
                sleeping = True
                continue

    except KeyboardInterrupt:
        print("[COMPUTER] Shutdown")


if __name__ == '__main__':
    main()