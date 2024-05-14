#Source: https://stackoverflow.com/questions/42019886/python-3-mechanical-soup-typeerror-nonetype-object-is-not-callable
browser = mechanicalsoup.Browser()

# Request page
login_page = browser.get("https://www.website.com/login")

login_form = login_page.soup.find("form", {"id":"login"})

# specify username and password
login_form.find("input", {"id": "username"})["value"] = 'myUsername'
login_form.find("input", {"id": "password"})["value"] = 'myPassword'

# submit form
response = browser.submit(login_form, login_page.url)