# its a autometic password generator programme and input must be a positive intiger 
import string
import random
num = int(input("enter the length of the password: \n"))

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

s = []

s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)

print("your password is:",''.join(s[0:num]))
