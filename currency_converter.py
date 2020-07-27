print("@@@@@@@ currency converter @@@@@@@@")

with open('currency.txt') as cu:
    lines = cu.readlines()

curr_dict = {}
for line in lines:
    cur = line.split("\t")
    curr_dict[cur[0]] = cur[1]
amount = int(input("enter your amount: \n"))
print("these are the following option avilable: \n")
[print(item) for item in curr_dict.keys()]
user_input = input("\nchoose the above which you want  to convert from INR to specified currency: \n")
print(f"{amount}INR is equal to {amount * float(curr_dict[user_input])} {user_input}")