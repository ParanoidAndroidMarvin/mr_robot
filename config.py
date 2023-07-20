from dotenv import load_dotenv
import os

load_dotenv()

BANNER = """
 ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗  ██████╔╝
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
"""  # Generated by: https://manytools.org/hacker-tools/ascii-banner/

###############
#   General   #
###############
WAKE_WORDS = ["hey computer", "wake up"]
SLEEP_WORDS = ["computer go to sleep", "good night"]

######################
#   Speech to text   #
######################
STT_LANGUAGE = "en-us"

######################
#   Text generator   #
######################
LLM_USER_NAME = "Human"
LLM_AI_NAME = "Computer"
LLM_ONLINE = True
# Only required if ONLINE = False
LLM_MODEL_BASE_PATH = "./models/"
LLM_MODEL_NAME = "nous-hermes-13b.ggmlv3.q4_0.bin"
# Only required if ONLINE = True
LLM_API_KEY = os.getenv("API_KEY")

######################
#   Text to speech   #
######################
TTS_VOICE_ID = 'com.apple.eloquence.en-US.Reed'
