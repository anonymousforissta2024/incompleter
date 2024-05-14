#Source: https://stackoverflow.com/questions/60990464/kivy-buildozer-attributeerror-nonetype-object-has-no-attribute-text
import kivy
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.textinput import TextInput  
import random
from kivy.clock import Clock
from kivy.properties import ObjectProperty
import requests
import json

def login (name,password):
    url_login = 'URL'
    payload = {'email': name, 'password': password}
    headers = {'content-type': 'application/json'}
    r = requests.post(url_login, data=json.dumps(payload), headers=headers).json()
    return (r['token'])
token =login("ID","PW")

class ConnectPage(GridLayout):
    oee = ObjectProperty(None)
    performance = ObjectProperty(None)
    quality = ObjectProperty(None)
    availability = ObjectProperty(None)
    sensorstandort = ObjectProperty(None)
    schicht = ObjectProperty(None)
    timestamp = ObjectProperty(None)
    alert = ObjectProperty(None)

    def oee_anzeige(self, *args):
        #Anfrage an Server senden
        url_report = 'URL/'
        payload_report = {}
        headers_report = {'content-type': 'application/json', 'Authorization': token}
        r_report = requests.get(url_report, data=json.dumps(payload_report), headers=headers_report)
        response = r_report.json()

        #Schicht, Sensorstandort und ggfs. Störgrund raussuchen
        x = 0
        for i in response['included']:
            if response['included'][x]['type'] == 'shift':
                schicht = response['included'][x]['attributes']['name']
            if response['included'][x]['type'] == 'location':
                sensorstandort = response['included'][x]['attributes']['name']
            if response['included'][x]['type'] == 'notification':

                timestamp = str(response['included'][x]['attributes']['inserted-at'])
                timestamp = timestamp[11:16] + ' Uhr'

                #self.timestamp.text = timestamp
                if response['included'][x]['attributes']['triggered-by'] == 'standstill':
                    self.alert.text = "Verfügbarkeitsverlust seit"
                elif sensorstandort == response['included'][x]['attributes']['triggered-by'] == 'slowdown':
                    self.alert.text = "Leistungsverlust seit"
            x +=1






        #oee Werte aus API ziehen
        oee = str(response['data']['attributes']['oee']) + " %"
        availability = str(response['data']['attributes']['availability']) + " %"
        performance =str(response['data']['attributes']['performance']) + " %"
        quality = str(response['data']['attributes']['quality']) + " %"




        #Labels definieren
        self.oee.text = oee
        self.availability.text = availability
        self.performance.text = performance
        self.quality.text = quality
        self.sensorstandort.text = sensorstandort
        self.schicht.text = schicht


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2  # used for our grid


class EpicApp(App):
    def build(self):
        t = ConnectPage()
        Clock.schedule_once(t.oee_anzeige, 2)
        Clock.schedule_interval(t.oee_anzeige, 90)
        return t



if __name__ == "__main__":
    EpicApp().run()