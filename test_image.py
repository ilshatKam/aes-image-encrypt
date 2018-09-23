import aes_new
import os
import sys
def encrypt(input, key, aes, iv):
    #input = [255, 255, 255, 255, 5, 6, 7, 7, 7, 7, 11, 12, 13, 254, 15, 240]
#333    plaintext = [0, 0, 0, 0]
#333    i = 0
#333    max = (len(input)//16)
#333    ciphertext_arr = [ ]
#333    for i in range(0, max):
#333        plaintext[0] = (input[16*i] << 24) | (input[16*i+1] << 16) | (input[16*i+2] << 8) | input[16*i+3]
#333        for j in range(1, 4): 
#333            plaintext[j] = (input[4*j+16*i] << 24) | (input[4*j+16*i+1] << 16) | (input[4*j+16*i+2] << 8) | input[4*j+16*i+3]
#333        ciphertext = aes.encrypt(plaintext)
#333        for m in range(0, 16):
#333        	ciphertext_arr.append(ciphertext[m])
#333        #ciphertext_arr = [ struct.unpack('>i', ciphertext[i:i + 4])[0] for i in xrange(0, len(key), 4) ]
#333        print('len ciphertext', len(ciphertext))
#333       # decrypted = [aes.decrypt(ciphertext(i))]
#333    return ciphertext_arr
    ciphertext = list(aes.encrypt(input))
# 'L6\x95\x85\xe4\xd9\xf1\x8a\xfb\xe5\x94X\x80|\x19\xc3'
    print (repr(ciphertext))
    return ciphertext
# Since there is no state stored in this mode of operation, it
# is not necessary to create a new aes object for decryption.
#aes = pyaes.AESModeOfOperationECB(key)
    

# True
#    print ('decrypted ', decrypted)
#    print (decrypted == plaintext)