from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
privateKey = key.exportKey('PEM')
publicKey = key.publickey().exportKey('PEM')

message = input("what is the top secret message?" )
message = str.encode(message)

RSApublicKey = RSA.importKey(publicKey)
OAEP_cipher = PKCS1_OAEP.new(RSApublicKey)
encryptedMsg = OAEP_cipher.encrypt(message)

print('Encrypted text:', encryptedMsg)

RSAprivateKey = RSA.importKey(privateKey)
OAEP_cipher = PKCS1_OAEP.new(RSAprivateKey)
decryptedMsg = OAEP_cipher.decrypt(encryptedMsg)

print('The original text:', decryptedMsg)