# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.

import random
user_point = 1
comp_point = 1
no_of_chance = 0
chance = 10

print("\t \t \t \twelcome to the snake,water,gun game.\n \t \t \t \t")
print("\t \t \t \tyou are given 10 number of chance.\n \t \t \t \t")

lst = ["snake", "water", "gun"]
while no_of_chance < chance :
    user_choice = input('''choose from these :
                    snake
                    water
                    gun\n''')
    comp_choice = random.choice(lst)

    if user_choice == comp_choice:
        print(f"game tie both gain {0} point\n")
    elif user_choice == "snake" and comp_choice == "water":
        print(f"you won your point will be: {user_point}\n")
        user_point = user_point +1
    elif user_choice == "water" and comp_choice == "gun":
        print(f"you won your point will be: {user_point}\n")
        user_point = user_point +1
    elif user_choice == "gun" and comp_choice == "snake":
        print(f"you won your point will be: {user_point}\n")
        user_point = user_point + 1
    else:
        print(f"computer win computer points will be: {comp_point}\n")
        comp_point = comp_point + 1

    no_of_chance = no_of_chance + 1
    print(f"no of chance left: {chance - no_of_chance}")
    if chance - no_of_chance == 0:
        print("sorry!!! you left out of your chances\n")

print("game over\n")


if user_point == comp_point:
    print("game tie\n")
elif user_point > comp_point:
    print("congratulations:\n you won\n")
else:
    print("sorry!!!:\n you loose\n")

print(f"your point is: {user_point} and computer point is: {comp_point}\n")
print("thanks for playing have a good day!!!! ")