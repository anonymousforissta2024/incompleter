#Source: https://stackoverflow.com/questions/75031533/attributeerror-text-in-django
from django.shortcuts import render
import openai


# Create your views here.

def chatbot_view(request):
    # Get the user's input from the request
    user_input = request.POST.get("user_input") 
    # Use the OpenAI library to generate a response
    openai.api_key = "MY-API"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=1024,
        temperature=0.7,
    )
    chatbot_response = response.text

    # Render the response in a template
    return render(request, 'chat/index.html', {"chatbot_response": chatbot_response})