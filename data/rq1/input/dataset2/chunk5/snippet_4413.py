#Source: https://stackoverflow.com/questions/71905524/vonage-voice-api-calling-error-exception-has-occurred-typeerror-expecting-a-p
import os
from os.path import join, dirname
from pprint import pprint
from vonage import *
from dotenv import load_dotenv

dotenv_path = join(dirname(file), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
VONAGE_NUMBER = os.environ.get("VONAGE_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")

client = vonage.Client(
application_id=VONAGE_APPLICATION_ID,
private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

voice = vonage.Voice(client)

response = voice.create_call({
'to': [{'type': 'phone', 'number': TO_NUMBER}],
'from': {'type': 'phone', 'number': VONAGE_NUMBER},
'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
})

pprint(response)