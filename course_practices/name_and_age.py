def print_name_and_age(name, age):
    print("Your name is " + name + " and you are " + age + " years old")


def get_decades(age):
    return int(int(age)/10)


name = input("Your name please: ")
age = input("Your age please: ")

print_name_and_age(name, age)
decades = get_decades(age)
print("You have lived " + str(decades) + " decades")
