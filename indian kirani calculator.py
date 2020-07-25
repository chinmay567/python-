lst =[]
sum = 0
while(True):
    user_input = input("plese enter your product value and to quit enter 'q':\n")
    lst.append(user_input)
    if (user_input != 'q'):
        sum = sum + int(user_input)
    else:
        print(f"your sum total is {sum}.")
        break
for i in (lst):
    if i == 'q':
        print("Thank you visit us again")
    else:
        print(i)