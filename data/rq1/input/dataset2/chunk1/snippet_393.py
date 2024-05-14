#Source: https://stackoverflow.com/questions/48997007/check-for-string-in-response-content-raising-typeerror-a-bytes-like-object-i
import requests

r = requests.get('https://www.eventbrite.co.uk/o/piers-test-16613670281')
text = 'Sorry, there are no upcoming events'

if text in r.content: 
   print('No Upcoming Events')