############################################
# Programming Challenge 4
# Python: Variables, Conditionals, Loops, & Functions
############################################

# 1
# write a function that takes a word as a parameter and returns a scrambled version of the word 
# import random
# user_input = input ("Choose a word!")
# def scrambled (user_input):
# 	random_index = random.randint (0, len(user_input)-1)
# 	print (user_input[random_index])
# scrambled (user_input)

# def shuffle_word(word):
# 	word = list(word)
# 	shuffle(word)
# 	return ''.join(word)
# def mixup(word):
# 	as_list_of_letters = list(word)
# 	random.shuffle(as_list_of_letters)
# 	return ''.join(as_list_of_letters)

# sentence = input ("Choose a word!")
# def scrambler(sentence):
# 	split = sentence.split()
# 	shuffle(split)
# 	return ' '.join(split)
# 	print (scrambler(sentence))

# word = input ("Choose a word!")
# def scrambled (shuffled):
# 	shuffled = ''.join(random.sample(word, len(word)))
# 	return word
# 	print (scrambled (shuffled))
# 	scrambled (shuffled)

from random import randint
word = input ("Choose a word!")

def shuffle(word):
    wordlen = len(word)
    word = list(word)
    for i in range(0,wordlen-1):
        pos = randint(i+1,wordlen-1)
        word[i], word[pos] = word[pos], word[i]
    word = "".join(word)
    return word

print (shuffle(word)) 


# 2
# write a function that takes in a word and returns an 'encrypted' version by increasing each letter by 2 (e.g. 'a' becomes 'c', 'f' becomes 'h', etc.)
alphabet ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encrypted_version (alphabet):



# 3
# write a function that decodes the 'encrypted' version of the word into its original form (the opposite fo the above challenge problem) 



# 4
# write a function that takes in a list of integers and a number called 'num',  adds 'num' to each of the elements of the list, and returns the new version of the list
