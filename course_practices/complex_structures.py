list_of_persons = [{'name': 'Vincenzo',
                     'age': 37,
                     'hobbies': ['movies', 'software development']},
                    {'name': 'Magleni',
                    'age': 36,
                     'hobbies': ['kitchen', 'content writter']},
                    {'name': 'Jose',
                    'age': 9,
                     'hobbies': ['video-games', 'movies']},
                    {'name': 'Alejandro',
                    'age': 15,
                     'hobbies': ['video-games', 'movies']}
                    ]

# list of names
list_of_names = [el['name'] for el in list_of_persons]
print('List of names: ' + str(list_of_names))

# are all older than 20
print('')
print('Older than 20')
older_than_20 = all([el['age'] > 20 for el in list_of_persons])
print('Are they older than 20? ' + str(older_than_20))

# copy and mutate list of persons
print('')
print('List copy')
list_of_persons_copy = [el.copy() for el in list_of_persons]
list_of_persons_copy[0]['name'] = 'Ramon'
print('List of persons: ' + str(list_of_persons))
print('List of persons copy: ' + str(list_of_persons_copy))

# unpack list of persons
person1, person2, person3, person4 = list_of_persons
print('')
print('Unpack')
print('Person1: ' + str(person1))
print('Person2: ' + str(person2))
print('Person3: ' + str(person3))
print('Person4: ' + str(person4))


