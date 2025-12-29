# 1 to 10
for number in range(1,11):
    print(number)

# print name letter by letter

name = 'ashu'
for letter in name:
    print(letter)


# even numbers 2 to 20
for number in range(2,21):
    print(number)

# reverse a number
for number in range(5,0,-1):
    print(number)

# Loop over dict and print key:value

data = {'name': 'ashu',
        'degree': 'bca',
        'skill': 'python'}
for key,value in data.items():
    print(f"{key.title()}: {value.title()}")

# letter in name
name = 'ashu'
for letter in name:
    print(letter.title())

# num in [1,2,3]
number = [1,2,3]
for num in number:
    print(num)

# ch in python
language = "Python"
for ch in language:
    print(ch)

# for key in dict
data = {"a":"1","b":2}
for key in data.keys():
    print(key)
for value in data.values():
    print(value)
for items in data.items():
    print(items)

# intented code that repeats
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
# continue skips the current value
# break stops loop instantly
for i in range(20):
    if i == 12:
        continue
    if i == 18:
        break
    print(i)

# enumerates() - gives index + value
for idx,value in enumerate(["A","B","C"]):
    print(idx,value)

# fruit list

fruits = ['apple','banana','mango']
for idx,value in enumerate(fruits, start = 1):
    print(f"{idx} - {value}")

# enumerate in dict

data = {'name': 'rohan',
        'pet name': 'bella',
        'address': 'vasundhara'}
for idx,(key,value) in enumerate(data.items(),start=1):
    print(f"{idx}. {key.title()} : {value.title()}")



# enumerate in multiple dict

person_1 = {'name': 'rohan',
            'age': 21,
            'college': 'ims'}
person_2 = {'name': 'akshit',
            'age' : 23,
            'college': 'du'}
person_3 = {'name': 'naman',
            'age': 21,
            'college': 'iimt'}

for idx,(key,value) in enumerate(person_1.items(),start = 1):
    print(f"{idx}. {key.title()} : {value.title() if isinstance(value,str) else value}")

for idx,(key,value) in enumerate(person_2.items(),start = 1):
    print(f"{idx}. {key.title()} : {value.title() if isinstance(value,str) else value}")

for idx,(key,value) in enumerate(person_3.items(),start = 1):
    print(f"{idx}. {key.title()} : {value.title() if isinstance(value,str) else value}")


# top 5 rich persons in the world

person_1 = {'name': 'elon musk',
            'source of wealth': ['tesla','spacex','x','ai and tech investments.'],
            'age': 54}
person_2 = {'name': 'Larry page',
            'source of wealth': 'co founder of google/alphabate.',
            'age': 52}
person_3 = {'name': 'Larry ellison',
            'source of wealth': 'oracle',
            'age': 84}
person_4 = {'name': 'jeff bezos',
            'source of wealth': ['amazon','blue origin'],
            'age': 61}
person_5 = {'name': 'sergey brin',
            'source of wealth': 'co founder of google/alphabate',
            'age': 52}

billionaire = [person_1, person_2, person_3, person_4, person_5]

for person in billionaire:
    for idx,(key,value) in enumerate(person.items(),start=1):
    
        print(f"{idx}. {key.title()} - {value.title() if isinstance(value,str) else value}")
