from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from struct import pack
import base64
import random
import string
from cryptography.hazmat.primitives import padding
class Blow():
    BLOCK_SIZE = 32
    def __init__(self, key =None):
        if key == None:
            self.key = get_random_bytes(32)
        elif len(key)< 32:
            ad = 32 - len(key)
            key = key + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(ad))
            self.key = key.encode()
        elif len(key) == 32:
            self.key =key.encode()
        else:
            print("Chave muito longa")
            self.key = None
    def encrypt(self, mensagem):
        if self.key != None:
            #cipher = Blowfish.new(self.key,Blowfish.MODE_CBC)
            cipher = Blowfish.new(self.key,Blowfish.MODE_ECB)
            #serve para completar o bloco que vai ser cifrado
            mensagem = self.pkcs5_pad(mensagem)
            mensagem = mensagem.encode("utf-8")
            #plen  = Blowfish.block_size  - len(mensagem) % Blowfish.block_size
            #padding = [plen]*plen
            #padding = pack('b'*plen, *padding)
            #ate aqui
            #mensagem = cipher.iv + cipher.encrypt(mensagem)
            mensagem =cipher.encrypt(mensagem)
            return base64.b64encode(mensagem).decode("utf-8")
    def decrypt(self, mensagem):
        ciphertext = base64.b64decode(mensagem)
        iv = ciphertext[:Blowfish.block_size]
        #ciphertext  = ciphertext[Blowfish.block_size:]
        #cipher = Blowfish.new(self.key,Blowfish.MODE_CBC,iv)
        cipher = Blowfish.new(self.key,Blowfish.MODE_ECB)
        #mensagem = cipher.decrypt(ciphertext)
        mensagem = cipher.decrypt(ciphertext)
        mensagem = mensagem.decode()
        mensagem = self.pkcs5_unpad(mensagem)
        #last_byte = mensagem[-1]
        #mensagem = mensagem[:-(last_byte if type(last_byte) is int else ord(last_byte))]
        return mensagem
    def pkcs5_pad(self,s):
        return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)

    def pkcs5_unpad(self,s):
    
        return s[0:-ord(s[-1])]    
    
    
b = Blow("ABCDE")
textocriptografado = b.encrypt("Julio Vicente Brych")
print(textocriptografado,"\n-------------")
texto = b.decrypt(textocriptografado)
print(texto)