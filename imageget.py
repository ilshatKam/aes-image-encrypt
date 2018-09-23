from PIL import Image
import test_image
import aes_new

#encr params
# A 256 bit (32 byte) key
key = bytes("This_key_for_demo_purposes_only!", 'utf-8') 
iv = "InitializationVe"
mode = 'CTR'
#aes = aes_new.AESModeOfOperationECB(key)
#aes = aes_new.AESModeOfOperationCBC(key, iv = iv)
#aes = aes_new.AESModeOfOperationCFB(key, iv = iv, segment_size = 8)
#aes = aes_new.AESModeOfOperationOFB(key, iv = iv)
counter = aes_new.Counter(initial_value = 100)
aes = aes_new.AESModeOfOperationCTR_fast(key, counter = counter)

#image
in_img = Image.open("E:\Work\Report\Python\ilshat\kot.bmp")
in_arr=list(in_img.getdata())
#print(in_arr)
out_arr = test_image.encrypt_img(in_arr, key, aes, iv, mode)
#print(out_arr)
out_img = Image.new(in_img.mode, in_img.size)
out_img.putdata(out_arr)
out_img.save('kot_out.bmp')
out_img.show()