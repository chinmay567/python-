import datetime

def gettime():
    return datetime.datetime.now()

def log(k):
    if k==1:
        num2 = int(input("enter 1 for excercise and 2 for food\n"))
        if num2==1:
            value=input("type here :\n")
            H1=open("harryexcercise.txt", "a")
            H1.write(str([str(gettime())]) + ": " + value + "\n")
            print('successfully written')
        elif num2==2:
            value = input("type here :\n")
            H2 = open("harrydiet.txt", "a")
            H2.write(str([str(gettime())]) + ": " + value + "\n")
            print('successfully written')
    if k==2:
        num2 = int(input("enter 1 for excercise and 2 for food\n"))
        if num2 == 1:
            value = input("type here :\n")
            H1 = open("hamidexcercise.txt", "a")
            H1.write(str([str(gettime())]) + ": " + value + "\n")
            print('successfully written')
        elif num2 == 2:
            value = input("type here :\n")
            H2 = open("hamiddiet.txt", "a")
            H2.write(str([str(gettime())]) + ": " + value + "\n")
            print('successfully written')
    if k==3:
        num2 = int(input("enter 1 for excercise and 2 for food\n"))
        if num2==1:
            value = input("type here :\n")
            H1 = open("rohanexcercise.txt", "a")
            H1.write(str([str(gettime())]) + ": " + value + "\n")
            print('successfully written:thumbs up')
        elif num2==2:
            value = input("type here :\n")
            H2 = open("rohandiet.txt", "a")
            H2.write(str([str(gettime())]) + ": " + value + "\n")
            print('successfully written:thumbs up')
        else:
            print("enter a valid input 1(harry),2(hamid),3(rohan)\n")

def retrieve(k):
    if k==1:
        num2 = int(input("enter 1 for excercise and 2 for food\n"))
        if num2==1:
            H1 = open("harryexcercise.txt")
            for i in H1:
                print(i,end=" ")
        elif num2==2:
            H2= open("harrydiet.txt")
            for i in H2:
                    print(i,end=" ")
    if k==2:
        num2 = int(input("enter 1 for excercise and 2 for food\n"))
        if num2==1:
            H1= open("hamidexcercise.txt")
            for i in H1:
                print(i,end=" ")
        elif num2==2:
            H2=open("hamiddiet.txt")
            for i in H2:
                print(i,end=" ")
    elif k==3:
        num2 = int(input("enter 1 for excercise and 2 for food\n"))
        if num2==1:
            H1=open("rohanexcercise.txt")
            for i in H1:
                print(i,end=" ")
        elif num2==2:
            H2=open("rohandiet.txt")
            for i in H2:
                print(i,end=" ")
        else:
            print("enter a valid input 1(harry),2(hamid),3(rohan)")


print("welcome to the health management system:\n")
num1=int(input("press 1 for log the value and 2 for retrieve\n"))
if num1==1:
    A=int(input("press 1 for harry 2 for hamid and 3 for rohan\n"))
    log(A)
else:
    A=int(input("press 1 for harry 2 for hamid and 3 for rohan\n"))
    retrieve(A)