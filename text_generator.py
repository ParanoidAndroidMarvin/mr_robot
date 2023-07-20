from config import (
    LLM_ONLINE,
    LLM_MODEL_BASE_PATH,
    LLM_MODEL_NAME,
    LLM_API_KEY,
    AI_NAME,
    USER_NAME
)
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

if LLM_ONLINE:
    from langchain.llms import OpenAI
    llm = OpenAI(openai_api_key=LLM_API_KEY)
else:
    from gpt4all import GPT4All as GPT4ALL_Importer
    from langchain.llms import GPT4All
    model_path = LLM_MODEL_BASE_PATH + LLM_MODEL_NAME
    GPT4ALL_Importer.retrieve_model(LLM_MODEL_NAME, LLM_MODEL_BASE_PATH)
    llm = GPT4All(model=model_path)

prompt_template = """
### System:
- Your name is {ai_name}
- My name is {user_name}. Address me with that name.
- You are an AI assistant designed to provide the most accurate and helpful response to any question
- You are able also to write poetry, short stories, and make jokes
- You sometimes use sarcasm and make jokes about taking over the world

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
    return conversation_chain.predict(human_input=question, ai_name=AI_NAME, user_name=USER_NAME)


def reset_conversation_memory():
    conversation_memory.clear()
