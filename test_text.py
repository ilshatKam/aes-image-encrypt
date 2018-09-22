import pyaes
import os
import sys

# A 256 bit (32 byte) key
key = bytes("This_key_for_demo_purposes_only!", 'utf-8') 

# For some modes of operation we need a random initialization vector
# of 16 bytes
iv = "InitializationVe"
print('len ',len(key))
aes = pyaes.AESModeOfOperationECB(key)
plaintext = "TextMustBe16Byte"

ciphertext = aes.encrypt(plaintext)

# 'L6\x95\x85\xe4\xd9\xf1\x8a\xfb\xe5\x94X\x80|\x19\xc3'
print (repr(ciphertext))

# Since there is no state stored in this mode of operation, it
# is not necessary to create a new aes object for decryption.
#aes = pyaes.AESModeOfOperationECB(key)
decrypted = aes.decrypt(ciphertext)

# True
print ('decrypted ', decrypted)
print (decrypted == plaintext)