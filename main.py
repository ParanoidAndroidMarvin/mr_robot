from config import BANNER, WAKE_WORD, SLEEP_WORD
from text_to_speech import say
from text_generator import answer
from speech_to_text import wait_for_wakeup, listen
from colorama import Fore, Style

# Setup console styling
print(Fore.GREEN + Style.BRIGHT)


def main():
    print(BANNER)
    try:
        sleeping = True
        while True:
            if sleeping:
                wait_for_wakeup(WAKE_WORD)
                sleeping = False

            text_input = listen()
            text_answer = answer(text_input)
            say(text_answer)

            if SLEEP_WORD in text_input:
                sleeping = True
                continue

    except KeyboardInterrupt:
        print("[COMPUTER] Shutdown")


if __name__ == '__main__':
    main()