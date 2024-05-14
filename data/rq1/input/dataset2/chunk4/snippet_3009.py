#Source: https://stackoverflow.com/questions/70727382/how-would-i-fix-the-attribute-error-bytes-object-has-no-attribute-encode-d
z = (priv.to_string().encode('hex'))
url = ("https://etherscan.io/address/%s"%address)

html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
soup = BeautifulSoup(html, "html.parser")
table = soup.find("div", {"class": "col-md-6"})
value = table.findAll('td')[1].text.split(' ')[0].strip()


dosya3 = open("eth-adresler.txt", "a")
dosya3.write(str(i)+" "+"PRV Key = "+z+"  ADR = 0x"+address+" "+str(value) + "\n")
time.sleep(0.2)


tp = 1+float(value)
if tp > 1:
    print("--------------------")
    print("-----BULUNDU--------")
    print("Private Key     = "+z)
    print("Adres           = 0x"+address)
    print("Ether Miktar    = "+str(value))
    print("--------------------")

    dosya4=open("BULUNAN.txt","a")
    dosya4.write(z+" "+"0x"+address+" "+str(value)+ "\n")
    dosya4.close()
else:
    print (str(i) + " " + "private key = " + z + " " + "Adress = 0x" + address + "  " + str(value))

i = i + 1