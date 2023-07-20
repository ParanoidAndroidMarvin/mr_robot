from config import SLEEP_WORDS
from text_to_speech import say
from text_generator import generate_answer, reset_conversation_memory
from speech_to_text import wait_for_wakeup, listen
from output import print_computer, print_banner
from time import sleep


def main():
    sleep(.5)
    print_banner()
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
            say(answer)

            # Go to sleep on SLEEP_WORD
            if any(sleep_word in prompt for sleep_word in SLEEP_WORDS):
                sleeping = True
                continue

    except KeyboardInterrupt:
        print_computer("Shutdown")


if __name__ == '__main__':
    main()