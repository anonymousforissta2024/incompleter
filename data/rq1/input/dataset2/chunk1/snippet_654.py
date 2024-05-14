#Source: https://stackoverflow.com/questions/55679929/how-to-fix-attributeerror-dict-object-has-no-attribute-error-in-python
import requests
import pprint

URL = 'https://github.com/timeline.json'

def get_github_json(URL):
    response = requests.get(URL).json()
    return response

assert get_github_json(URL).documentation_url == 'https://developer.github.com/v3/activity/events/#list-public-events'