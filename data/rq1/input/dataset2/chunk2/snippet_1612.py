#Source: https://stackoverflow.com/questions/77457590/creating-chat-agent-with-langchain-and-openai-getting-no-attribute-error
from config import api_key,new_personal_api_key

apikey=new_personal_api_key

# apikey=api_key

import os

os.environ['OPENAI_API_KEY'] = apikey


from langchain.chains.conversation.memory import ConversationBufferWindowMemory


from langchain.agents import Tool
from langchain.tools import BaseTool

def meaning_of_life(input=""):
    return 'The meaning of life is 42 if rounded but is actually 42.17658'
    
life_tool = Tool(
    name='Meaning of Life',
    func= meaning_of_life,
    description="Useful for when you need to answer questions about the meaning of life. input should be MOL "
)


import random

def random_num(input=""):
    return random.randint(0,5)
    
    
random_tool = Tool(
    name='Random number',
    func= random_num,
    description="Useful for when you need to get a random number. input should be 'random'"
)

from langchain import OpenAI 
from langchain.chat_models import ChatOpenAI

# Set up the turbo LLM
turbo_llm = ChatOpenAI(
    temperature=0,
    model_name='gpt-3.5-turbo'
)



from langchain.agents import initialize_agent

tools = [random_tool, life_tool]

# conversational agent memory
memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=3,
    return_messages=True
)


# create our agent
conversational_agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=turbo_llm,
#     llm=local_llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=memory,
    handle_parsing_errors=True
)


conversational_agent('Can you give me a random number?')