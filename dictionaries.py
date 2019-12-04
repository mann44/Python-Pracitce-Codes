# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#simple dict
person = {'first_name':'Mann', 'last_name':'Gajjar', 'age': 26}

#using constructor
person2 = dict(first_name='Mann', last_name='Gajjar', age= 26)

print("1",person,"\n","2",person2)

print(person2['first_name'])
print(person.get('last_name'))

#add key/value
person['Phone'] = '510-150-5105'
print(person)

#get values
print(person.items())

#make copy
person3 = person2.copy()
person3['City'] = 'San Jose'
#print(person3)

#remove item
del(person2)
person.pop("age")

print(person)
person.clear()
print(person)

#get Lenght
print(len(person3))

#list of dict
people = [
    {'name': "manthan", "age" : 25},
    {'name': "Pat", "age" : 22},
    {'name': "mike", "age" : 35},
        ]
print(people[1]['name'])