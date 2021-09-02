# 1 
from os import name


class Food:

    def __init__(self, name, kind) -> None:
        self.name = name
        self.kind = kind

    def describe(self):
        print('The attrbiute name is {} and the kind is {}'.format(
            self.name, self.kind))
    
    def __repr__(self) -> str:
        return 'Food class with attributes, Name: {}, Kind: {}'.format(self.name, self.kind)


# food = Food(name='Test', kind='Class')
# food.describe()

#2
# class Food:

#     def __init__(self, name, kind) -> None:
#         self.name = name
#         self.kind = kind

#     @classmethod
#     def describe(self):
#         print('The attrbiute name is {} and the kind is {}'.format(
#             self.name, self.kind))


# food = Food(name='Test', kind='Class')
# food.describe()

#2.1
#2
# class Food:

#     def __init__(self, name, kind) -> None:
#         self.name = name
#         self.kind = kind

#     @staticmethod
#     def describe(self):
#         print('The attrbiute name is {} and the kind is {}'.format(
#             self.name, self.kind))


food = Food(name='Test', kind='Class')
food.describe()

class Meat(Food):
    def cook(self):
        print('Cooking {} with kind {}'.format(self.name, self.kind))


meat = Meat(name='Fish', kind='Test')
meat.cook()

class Fruit(Food):
    def clean(self):
        print('Cleaning {}, kind {}'.format(self.name, self.kind))

    def __repr__(self) -> str:
        return super().describe()


fruit = Fruit(name='Lemon', kind='Citrus')
fruit.clean()
print(food)
