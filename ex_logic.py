"""with conditions only"""

"""
rainy = input("Is it rainy? (y/n):\n")
if rainy == "y" :
    power = input("You should stay indoor. Is there power? (y/n):\n")
    if power == "y" :
        print("Have fun with Netflix")
    elif power == "n" :
        print("Just rad a novel")
    else :
        while (power != "y" and power != "n") :
            input("Command not found.\nIs there power? (y/n)\n")
elif rainy == "n" :
    temp = input("You should go out. Is it too hot (y/n):\n")
    if temp == "y" :
        print("Visit the mall")
    elif temp == "n" :
        print("Visit the garden")
    else :
        while (temp != "y" and temp != "n") :
            input("Command not found.\nIs it too hot? (y/n):\n")
else :
    while (rainy != "y" and rainy != "n") :
        input("Command not found.\nIs it rainy? (y/n):\n")

"""

"""With logic operators"""

# """
question_rainy = input("Is it rainy? (y/n):\n")
while ( question_rainy not in ['y','n']) :
        question_rainy = input("Command not found.\nIs it rainy? (y/n):\n")
if question_rainy == "y" :
    rainy = True
elif question_rainy == "n" :
    rainy = False 

if rainy == True :
    question_power = input("Is there power? (y/n):\n")
    while (question_power != "y" and question_power != "n") :
        question_power = input("Command not found.\nIs there power? (y/n):\n")
    if question_power == "y" :
        power = True
    elif question_power == "n" :
        power = False 
else :
    question_temp = input("Is it too hot? (y/n):\n")
    while (question_temp != "y" and question_temp != "n") :
        question_temp = input("Command not found.\nIs it too hot? (y/n):\n")
    if question_temp == "y" :
        temp = True
    elif question_temp == "n" :
        temp = False
if (rainy and power) :
    print("Stay indoor and watch Netflix")
elif (rainy and power == False) :
    print("Stay indoor and read a novel")
elif (rainy == False and temp) :
    print("Go out and visit the mall")
elif (rainy == False and temp == False) : 
    print("Go out and visit the garden")

# """