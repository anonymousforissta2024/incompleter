#Source: https://stackoverflow.com/questions/67064352/my-data-from-script-returns-none-attributeerror-nonetype-object-has-no-att
html_doc = """
    <script>
      var modelData = {
        "hlsUrl": "null",
        "account": "4LH7J44IYPAGEZEY6E3UL"
      }
  </script>
"""

soup = BeautifulSoup(html_doc, "html.parser")
# locate the script, get the contents
script_text = soup.select_one("script").contents[0]

# get javascript object inside the script
model_data = re.search(r"modelData = ({.*?});", script_text, flags=re.S)
print(model_data) # RETURNS None - why?
model_data = model_data.group(1)

# "convert" the javascript object to json-valid object
model_data = re.sub(
    r"^\s*([^:\s]+):", r'"\1":', model_data.replace("'", '"'), flags=re.M
)

# json decode the object
model_data = json.loads(model_data)

# print the data
print(model_data["account"])