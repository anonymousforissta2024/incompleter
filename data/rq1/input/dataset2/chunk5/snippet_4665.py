#Source: https://stackoverflow.com/questions/41475703/beautiful-soup-attributeerror-nonetype-object-has-no-attribute-find
url = "https://www.smith.edu/diningservices/menu_poc/cbord_menus.php"
response = requests.get(url)
bsObj = BeautifulSoup(response.content, "html.parser")