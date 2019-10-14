#data type >>

#int
a = 5 #im

#float
b = 5.0 #im

#str
c= 'chinmay567'  #im

#complexb  #im
cp = 4+7j

#list
li=[5,4,988,65,4,'chinu']#1[23,e,43,4,,4,,f,d,f[df,,df],[d,f,df,],[df,df,d,f,]]  #mu  

#set
raja = 500
j = 'chinu'
st={4,65,4,6,raja,j}   #mu

#tuple
tu=(5,47,85,4,6,7,'chinu')   #imutable *******

#dict
di = {'key1':6, "key2":[11,70]}  #mu

ds = {}




print('\nList: ')

#1.List(li)         #COMMENT >>
print(li)           #[5,4,988,65,4]
print(id(li))       #random like 45842571223
print(type(li))     #<class 'list'>
print(len(li))      #5
li.append(5649)     #element add
print(li)           #[5,4,988,65,4,5649]
li.remove(988)      #element to remove
print(li)           #[5,4,65,4,5649]
print(li[2])        # prints element of index '2' = 65
ind = li.index(4)   #ind = 1 to find index of element in a list
print(ind)          #1
print(li.pop(2))
print(li)




print('\nDictionary: ')

#2*dict(di)
print(type(di))   #<class 'dict'>
print(id(di))     #1344566 #RANDOM
print(di)         #{'key1':6, 'key2': 11}
print(len(di))
di['name'] = 'chinmay'   #adding key with 
di['RollNo'] = 104      #value
di[5] = 'id'
print(di)
print(di.pop('key2'))  #print the value and remove
print(di)





print('\nSet: ')

print(st)
st.remove(65)
st.add(64565)
print(st)
print(st.pop())
print(st)
print(st.pop())
print(st)
#st[65] = 10 #TypeError: 'set' object does not support item assignment


print('\nTuple: ')
print(type(tu))
#tu[0] = 10   #TypeError: 'tuple' object does not support item assignment

