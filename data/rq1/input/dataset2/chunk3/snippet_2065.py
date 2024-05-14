#Source: https://stackoverflow.com/questions/55212109/receiving-a-typeerror-in-trying-to-create-a-new-aes-cipher-in-python3
iv = 0x0008739a3043314e614c4b764f234189
key = 0xf188c2f6176502368ab346a0b40f1098ed350c3c46595e998147ab1db9d865b7
cipher = AES.new(key, AES.MODE_CBC, iv)