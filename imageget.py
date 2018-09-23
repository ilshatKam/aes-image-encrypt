from PIL import Image
import test_image
import aes_new
#encr params
# A 256 bit (32 byte) key
key = bytes("This_key_for_demo_purposes_only!", 'utf-8') 

# For some modes of operation we need a random initialization vector
# of 16 bytes
iv = "InitializationVe"
print('len ',len(key))
aes = aes_new.AESModeOfOperationECB(key)

#image
in_img = Image.open("E:\Work\Report\Python\ilshat\kot.bmp")

in_arr=list(in_img.getdata())
#print(in_arr)

out_arr = test_image.encrypt(in_arr, key, aes, iv)
print(out_arr)
out_img = Image.new(in_img.mode, in_img.size)
out_img.putdata(out_arr)
out_img.save('kot_out.bmp')
out_img.show()