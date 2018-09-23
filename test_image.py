import aes_new
import os
import sys
def encrypt_img(input, key, aes, iv, mode):
    #input = [255, 255, 255, 255, 5, 6, 7, 7, 7, 7, 11, 12, 13, 254, 15, 240]
    if mode == 'ECB' or mode == 'CBC':
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
           # decrypted = [aes.decrypt(ciphertext(i))]
        return ciphertext_arr
    elif mode == 'CFB' or 'OFB' or 'CTR':
        ciphertext = list(aes.encrypt(input))
        return ciphertext
# Since there is no state stored in this mode of operation, it
# is not necessary to create a new aes object for decryption.
#aes = pyaes.AESModeOfOperationECB(key)
    

# True
#    print ('decrypted ', decrypted)
#    print (decrypted == plaintext)