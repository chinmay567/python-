#guess the number
i=33
number_of_guess=1
print("number of attempt limited to 10 times:")
while(number_of_guess<=10):
    num1=int(input("guess your number:\n"))
    if num1<33:
        print("you guess lesser then number recorded:\n")
    elif num1>33:
        print("you gess higher then the number recorded:\n")
        print("number of guess left:\n", 10 - number_of_guess)
        number_of_guess = number_of_guess + 1
        continue
    else:
        print("you won:congratulations \n")
        print("number of guess you took to finish:\n",number_of_guess)
        break
    print("number of guess left:\n",10-number_of_guess)
    number_of_guess = number_of_guess+1
if(number_of_guess>10):
    print("game over")



