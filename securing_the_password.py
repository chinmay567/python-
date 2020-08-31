secure = (('s','$'),('o','0'),('i','1'),('and','&'),('a','@'),('1','!'))

def secure_password(password):
    for a,b in secure:
        password = password.replace(a,b)
    return password


if __name__ == "__main__":
    password = input("enter your password:")
    password = secure_password(password)
    print(f"your password will be {password}")