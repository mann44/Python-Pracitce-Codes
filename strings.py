#Manthan Gajjar

# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = "Its yo boy Mann Gajjar"

Money =  1000000

# Concatenatation
print("Hello" + name + "and My Salary is: ",Money)

# String Formatting

#Argument by Position
print('{},{},{}'.format(name,Money,'Done Deal'))

print('{2},{0},{1}'.format(name,Money,'Done Deal'))


#Argument by name
print("My name is {myname}, and I am {job}. My salary is {Money}".format(myname="Manthan", job="A Software Developer",Money = Money))

#F-strings Only Python 3.6+

print(f" a person with ${Money}, is {name}")

# String Methods
m = "Its a Developer's World"
c= "s"
print ("Capital:",m.capitalize())
print("Upper:",m.upper())
print("Lower:",m.lower())
print("swapcase:",m.swapcase())
print("length:",len(m))
print("replace:",m.replace("World","Universe"))
print("count:",m.count(c))

