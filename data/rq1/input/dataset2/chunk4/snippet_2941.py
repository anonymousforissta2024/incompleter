#Source: https://stackoverflow.com/questions/71067529/beautiful-soup-attributeerror-nonetype-object-has-no-attribute-get-text
location = t.find('span', itemprop='name').get_text()