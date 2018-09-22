from PIL import Image
im = Image.open("E:\Work\Report\Python\ilshat\honda.jpg")
im.show()

print(list(im.getdata()))