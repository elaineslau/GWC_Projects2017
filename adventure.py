#opening line
print ("You're home alone on a dreary Friday night when suddenly you hear hasty footsteps running through your basement.  Your parents had gone away for the weekend and there were no others that lived in the house.  You felt fear tremble through your body.  An intruder has entered your home.  What do you do now?")
leave_closet = input ("Choose: 1) leave the house or 2) hide in the closet upstairs.")

#first choice (leave)
if leave_closet == ("1"):
    print ("The intruders heard the slam of the door as you left... They begin to chase you with unidentifiable objects.  You reach a fork in the road.")

    left_right = input ("Choose: 1) go left. 2) go right.")
#go left
    if left_right == ("1"):
        print ("You turn left and continue straight down the road until you approach dead end with a fence!  You can hear the loud steps of the intruders creeping behind you.  What do you do?")

        over_under = input ("Choose: 1) climb the fence. 2) go under the fence.")
#go over (ENDING)
        if over_under == ("1"):
            print ("You climb the fence but unfortunately your shirt gets hooked onto the fence... The intruders catch up and kill you.. RIP!")
#go under (ENDING)
        elif over_under == ("2"):
            print ("Fortunately, you were small enough to fit under the fence, unlike the intruders!  You've escaped!  You go to the police station and EVERYONE LIVED HAPPILY EVER AFTER!")
#go right
    elif left_right == ("2"):
        print ("You turn right and encounter a dead end!  There are two doors to the left and right of you: a black door and a white door.")

        black_white = input ("Choose: 1) go through the black door. 2) go through the white door.")

#go through black door (ENDING)
        if black_white == ("1"):
            print ("You go through the black door!  Fortunately, this door happened to lead to the police station!  You are saved.  Good work.")

#go through white door (ENDING)
        elif black_white == ("2"):
            print ("Ah..the classic white door.  Unfotunately, there was a murderer standing behind the door!  You are dead and now an angel... RIP!")

#second choice (hide)
elif leave_closet == ("2"):
    print ("Oh no!  They heard you run up the stairs... They know someone is home...  What do you do?")

    peek_stay = input ("Choose: 1) Peek your head out to see. 2) Stay in the closet.")

#peek head out
    if peek_stay == ("1"):
        print ("The coast SEEMS to be clear... You see a phone across the room.  You know you need to contact help.  What do you do?")

        hanger_crawl = input ("Choose: 1) Grab a hanger from the closet and try to reach the phone. 2) Crawl towards the phone and pray you won't make a peep.")

#use the hanger to get phone
        if hanger_crawl == ("1"):
            print ("While grabbing the hanger, you caused other items in the closet to fall as well!  The intruders find you and kill you on the spot...  RIP!")

#crawl to get phone
        elif hanger_crawl == ("2"):
            print ("While crawling, you accidentally hit the speaker, setting off very loud music and thus revealing your location.  The intruders find you and kill you!  RIP!")

#stay in closet
    elif peek_stay == ("2"):
        print ("Wow, what a scaredy cat!  Too bad you still ended up being caught by the intruders!  RIP!")


#first
else:
    print ("Enter 1 or 2 please.")
