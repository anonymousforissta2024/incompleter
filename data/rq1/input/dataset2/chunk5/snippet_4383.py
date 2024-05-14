#Source: https://stackoverflow.com/questions/46923475/attributeerror-str-object-has-no-attribute-text-printing-css-error
team_name = section.find_element_by_css_selector(".row:nth-child(1) td:nth-child(1)").text
print(team_name.text)