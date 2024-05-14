#Source: https://stackoverflow.com/questions/75641055/typeerror-argument-of-type-bool-is-not-iterable-when-practicing-list-comprehe
lista = ["Hello", "And", "Goodbye"]

uppgift = [s + "..." for s in lista if (s.lower() in lista.__contains__("h") or s.lower() in lista.__contains__(
    "o") or s.lower() in lista.__contains__("a"))]

print(uppgift)