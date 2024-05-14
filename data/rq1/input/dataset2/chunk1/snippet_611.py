#Source: https://stackoverflow.com/questions/75825362/attributeerror-encode-when-returning-streamingresponse-in-fastapi
import openai

def chat_stream(question: str, key: str):
    openai.api_key = key
    # create a completion
    completion = openai.Completion.create(model="text-davinci-003",
                                          prompt=question,
                                          stream=True)
    return completion