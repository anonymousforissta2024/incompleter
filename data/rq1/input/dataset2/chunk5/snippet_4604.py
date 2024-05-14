#Source: https://stackoverflow.com/questions/54480471/attributeerror-float-object-has-no-attribute-apply
products['sentiment'] = products['rating'].apply(lambda rating : +1 if rating > 3 else -1)