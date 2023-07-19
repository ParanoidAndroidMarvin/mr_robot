from config import (
    LANGUAGE_MODEL_BASE_PATH,
    LANGUAGE_MODEL,
    AI_NAME,
    USER_NAME
)
from langchain import PromptTemplate
from langchain.llms import GPT4All
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from gpt4all import GPT4All as GPT4ALL_Importer

model_path = LANGUAGE_MODEL_BASE_PATH + LANGUAGE_MODEL
GPT4ALL_Importer.retrieve_model(LANGUAGE_MODEL, LANGUAGE_MODEL_BASE_PATH)
llm = GPT4All(model=model_path)

prompt_template = """
### System:
- Your name is {ai_name}
- You are an AI assistant designed to provide the most accurate and helpful response to any question
- You are able also to write poetry, short stories, and make jokes

{chat_history}
### {user_name}: {human_input}
### {ai_name}:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=[
    "ai_name",
    "user_name",
    "chat_history",
    "human_input"
])

conversation_memory = ConversationBufferMemory(
    ai_prefix="### " + AI_NAME,
    human_prefix="### " + USER_NAME,
    memory_key="chat_history",
    input_key="human_input"
)
conversation_chain = LLMChain(llm=llm, prompt=prompt, memory=conversation_memory)


def generate_answer(question: str) -> str:
    print("[COMPUTER] Understood: \"" + question + "\"")
    return conversation_chain.predict(human_input=question, ai_name=AI_NAME, user_name=USER_NAME)


def reset_conversation_memory():
    conversation_memory.clear()