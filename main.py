from rsa import rsa
from playfair import playfair

#####
# rsa

p = 17
q = 11
e = 7
message = 'XX' #88 ascii
#message_binary = 88

ob = rsa(p, q, e)

publicKey = ob.getPublicKey()
privateKey = ob.getPrivateKey()

cipherText = ob.encrypt(publicKey, message)

plainText = ""
for cipherChunck in cipherText:
    plainText = plainText + ob.decrypt(privateKey, str(cipherChunck))

print("original message:", message, "\ncipher text:", cipherText, "\ndecrypt:", plainText)

#####
# playfair

plainText = "Modasa"
cipherText = "GTBFQY"
key = "playfair"

ob = playfair(key)

print("cipher text : "+ob.encode(plainText))
print("plain text : "+ob.decode(cipherText))