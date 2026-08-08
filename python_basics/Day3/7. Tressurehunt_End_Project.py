print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')

print("Welcome to Tresure Island, Your Mission is to find the tresure")
print("You are at the cross road, where do you want to go?\n" + "             "    'Type "left" or "right"')
direction = input().lower()
if direction == "left":
    print('You have encountered a lake, do you to "wait" for the boat or "swim"')
    actions = input().lower()
    if actions == "wait":
        print('You have reached an Isaland, kindly choose any one door "red", "blue" or "yellow"')
        door = input().lower()
        if door == "red":
            print("You drowned into a volcano and burned, Game Over!!")
        elif door == "blue":
            print("You were eatn by a dragon, Game Over!!")
        elif door == "yellow":
            print("You found the tressure, YOU WIN !!! :-)")
        else:
            print("Game Over!!")
    else:
        print("You drowned and died, Game Over!!")
else:
    print("You fell into a hole, Game Over !!")