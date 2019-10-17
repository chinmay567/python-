import time

#if , elif, else #iterator
#for , while


my_DataBase_pass = [23,'1997chinu',5,7,8,89,54,64]

my_dict = {'name':'chinu', 'password':'1997ch', 'mobNo':455, '01':'ID'}

my_str = 'k.Chinmay Dora'

my_int = 862

your_int = 865


##equal to (==)
##greater than(>)
##less than (<)
##greater than equal to (>=)
##less than equal to (<=)
##not equal to (!=)


##if (some conditions):
##    do some thing...
##    operation..
##
##elif (some_condition):
##    do something ..
##
##elif (some_condition):
##    do something  ..
##else:
##    print()
##    do something ...


'''

if my_dict['password'] in my_DataBase_pass :
    print('User Loged In')
    
else:
    print('Login Error')
    
    #print(my_dict)
'''
'''
print('Start:>')
#loop :-
time.sleep(6)
for key in my_dict:
    time.sleep(1)
    print(key,':',my_dict[key])
    #print(my_dict[key])
    
    print('\n')
'''
'''
import time


charge=1
while charge >0:
    for h in range(0,24):
        for m in range(0,60):
            for s in range(0,60):
                print(h,'h',m,'m',s,'s')
                time.sleep(0.1)
                
    charge = charge - 1

'''
'''
li = []
for i in range (0,101,2):
    li.append(i)
    print(li)
'''         
