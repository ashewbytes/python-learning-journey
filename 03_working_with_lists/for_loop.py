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


# top 5 tech cities
city_1 = {'city': 'san francisco',
          "why it's famous": ['google','apple','facebook','thousands of startups'],
          'what happens there': ['inovation','venture capital','world-leading research & development'],
          'vibe': ['fast-paced','highly competitive','huge networking opportunities']}

city_2 = {'city': 'bengaluru',
          "why it's famous": 'silicon valley of india',
          'what happens there': ['IT services, software development','tons of startups'],
          'vibe':['energitic','multicultural','lots of opportunities for developers']}

city_3 = {'city':'Seattle',
          "Why it's famous": 'headquartors of microsoft and amazon',
          "What happens there": ['cloud computing','AI research','enterprise software innovation'],
          'vibe': 'mix of big company stability and modern tech culture'}

city_4 = {'city':'shenzhen',
          "Why it's famous": "china's hardware & electronics capital",
          "what happens there": ['huawei','tencent labs','countless manufacturing R&D teams'],
          'vibe': ['fast engineering cycles','hands on innovation']}

city_5 = {'city': 'tel aviv',
          "why it's famous": "one of the world's hottest startups ecosystems per capita",
          "what happens there": ['cybersecurity','AI','biotech','defence tech','high innovatuon','strong research culture'],
          'vibe': ['young','ambitious','intensely collaborative scene']}

cities = [city_1,city_2,city_3,city_4,city_5]
for city in cities:
    for idx,(key,value) in enumerate(city.items(),start=1):
        if isinstance(value,list):
            value = ", ".join(items.title() for items in value)
        
        print(f"{idx}. {key.title()} : {value.title() if isinstance(value,str) else value}")



data = {"name" : "rohan",
        "pet" : "bella",
        "address" : "vasundhara",
        "age": 22}
for idx,(key,value) in enumerate(data.items(),start = 1):
    print(f"{idx}. {key.title()} : {value.title() if isinstance(value,str) else value}")


person_1 = {"name" : "rohan",
            "age" : 22,
            "runs" : 4000,
            "pet" : "dog"}
person_2 = {"name" : "akshit",
            "age" : 22,
            "runs" : 2000,
            "pet" : "cat"}
person_3 = {"name" : "tarun",
            "age" : 22,
            "runs" : 5500,
            "pet" : "cat"}
persons = [person_1,person_2,person_3]
for person in persons:
    for idx,(key,value) in enumerate(person.items(),start=1):
        print(f"{idx}. {key.title()} : {value.title() if isinstance(value,str) else value}")



countries = {
    "japan" : ["tokyo","osaka","kyoto"],
    "switzerland" : ["zurich","geneva","basel"],
    "usa" : ["new york","san fransisco","chicago"],
    "finland": ["helsinki","espoo","tempere"],
    "italy" : ["rome","milan","venice"]
}

for idx,(key,value) in enumerate(countries.items(),start=1):
    if isinstance(value,list):
        value = ", ".join(city.title() for city in value)
        print(f"{idx}. {key.title()} : {value}")



data_1 = {'name': 'rohan',
        'class': '10th',
        'school': 'jkg',
        'favorite sports': ['cricket','baseball','football']}
data_2 = {'name': 'akshit',
          'class': '10th',
          'school': 'st. teresa',
          'favourite sports': ['table tennis','badminton']}

information = [data_1,data_2]
for data in information:
    for idx,(key,value) in enumerate(data.items(),start=1):
        if isinstance(value,list):
            value = ", ".join(info.title() for info in value)
        print(f"{idx}. {key.title()} : {value.title()}")


students_data = {
    "student_1": {
        'name': 'akshit',
        'course': 'python',
        'favourite languages': ['c','python']
    },
    "student_2": {
        'name': 'rohan',
        'course': 'javascript',
        'favourite languages': ['java','linux']
    },
    "student_3" : {
        "name": "ashu",
        "course": "python",
        "favourite languages": ['go','python','c++']
    }
}
for student in students_data.values():
    for idx,(key,value) in enumerate(student.items(),start=1):
        if isinstance(value,list):
            value = ", ".join(item.title() for item in value)
        print(f"{idx}. {key.title()} : {value.title()}")


data = {'college': "ims",
        'topics': ['python', 'mahcine learning', 'cloud'],
        'students': 120}
for key,value in data.items():
    if isinstance(value,list):
        formatted_list = []
        for item in value:
            if isinstance(item,str) and item.lower() == 'ims':
                formatted_list.append(item.upper())
            elif isinstance(item,str):
                formatted_list.append(item.title())
            else:
                formatted_list.append(str(item))
            value = ', '.join(formatted_list)

    elif isinstance(value,str):
        if value.lower() == 'ims':
            value = value.upper()
        else:
            value = value.title()

    
    else:
        value = str(value)

    print(f"{key.title()} : {value}")


