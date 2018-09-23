import aes_new
import os
import sys
def encrypt(input, key, aes, iv):
    #input = [255, 255, 255, 255, 5, 6, 7, 7, 7, 7, 11, 12, 13, 254, 15, 240]
    plaintext = [0, 0, 0, 0]
    i = 0
    max = (len(input)//16)
    ciphertext_arr = [ ]
    for i in range(0, max):
        plaintext[0] = (input[16*i] << 24) | (input[16*i+1] << 16) | (input[16*i+2] << 8) | input[16*i+3]
        for j in range(1, 4): 
            plaintext[j] = (input[4*j+16*i] << 24) | (input[4*j+16*i+1] << 16) | (input[4*j+16*i+2] << 8) | input[4*j+16*i+3]
        ciphertext = aes.encrypt(plaintext)
        for m in range(0, 16):
        	ciphertext_arr.append(ciphertext[m])
        #ciphertext_arr = [ struct.unpack('>i', ciphertext[i:i + 4])[0] for i in xrange(0, len(key), 4) ]
        print('len ciphertext', len(ciphertext))
       # decrypted = [aes.decrypt(ciphertext(i))]
    return ciphertext_arr
    
# 'L6\x95\x85\xe4\xd9\xf1\x8a\xfb\xe5\x94X\x80|\x19\xc3'
    print (repr(ciphertext))

# Since there is no state stored in this mode of operation, it
# is not necessary to create a new aes object for decryption.
#aes = pyaes.AESModeOfOperationECB(key)
    

# True
    print ('decrypted ', decrypted)
    print (decrypted == plaintext)