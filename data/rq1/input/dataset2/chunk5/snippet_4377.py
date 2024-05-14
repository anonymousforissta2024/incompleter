#Source: https://stackoverflow.com/questions/62287823/attributeerror-response-object-has-no-attribute-read-uses-requsts-and-json
import requests as req
import json
Bin = int(300000)
BinMax = int(600000)
File = open("C:/Users/admin/Desktop/PS Now Generaetors/Bins.txt", 'a')

while Bin != BinMax:
    json1 = req.get("https://lookup.binlist.net/" + str(Bin))
    json2 = json1.text
    jsonout = json.loads(json2)
    country = jsonout["country"]
    cc = country["alpha2"]
    if "US" or "AT" or "BE" or "CA" or "FR" or "De" or "IE" or "JP" or "LU" or "NL" or "CH" or "GB" or "ES" or "IT" or "PT" or "NO" or "DK" or "FI" or "SE" or "PH" == cc:
        print (bin, "writed")
        File.write("\n" + str(Bin) + ";" + cc)
    Bin =+ 1