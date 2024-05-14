#Source: https://stackoverflow.com/questions/74599866/typeerror-argument-of-type-mx-is-not-iterable
import dns.resolver
answer=dns.resolver.resolve("google.com", "MX")
for data in answer:
    print (data)
    if "smtp.google.com" in data:
      print("cool")