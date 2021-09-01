
# task no 1 and no 2
# while True:
#     print(' ')
#     print('Write any text to the file or choose an option below')
#     print('q to quite')
#     print('p to print the file content')
#     user_input = input('Input something: ')
#     if user_input == 'q':
#         break
#     elif user_input == 'p':
#         with open('task.txt', mode='r') as file:
#             print('File content:')
#             print('=============')
#             print(file.read())
#     else:
#         with open('task.txt', mode='a') as file:
#             file.write(user_input)
#             file.write('\n')

# print('Done!')

# task no 3
# import json
# user_input_list = []
# while True:
#     print(' ')
#     print('Write any text to the file or choose an option below')
#     print('q to quite')
#     print('p to print the file content')
#     user_input = input('Input something: ')
#     if user_input == 'q':
#         break
#     elif user_input == 'p':
#         with open('task.txt', mode='r') as file:
#             print('File content:')
#             print('=============')
#             print(json.loads(file.read()))
#     else:
#         user_input_list.append(user_input)
#         with open('task.txt', mode='w') as file:
#             file.write(json.dumps(user_input_list))

# print('Done!')

# task no 3.1 and 4
import pickle
user_input_list = []
while True:
    print(' ')
    print('Write any text to the file or choose an option below')
    print('q to quite')
    print('p to print the file content')
    user_input = input('Input something: ')
    if user_input == 'q':
        break
    elif user_input == 'p':
        with open('task.p', mode='rb') as file:
            print('File content:')
            print('=============')
            print(pickle.loads(file.read()))
    else:
        user_input_list.append(user_input)
        with open('task.p', mode='wb') as file:
            file.write(pickle.dumps(user_input_list))

print('Done!')

