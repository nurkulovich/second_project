# 1) Напишите класс MyList, который наследуется от list. Сделайте так,
# чтобы индексация
# элементов начиналась с 1. Например:
# x = MyList([1,2,3,4,5])
# x[1] → 1


class MyList(list):
    def __getitem__(self, index):
        if index >= 1:
            index -= 1
            return super().__getitem__(index)
        elif index == 0:
            raise IndexError('индексация с 1 начинается')
        return super().__getitem__(index)


a = MyList(['a', 'b', 'c'])
print(a[1])



# 2) Определите класс A, в нём объявите метод method1, который печатает
# строку "Hello World". Затем создайте класс B, который будет
# наследоваться от класса A. Создайте экземпляр от класса B, и через него
# вызовите метод method1.

class A:
    def method1(self):
        print('Hello World')

class B(A):
    pass

a = B()
a.method1()

# 3) Создайте класс Auto в нем реализуйте метод ride который выводит
# сообщение Riding on a ground, создайте класс Boat реализуйте метод
# swim, который выводит floating on water.
# Создайте класс Amphibian который наследуется от класса Auto и Boat.
# Создайте от него объект и вызовите все методы.

class Auto:
    def ride(self):
        print('Riding on a ground')

class Boat:
    def swim(self):
        print('floating on water')

class Amphibian(Auto, Boat):
    pass

amp = Amphibian()
amp.ride()
amp.swim()

# 4) Создайте класс MyString, который будет наследоваться от str.
# Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Пример:
# # example = MyString('String')
# # example.append('hello')
# # print(example) -> 'Stringhello'
# # print(example.pop()) -> 'o'
# # print(example) -> 'Stringhell'

class MyString(str):
    def __init__(self, string):
        self.string = string

    def append(self, a):
        self.string = self.string + a
        return self.string 

    def pop(self):
        x = self.string[-1]
        self.string = self.string[:-1]
        return x
    
    def __str__(self):
        return self.string

example = MyString('String')
example.append('hello')
print(example)
print(example.pop())
print(example) 
