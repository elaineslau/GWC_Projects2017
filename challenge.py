############################################
# Programming Challenge 1
# Python: Variables, Conditionals, & Loops
############################################
# 1
# print "Welcome to my world!"
print ("Welcome to my world!")

# 2
# print "hey!" 7 times using a for loop
for counter in range (7):
	print ("hey!")

# 3
# print the numbers 1-10 using a for loop 
for i in range(1, 11):
    print(i)

# 4
# print the odd numbers between 20 and 30 using a while loop
x = 29
while x>20:
	print (x) 
	x-=2

# 5
# write a function that subtracts two numbers (and call the function to test it) 
def subtract(a, b):
	return a-b

ans = subtract(8,3)
print(ans)


# 6
# # print all the multiples of 3 between 2 and 34 using a loop
y = 3
while y<34:
	print (y)
	y+=3

# # 7
# # print the numbers 2-8 in order, ten times using two for loops
for i in range(10):
	for j in range(7):
		print(j+2)

# # 8
# # write a function that takes in parameters 
def my_function(a, b):
	return (a*a)-(b*b) # difference of squares

ans = my_function(5, 4)
print(ans)


# # 9
# # print a list of all the numbers that are divisible by 7 that are between 22 and 62
i = 22
while i<62:
	if i%7 == 0:
		print(i)
	i += 1

# # 10
for i in range(14):
	my_str = "yo"
	for j in range(i):
		my_str = my_str + "o"
	print(my_str)


def wee(numba):
	if numba % 5 == 0:
		print ("It's a multiple of 5!")		
	else:
		print ("It's not a multiple of 5!")

wee(10)
