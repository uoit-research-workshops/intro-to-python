#!/usr/bin/python

#This is an int
a = 1
#This is a float
b = 65.2
#This is a string
c = 'banana'
#This is a boolean
d = True

#This is an example of a list
mylist = [a, b, c, d]

#List indexes start from zero!
print mylist[1]


#Looping over a list
for item in mylist:

    #Lets check that our data types are correct     
    print item, type(item)

    #Compare items in the list to something
    if item == 'banana':
        print 'This is a banana'

    else:
        print 'This is not a banana'












