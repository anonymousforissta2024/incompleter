#Source: https://stackoverflow.com/questions/58812320/attributeerror-str-object-has-no-attribute-title
first="harry"
last="potter"

print(first, first.title())
print(f"Full name: {first.title()} {last.title()}")
print("Full name: {0.title()} {1.title()}".format(first, last))