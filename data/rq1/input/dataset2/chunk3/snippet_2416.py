#Source: https://stackoverflow.com/questions/76101117/attributeerror-module-prtscnr-has-no-attribute-portscanner
import prtscnr

def menu():
    print("****** Recon ******")
    print("1- PortScanner")
    print("2- Subdomain Finder")
    print("3- Hash Decryption ")
    print("4- Çıkış ")
    msecim = int(input("Seçimini yap: "))
    if msecim == 1 :
        print("Portscanner'a hoşgeldin...")
        prtscnr.portscanner()