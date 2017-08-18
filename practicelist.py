#importting random library
import random

#my 3 different lists
sides = ["fries","hash browns","mashed potatoes","sweet potato fries","baked potato","salad"]
main_courses = ["grilled chicken sandwich","shrimp scampi","pizza","steak","pasta","ribs"]
desserts = ["ice cream","chocolate cake","banana split","brownie sundae","panna cotta","fried ice cream"]

#randomizer for sides
random_index = random.randint (0, len(sides)-1)
print (random_index)
print (sides[random_index])

#randomizer for main_courses
random_index2 = random.randint (0, len(main_courses)-1)
print (random_index2)
print (main_courses[random_index2])

#randomizer for desserts
random_index3 = random.randint (0, len(desserts)-1)
print (random_index3)
print (desserts[random_index3])
