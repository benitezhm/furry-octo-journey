list_of_names = ['Miguel', 'Luz', 'Miguelangel', 'Samuel']
print('List of name size is ', len(list_of_names))

for name in list_of_names:
    name_size = len(name)
    if name_size > 5:
        print(name + ' is ' + str(name_size) + ' characters long')
    if 'n' in name or 'N' in name:
        print(name + " has 'n' or 'N' in it")

while len(list_of_names) > 0:
    list_of_names.pop()
else:
    print('List of name size is ', len(list_of_names))