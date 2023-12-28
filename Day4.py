#dictionaries {'key1':'value1','key2':'value2'} not sorted and unorderd

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key1'])

prices = {'appale':122,'oragng':299,'bnana':222}
print(prices['appale'])

d = {'k1':12,'k2':[1,2,3],'k3':{'insidekey':100} } #they are super flexible can store lists as well as dictionaries
print(d['k2'][2]) #calling specific index from 
print(d['k3']['insidekey']) #calling value from dic inside dictionary

d1 = {'k1':['a','b','c']}
print(d1['k1'][1].upper()) 

d1['k2']={2}
print(d1) #adding new key to dictionary we can also use same method to overwrite


print(d1.keys()) #returbn all keys in dictionary
print(d1.values()) #return value
print(d1.items()) #return items


#tuples 

t = (1,2,3) #tuple


print(type(t))


print(len(t))


t = ("one", 2 , 's')
print(t) #Support multiple datatypes, can do slicing aswell
print(t[-1]) #last index

t = (1,2,3,1,)
print(t.count(1)) #method to count how many times a element is shown in a tuple
print(t.index(1)) #to find index of particular element

mylist =  [1,2,3] #list
print(type(mylist))
print(len(mylist))

t = (1,2,3)

mylist[0]={'new'}
print(mylist) #we cannot do ta with tuples


#Sets  unorded colletobn of different elements
myset = set()
myset.add(1)
print(myset)

myset.add(2) #adding same element multiple times in a set
print(myset)

myset.add(1)
print(myset)

mylist = [1,2,2,2,2,2,2,3,3,3,3,4,4,54,4]
print(set(mylist)) #only gives unique elements

#boolean
type(True)
print(1==1)
print(1==14)


b = None
print(type(b))  #None datatype