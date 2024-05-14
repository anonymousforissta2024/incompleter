#Source: https://stackoverflow.com/questions/74188784/attributeerror-nonetype-object-has-no-attribute-get-text-in-the-line-9
soup = BeautifulSoup(page, "html.parser")
soup_title = soup.find(name="a", class_="spacer")
print(soup_title.get_text())