#Source: https://stackoverflow.com/questions/46520034/attributeerror-function-object-has-no-attribute-method-for-if-request-metho
from __future__ import print_function
from flask import Flask, render_template, flash, request, url_for, redirect, session, g
import controllers
import config
from functools import wraps
import argparse
import json
import pprint
import requests
import sys
import urllib

# this client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

@app.route('/',  methods=["GET","POST"])
def main_route():
    if request.method == "POST":
        input_place = request.form['location']
        input_type = request.form['type']
        return render_template('index.html')
    return render_template('index.html')