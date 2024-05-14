#Source: https://stackoverflow.com/questions/62285920/python-error-attributeerror-str-object-has-no-attribute-read
import requests as req
import json
Bin = int(300000)
BinMax = int(600000)
File = open("C:/Users/admin/Desktop/PS Now Generaetors/Bins.txt", 'a')

while bin != BinMax:
    json1 = req.get("https://lookup.binlist.net/" + str(Bin))
    json2 = json1.text
    jsonout = json.load(json2)
    country = jsonout["country"]
    cc = country["alpha2"]
    if cc == "US" or "AT" or "BE" or "CA" or "FR" or "De" or "IE" or "JP" or "LU" or "NL" or "CH" or "GB" or "ES" or "IT" or "PT" or "NO" or "DK" or "FI" or "SE" or "PH":
        print (bin, "writed")
        File.write("\n" + str(Bin) + ";" + cc)
    bin =+ 1