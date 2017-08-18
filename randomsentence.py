#importting random library
import random

#the different lists
noun = ["He","The cat","The ugly man","I","We","The CEO of AIG","New Yorkers","The student","The teacher","The panda","The lion"]
verb = ["ran","fell","tumbled","bawled","bounced", "flapped","licked"]
adjective = ["quickly","slowly","stupidly","abruptly","cheerfully","sadly","loudly","gently","annually","willingly"]
location = ["in the volcano","in the building","on the floor","at home","on the street","on top of the bear","in the grass","in the police station"]
conjunction = ["because","yet","but","and","yet","for","however",]
random_sentence = ["the dog was ugly.","his girlfriend left him on seen.","his friend wouldn't send him her location", "the sandwich had mayo.","the school was on fire.","it was raining hot dogs.","the murderer had a knife.","I licked my elbow.","the sky turned black from being too polluted.","the old lady wouldn't shower for a year!",]

#randomizer for noun
random_index = random.randint (0, len(noun)-1)
#print (random_index)
print (noun[random_index])

#randomizer for verb
random_index2 = random.randint (0, len(verb)-1)
#print (random_index2)
print (verb[random_index2])

#randomizer for adjective
random_index3 = random.randint (0, len(adjective)-1)
#print (random_index3)
print (adjective[random_index3])

#randomizer for location
random_index6 = random.randint (0, len(location)-1)
#print (random_index6)
print (location[random_index6])

#randomizer for conjunction
random_index4 = random.randint (0, len(conjunction)-1)
#print (random_index4)
print (conjunction[random_index4])

#randomizer for random_sentence
random_index5 = random.randint (0, len(random_sentence)-1)
#print (random_index5)
print (random_sentence[random_index5])
