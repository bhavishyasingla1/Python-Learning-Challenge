#Files
myfile = open('newfile.txt')
print(myfile.read()) #it will return a massive string
print(myfile.read()) #it will return empty string, as cursor is in the end
myfile.seek(0) #placing cursor in staert
print(myfile.read()) #now all the string is back
myfile.seek(0)
print(myfile.readlines()) #each line a separate element in list

myfile.close() #we have to closefile

with open('newfile.txt') as mynewfile: #creating avariable for file, so we don't have to close it in the end
    contents = mynewfile.read()

    print(contents)



    with open('newfile.txt',mode = 'a') as mynewfile:
        mynewfile.write('\nthis is appended line')

with open('newfile.txt',mode = 'r') as mynewfile:
    contents = mynewfile.read()

print(contents)



with open('newfile.txt',mode='w') as mynewfile:
    mynewfile.write('overwritten file')

with open ('newfile.txt',mode='r') as mynewfile:
    print(mynewfile.read())


        #mode = 'r' read only
        #mode = 'w' writ only (overwrite files)
        #mode = 'r+' read + write
        #mode = 'w+' write + read (overwrite)
        #mode = 'a' append (add onn file)
