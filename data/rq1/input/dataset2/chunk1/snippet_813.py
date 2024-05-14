#Source: https://stackoverflow.com/questions/56931505/python3-slicing-typeerror-list-indices-must-be-integers-or-slices-not-list
# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
print(data["people"][0:2]["name"])