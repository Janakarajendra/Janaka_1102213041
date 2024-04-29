from PIL import Image, ImageEnhance

file = "lena.png"
img = Image.open(file)

img1 = img.convert("L")
img.show()

img2 = img.convert("LA")
img2.show()