#Manthan Gajjar
# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Simpe Tuple
fruit_tuple = ("apple", "Oragne", "Mango")
print("1",fruit_tuple)

#using Constructor
fruit_Constr = (("Apple", "Orange", "Banana", "Kiwi"))
print("2",fruit_Constr)

#Get single value
print("3",fruit_Constr[2])

#can not change value
#fruit_Constr[1]= "Grape"
#print(fruit_Constr)

#Tuples with one value should have trailing comma

fruit_tuple_2 = ("Apple",)

print("4",len(fruit_tuple_2))

#Delet from tuple
del fruit_tuple_2
#print(fruit_tuple_2)

# A Set is a collection which is unordered and unindexed. No duplicate members.
cars_set = {"Audi", "Mercedez", "Alpha Romeo", "Range Rover"} 

print("5",cars_set)

#Check if in set
print("Audi" in cars_set)

#add to set
cars_set.add("BMW")
print("6",cars_set)

#remove from set
cars_set.remove("Alpha Romeo")
print("7",cars_set)

