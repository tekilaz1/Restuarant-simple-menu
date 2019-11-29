

print("I will help you to choose a good restuarant in this area")

people = int(input("how many people are you going (in number)?"))
if people > 0:
    print("great")
else:
    print("please enter a valid number of people ?")

kosher = input("should it be kosher(yes/no) ")
if kosher == "no":
    print("what kind of foods do you want ?")
    food = int(input("press '1'(normal), press'2'(vegetarian)' and ' '3'(vegan)"))
    if food == 1:
        print(" we have steak,  burger, salad and fish")
        normal = input("please enter your food Here (steak , burger salas or fish)")
    elif food == 2:
        print("nice to be vegetarian kinda of between")
        print("we have salads, pasta and  fish as well")
        veggie = input("please enter your food Here(salads , pasta or fish ")
    else:
        print("for Vegan  we  have only salads and  one type of burger.")
        vegan = input("please enter your food Here (salad or burger)")
    print("just a moment I'm gone bring the food")
    print("have a nice meal")
    exit()
else:
    print("okay one more option please")
    kind = input("should it be Kashrut lemehadrin (yes/no) ?")
    if kind == "yes":
        print("okay what kind of food do you want to eat?")
        food2 = input("Enter your food here ('kumush, salad shuq or  pasta')")
    else:
        print("what kind of food do you want to eat?")
        food3 = input("enter your type of food here('salad, shekshuka, or pasta")

print("just a moment I'm gone bring the food")
print("have a nice meal")
exit()


