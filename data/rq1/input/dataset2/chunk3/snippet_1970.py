#Source: https://stackoverflow.com/questions/72495771/attributeerror-module-wsgi-has-no-attribute-application
import webbrowser
import time

#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/quote/AAPL,FB?apikey=d099f1f81bf9a62d0f16b90c3dc3f718")
print(get_jsonparsed_data(url))

country = get_jsonparsed_data(url)
count = 0
for result in country:
    if count == 0:
        header = result.keys()
        for head in header:
            html_content = f"<div> {head} </div>"
        count += 1


with open("index.html", "w") as html_file:
    html_file.write(html_content)
    print("Html file created successfully !!")

    time.sleep(2)
    webbrowser.open_new_tab("index.html")