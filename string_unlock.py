#unlock string    str = *****  entered : s
#                str = s****

import random
random_word  = ["sky" , "cloud","blue" , "bird" , "open"]
#random word picked for unlock string 

pick = random.choice(random_word)
string = "*" * len(pick)
count = 0
print(f"Guess the {len(string)} word unlock string : {string}")
while count != 3:
    if string == pick:
        print("Congratulations dear !")
        break
    letter = input("Enter  a  Guess Letter : ")
    if letter in pick:
        print("Good Guess !")
        ind = pick.index(letter)
        string = string[:ind] + letter + string[ind+1:]
        print(f"unlock string --> {string}")
    else:
        print("Not in Guess String !")
        count += 1
         
           
