import base64
from Crypto.Cipher import AES
import binascii

key = b'ABCDEFGHIJKLMNOP'
ent = open(r"C:\temp\a.txt","rb")
a = ent.read()
des = ""
for i in a:
    des += (str(i))
print(des)
decipher = AES.new(key, AES.MODE_ECB)
msg_dec = decipher.decrypt(a)
print(msg_dec)
#saida = cipher.decrypt(a)