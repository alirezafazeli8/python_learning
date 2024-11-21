# Pillow Python Library

pillow is python image processing library

- image.format : shows the image format
- image.size : shows the image size
- image.mode : how made it this image ? with 'rgb' or 'cmyk'
- image.fp : this is shows the file path
- image.save("file name", "file format")
- my_image.rotate(10)
- my_image.resize((50, 50))
- my_image.crop((100, 100, 300, 300))
- my_image.size : show the pixel size of image
- my_image.thumbnail(400, 400) : ما به این ابعاد تصویرو میدیم و این برای ما به نسبت تصویر پیکسل قبلی نسبت تصویر مارو تغییر میده پس در نتیجه به کل نسبت تصویر ما آسیب نمیرسه. این متود برای ساخت عکس پروفایل کاربر خیلی کاربرد داره.

## ImageFilter module from Pillow : 
- ImageFilter.BLUR
- ImageFilter.SMOOTH
- ImageFilter.SHARPEN