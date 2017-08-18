from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
my_image = Image.open("pictureofme.jpg")
image_list = my_image.getdata()
image_list = list(image_list)

recolored = []
#list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.



for color in image_list:
    intensity = color[0] + color[1] + color[2]
    color = (0,0,0)
    if intensity < 182:
        color = darkBlue
    elif intensity > 182 and intensity < 364:
        color = red
    elif intensity > 364 and intensity < 546:
        color = lightBlue
    else:
        color = yellow

    recolored.append(color)

# # Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size)
# #Creates a new image that will be the same size as the original image.

new_image.putdata(recolored)
# #Adds the data from the recolored list to the image.

new_image.show()
# #show the new image on the screen

new_image.save("recolored.jpg", "jpeg")
# #save the new image as "recolored.jpg"
