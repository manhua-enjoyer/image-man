from PIL import Image
import os
from PIL import Image, ImageFilter
from PIL import ImageEnhance



def image_manip():
    while True: 
        user_choice = input("Choose an image from pic1-pic10: ")
        usershow = Image.open(user_choice + ".jpg")
        usershow.show()
        user_confirmation = input("This the right image? yes/no: ")
        if user_confirmation == "yes":
            break

    choice = input("what kind of changes would you like to make?: resize, png, black/white(bw), rotate or blur?: ")


    if choice =="rorate":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.rotate(90).save('rotate/' + user_choice + '_rotate.jpg')
        pic2 = Image.open('rotate/' + user_choice + '_rotate.jpg')
        pic2.show()

    if choice =="blur":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.show()
        pic2 = pic1.filter(ImageFilter.BLUR)
        pic2.show()
        pic2.save('blur/' + user_choice + '_blur.jpg')
        
    if choice =="bw":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.save('bw/' + user_choice + '_bw.jpg')
        pic2 = pic1.convert('L')
        pic2.show()
        
    if choice =="resize":
        newsize = (300, 300)
        pic1 = Image.open(user_choice + ".jpg")
        pic2 = pic1.resize(newsize)
        pic2.show()
        
    if choice =="png":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.save('png/' + user_choice + '_png.png')
        pic1.show()
        
image_manip()
second_round = input("Would you like to manipulate another image? y/n: ")
if second_round == "y":
    image_manip()
else:
    print("Have a great day")
    





