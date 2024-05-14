#Source: https://stackoverflow.com/questions/74181540/typeerror-argument-should-be-a-bytes-like-object-or-ascii-string-not-buffered
import PGL
from cryptography.fernet import Fernet as Fn
class APM():
    class database():
        def genkey():
            keyfile = open("D:\\CODING\\Python\\APMKEY.APMKEY", "wb")
            key = Fn.generate_key()
            keyfile.write(key)
        def encrypt(self):
            key = open("D:\\CODING\\Python\\APMKEY.APMKEY", "rb")
            database = open("D:\\CODING\\Python\\APMDatabase.APMDATA", "w")

            newdata = Fn(key).encrypt(database.encode())
            database.write(newdata)
        def decrypt(self):
            key = open("D:\\CODING\\Python\\APMKEY.APMKEY", "rb")
            database = open("D:\\CODING\\Python\\APMDatabase.APMDATA", "w")

            newdata = Fn(key).decrypt(database)
            database.write(newdata)
        def access(self):
            database = open("D:\\CODING\\Python\\APMDatabase.APMDATA", "r")
            content = database.readlines()
            print(content)
        def write(self):
            database = open("D:\\CODING\\Python\\APMDatabase.APMDATA", "a")
            database.write("\"NAME OF SITE\", \"WEBSITE URL\", \"USERNAME\", \"PASSWORD\", \"XTRA INFO\"\n")
        def reencrypt():
            key = Fn.generate_key()
            keyfile = open("D:\\CODING\\Python\\APMKEY.APMKEY", "r")
            oldkey = keyfile.read()
            keyfile.close()
            keyfile = open("D:\\CODING\\Python\\APMKEY.APMKEY", "w")
            keyfile.write(key)
            APM.database.decrypt(oldkey)
            APM.database.encrypt(key)



    class gen():
        def password():
            PGL.gen.password()
        def username():
            PGL.gen.username()

APM.database.encrypt("a")