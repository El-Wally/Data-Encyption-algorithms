import math
from math_ import *

class rsa:
    def __init__(self, p, q, e):     
        # RSA Modulus
        n = p * q

        # Eulers Toitent
        r = (p-1)*(q-1)
        
        # d, Private and Public Keys
        d = mulInv(e, r)
        self.publicKey = (e, n)
        self.privateKey = (d, n)

    def getPublicKey(self):
        return self.publicKey

    def getPrivateKey(self):
        return self.privateKey

    def encrypt(self, publicKey, plainText):
        e, n = publicKey
        x=[]
        m=0
        for i in plainText:
            if(i.isspace()):
                spc=400
                x.append(400)
            elif(i.isupper()):
                m = ord(i) # ascii equivalent
                #c=(m**e)%n
                c = squareMultiply(m, e, n)
                x.append(c)
            
        return x

    def decrypt(self, privateKey, cipherText):
        d, n = privateKey
        text = cipherText.split(',')
        x = ''
        m = None
        for i in text:
            if (i == '400'):
                x+=' '
            else:
                #m=(int(i)**d)%n
                m = squareMultiply(int(i), d, n)
                c=chr(m)
                x+=c
        return x