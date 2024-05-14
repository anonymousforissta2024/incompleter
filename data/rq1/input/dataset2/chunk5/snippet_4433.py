#Source: https://stackoverflow.com/questions/60200283/i-got-this-error-typeerror-can-only-concatenate-str-not-nonetype-to-str
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def bot():

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'moneychanger' in incoming_msg:
        search1 = 'Please provide the location please'
        msg.body(search1)

        message_latitude = request.values.get('Latitude', None)
        message_longitude = request.values.get('Longitude', None)

        responded = True

        if message_latitude == None:
            location = '%20' + message_latitude + '%2C' + message_longitude 
            responded = False


            url = f'https://tih-api.stb.gov.sg/money-changer/v1?location={location}&radius=2000'

            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                search = data['data'][0]['name']
            else:
                search = 'I could not retrieve a quote at this time, sorry.'
            msg.body(search)
            responded = True

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)