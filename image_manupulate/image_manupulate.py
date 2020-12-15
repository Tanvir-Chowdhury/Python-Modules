from PIL import Image, ImageFilter
import glob, os

os.chdir('/home/codinxter/Desktop/Python_Projects/Python_modules/Python-Modules/image_manupulate')

image1 = Image.open("sample.jpg")
image1.show()   #It opens the picture to show
image1.rotate(90).save("sample90.png") #rotates the image
image1.convert(mode= "L").save("sample_black_and_white.jpg") # turns an colorful image into black and white
image1.filter(ImageFilter.GaussianBlur(15)).save("sample_blur.png") # makes an image blurry

image1.save("sample.png") # It saves the image into png format
size = (300, 400)
#translating all jpg in png

for file in glob.glob("*.jpg"):
    print(file)
    file_name, file_ext = file.split('.')
    image1 = Image.open(file)
    image1.thumbnail(size)    # resizes an image.
    image1.save(f"{file_name}_300x400.png")


#translating all jpg in png 2
for f in os.listdir('.'):
    if f.endswith(".png"):
        i = Image.open(f)