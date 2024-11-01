from PIL import Image, ImageFilter

my_img = Image.open("./pokemon_image/004 squirtle.jpg")

# my_img.show()
# print(my_img.format)
# print(my_img.mode)
# print(dir(my_img))
# print(my_img.fp)
# filtered_img = my_img.filter(ImageFilter.BLUR)
# filtered_img = my_img.filter(ImageFilter.SMOOTH)
# filtered_img = my_img.filter(ImageFilter.SHARPEN)
# filtered_img.show()

# filtered_img = my_img.filter(ImageFilter.SHARPEN)
filtered_img = my_img.convert("L")
blured = filtered_img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", "png")
blured.save("blur.png", "png")
