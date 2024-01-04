#for loops in python
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print('Hello')


for num in mylist:
    #check for even number
    if(num%2==0):
     print(num)
    else:
     print(f'Odd number:{num}') #day2

list_sum = 0
for num in mylist:
   list_sum = list_sum+num

print(list_sum)

for letter in 'Hello World':
   print(letter)

   tup = (1,2,3)
   for item in tup:
      print(item)

mylist = [(1,2),(3,4)]
print(len(mylist))

for num in mylist:
   print(num)

for (a,b) in mylist: #tuple unpacking
   print(a)
   print(b)

d = {'k1':1,'k2':2 } #remb dictionaries are unordered

for num in d: #gives key 
   print(num)

for num in d.items(): #gives items in key
   print(num)

for key,value in d.items(): #gives items in key
   print(value)

for num in d.values(): #gives values only in key
   print(num)

   