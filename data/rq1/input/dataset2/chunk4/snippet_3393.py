#Source: https://stackoverflow.com/questions/68025435/attributeerror-io-textiowrapper-object-has-no-attribute-fp
import os
import subprocess
import requests
import discord
import dhooks
from dhooks import Webhook, Embed

hook = Webhook("hook")
Discord_txt = open("data.txt", "r+")
hook.send(file=Discord_txt)