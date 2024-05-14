#Source: https://stackoverflow.com/questions/56842427/python-robobrowser-typeerror-nonetype
import re
import config
from robobrowser import RoboBrowser
br = RoboBrowser(history=True)

br.open("https://www.tessco.com/login")
form = br.get_form()
form['userID'] = config.TESSCO_USERNAME
form['password'] = config.TESSCO_PASSWORD
br.submit_form(form)