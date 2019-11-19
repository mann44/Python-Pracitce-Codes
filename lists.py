#Manthan Gajjar
# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1,3,4,5,6,7,12,445]
print(numbers)
#using Constructors

numbers1 = list((1,2,4,5,6,7))
print(numbers1)

fruits = ["Apples", "Oranges", "Grapes", 5]
print(fruits)

#Get Specific value from Index
print(fruits[2])

#Get Len
print(len(fruits))

#Append or Add something to a list
fruits.append("mango")
print(fruits)

#remove 
fruits.remove("Grapes")
print(fruits)

#insert into specific position
fruits.insert(2, "Stawberry")
print(fruits)

#Remove from position
fruits.pop(3)
print(fruits)

#reverse a list
fruits.reverse()
print(fruits)

#Sort a list
fruits.sort()
print(fruits)

#sort and reverse
fruits.sort(reverse=True)
print(fruits)



