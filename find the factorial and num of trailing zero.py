def fac(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fac(number-1)

def trailingZero(number):
    count = 0
    i = 0
    while(number//i != 0):
        count += int(number/i)
        i = i*5
    return count


if __name__ == '__main__':
    number = int(input("enter your num:"))
    factorial = fac(number)
    print('your factorial will be ', factorial)
    print(trailingZero(number))
    print("the trailing zero of this number will be:",trailingZero(number))