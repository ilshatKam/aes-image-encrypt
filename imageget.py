from PIL import Image
import test_image
in_img = Image.open("E:\Work\Report\Python\ilshat\kot.bmp")

in_arr=list(in_img.getdata())
#print(in_arr)

out_arr = test_image.encrypt(in_arr)
print(out_arr)
out_img = Image.new(in_img.mode, in_img.size)
out_img.putdata(out_arr)
out_img.save('kot_out.bmp')
out_img.show()