# # # Типы методов:
# # # методы экземпляра класса instance methods
# # методы , изменяющие состояние конкретного объекта
# # method(self)
# # # методы класса class methods
# # методы, изменяющие состоягие самого класса
# # @classmethod
# # method(cls)

# # статические методы static methods
# # методы , не изменяющие состояние ни класса, ни его объекта
# # Обычно добавляют в класс для группировки однотипной логики
# # @staticmethod
# # def method()

# class A:
#     attr1 = 'value'

#     def __init__(self, attr2):
#         self.attr2 = attr2

#     @classmethod
#     def set_attr1(cls, new_value):
#         cls.attr1 = new_value

#     def set_attr2(self, new_value):
#         self.attr2 = new_value

#     @staticmethod
#         def method1():
#             print('Static!')

# obj1 = A(20)
# obj1.set_attr1(30)
# obj1.set_attr2(2435)
# obj1.method1

# A.set_attr1()
# A.method1()

# def add(x, y):
#     return x+y

# class MayhOperatsummion:
#     @sraticmethod
#     def add(x, y):
#         return x + y

# class User:
#     def __init_(self, username, password,**fields):
#         self.username - username
#         self.password = self._get_envrypted_password(password)



# class A:
#     attr1 = 'vaue'

#     def set_attr1(self, new_value):
#         self.attr1 = new_value # self.__class__.attr1 = new_ value чтобы изменить у всех

# a = {'a': 1, 'b': 2, 'c':3}
# a.get('c')
# b = dict.fromkeys(['a', 'b', 'c'], 0)
# print(b)
# print(type(b))

# . Создайте класс Passport, в котором есть следующие
# атрибуты:
#  Атрибут класса users_images,в котором хранится пустой список, и атрибут класса black_list - тоже
# пустой список
#  Атрибуты экземпляра класса при инициализации
# объекта: name, last_name, date_of_birth, image, INN
# (INN при создании объекта равен None)
#  Метод check_dublicate_person, который при
# вызове через созданный объект класса, заносит
# атрибут данного объекта image в список
# users_image, если такой фотографии еще нет,
# если же она уже есть, т.е. если человек с такой
# фотографией уже есть в нашей “базе данных”, то
# этот объект-человек, через который мы вызвали
# данный метод, заносится в черный список. 
#  Также есть метод get_inn, который выдает
# сгенерированный INN для объекта. INN должен
# содержать какое-то число от 1999999-19999999.
# Но если объект находится в черном списке, то
# метод get_inn выдает сообщение: “Для объекта
# черного списка INN не генерируется”
#  По надобности переопределите методы str
# или repr

# Создайте объекты от класса Passport и вызовите у каждого
# объекта метод check_dublicate_person и метод get_inn. Также
# проверьте черный список и users_images.

class Passport:
    users_images = []
    black_list = []

    def __init__(self, name, last_name, date_of_birth, image, INN=0):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.image = image
        self.INN = INN

    def check_dublicate_person(self):
        if self.image not in self.users_images:
            self.users_images.append(self.image)
        else:
            self.black_list.append(self)
    
    def get_inn(self):
        if self.name not in self.black_list and self.INN == 0:
            # import string
            import random 
            INN = random.choice([10,20,30])#range(10000,50000))
            self.INN = INN
            return self.INN
        return 'Для объекта черного списка INN не генерируется'

    def __repr__(self):
        return f'{self.name} {self.last_name}'

print(Passport.users_images)
print(Passport.black_list)
ps = Passport('Nur', 'NUrkulov', '25.12.1997', '124t43.jpeg')
ps.check_dublicate_person()
print(ps.get_inn())
ps1 = Passport('Aika', 'Ulukmana', '04.04.1999', '1245.jpeg')
ps1.check_dublicate_person()
print(ps1.get_inn())
ps1.check_dublicate_person()
print(ps1.get_inn())
print(ps1.INN)
print(Passport.users_images)
print(Passport.black_list)

    
        
    



