operator=input("choose any one of the operator:+,-,*,/ :")
num1=int(input("enter your first num: "))
num2=int(input("enter your second num: "))
if num1==45 and num2==3 and operator=='*':
    print('555')
elif num1==56 and num2==9 and operator=='+':
    print('77')
elif num1==56 and num2==6 and operator=='/':
    print('4')
elif num1==30 and num2==4 and operator=='-':
    print('20')
elif operator=='*':
    num3=num1*num2
    print(num3)
elif operator=='+':
    num3=num1+num2
    print(num3)
elif operator=='/':
    num3=num1/num2
    print(num3)
elif operator=='-':
    num3=num1-num2
    print(num3)
else:
    print("error,please check the value")