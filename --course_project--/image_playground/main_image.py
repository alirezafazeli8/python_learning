from PIL import Image, ImageFilter

# my_image = Image.open("./pokemon_image/004 pikachu.jpg")
# # my_image.show()
# print(my_image.format)
# print(my_image.mode)
# print(my_image.fp.name)
# filtered_image = my_image.filter(ImageFilter.BLUR)
# filtered_image = my_image.filter(ImageFilter.SMOOTH_MORE)
# filtered_image = my_image.filter(ImageFilter.SHARPEN)
# filtered_image = my_image.convert('L')
# rgb_image = my_image.convert('RGB')
# rgba_image = my_image.convert('RGBA')
#
# rgb_image.show()
# rgba_image.show()

# filtered_image.save("new.png", "png")
# rotate_image = my_image.rotate(10)
#
# rotate_image.save("rotate.png", 'png')

# resize_image = my_image.resize((50, 50))
# resize_image.save("resize_image.png", "png")

# crop_image = my_image.crop((100, 100, 300, 300))
# crop_image.save("crop_image.png", "png")


# resize astro image
my_image = Image.open("./006 astro.jpg")
# resize_image = my_image.resize((400, 400))
# resize_image.save("resize_astro.png", "png")
# my_image.thumbnail((5000, 5000))
# my_image.save("thumbnail.png", "png")
print(my_image.size)
my_image.thumbnail((400, 400))
my_image.save("resize_astro.png", "png")
print(my_image.size)
