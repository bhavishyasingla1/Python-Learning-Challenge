name = "Singla"
print("Bhavishya "+name) #string concatenation
name = "Max wax"
print(10*name) #printing string by multiplyig with a number
print(name.upper()) #changing to upper case // doesnot affect original string
#lower to change to lowercase 
print(name.split())


#formatting
print("This is a string {}".format("Inserted"))
print("Your Name is {1} {0}".format("Singla","Bhavishya")) #we can format with index number as well
print("Your Name is {firstname} {lastname}".format(lastname = "Singla",firstname ="Bhavishya")) #we can use variables

result = 111/2222
print(result)
print("Value is {r:55.21}".format(r = result)) #{value:width.precision}

#newer method
print(f"Value is {result}")