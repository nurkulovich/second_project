
# Класс Human
#   1. Создайте класс Human. 
#   2. Определите для него два статических поля: default_name и default_age.
#   3. Создайте метод __init__(), который помимо self принимает еще два параметра: name и age. Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age. В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
#   4. Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
#   5. Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
#   6. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома: уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов данный метод принимает объект дома и его цену.
#   7. Реализуйте метод earn_money(), увеличивающий значение свойства money.
#   8. Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и размер скидки
# Класс House
#   1. Создайте класс House
#   2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price. 3. Свои начальные значения они получают из параметров метода __init__() 
#   4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом данной скидки.
# Класс SmallHouse
#   1. Создайте класс SmallHouse, унаследовав его функционал от класса House
#   2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
# Реализуйте:
# 1. Вызовите справочный метод  default_info() для класса Human()
# 2. Создайте объект класса Human
# 3. Выведите справочную информацию о созданном объекте (вызовите метод info()).
# 4. Создайте объект класса SmallHouse
# 5. Попробуйте купить созданный дом, убедитесь в получении предупреждения.
# 6. Поправьте финансовое положение объекта - вызовите метод earn_money()
# 7. Снова попробуйте купить дом
# 8. Посмотрите, как изменилось состояние объекта класса Human
class Human:
    default_name = 'A'
    default_age = 21

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        return f'name: {self.name}\nage: {self.age}\nmoney: {self.__money}\nhouse: {self.__house}'

    @staticmethod
    def default_info(name=default_name, age=default_age):
        return f'default_name: {name}\ndefault_age: {age} '

    def __make_deal(self, house, price):
        self.__house = house
        self.price = price
        return f'Куплен {self.__house} за {self.price}'

    def earn_money(self, money):
        self.__money += money

    def buy_house(self, house):
        if self.__money<house.price:
            return f'Мало денег. Не хватает еще {self.__money - house.price}'
        else:
            cost = house.price
            self.__money -= cost
            return self.__make_deal(house, cost)

    def __repr__(self):
        return f'default_name: {self.name}\ndefault_age: {self.age} '

    def __str__(self):
        return f'default_name: {self.name}\ndefault_age: {self.age} '

class House:
    def __init__(self, area=0, price=0):
        self._area = area
        self._price = price

    def final_price(self, sale):
        self._price -= sale
        return self._price

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f'Дом с площадью: {self._area}'

class SmallHouse(House):
    def __init__(self, area=40, price=0):
        self._area = area
        self._price = price

print(Human.default_info())
hum = Human('Nur', 18)
print(hum.info())
sh = SmallHouse(price=20000)
print(sh.final_price(1000))
print(hum.buy_house(sh))
hum.earn_money(20000)
print(hum.buy_house(sh))
print(hum.info())


# """
# 2. Задание:



# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

# Реализуйте:

#   Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)

class Tomato:
    states = {1:'green', 2:'blange', 3:'ripe'}

    def __init__(self, stat=states, index=1):
        self._index = index
        self._state = stat[self._index]

    def grow(self):
        if self._state == 'ripe':
            pass
        else:
            self._index += 1
            self._state = self.states[self._index]
            return self._state

    def is_ripe(self):
        if self._state == 'ripe':
            return 'Томат созрел'
        else:
            return 'Томат еще не созрел'

    def __repr__(self):
        return f'Томат: {self._state}'
    def __str__(self):
        return f'Томат: {self._state}'
    
class TomatoBush:
    tomatoes = []

    def __init__(self, count):
        self.count = count

        for i in range(1, self.count+1):
            a = Tomato()
            self.tomatoes.append(a)

    @classmethod
    def grow_all(cls):
        for i in TomatoBush.tomatoes:
            i.grow()

    @classmethod
    def all_are_ripe(cls):
        res = [True if i.is_ripe() == 'Томат созрел' else False for i in TomatoBush.tomatoes]
        return all(res)

    @classmethod
    def give_away_all(cls):
        TomatoBush.tomatoes.clear()

    def create_tomato(self, count):
        for i in range(count):
            tomato = Tomato(i)
            TomatoBush.tomatoes.append(tomato)
    
    @property
    def state(self):
        return f'Томат: {self._state}'
    def __str__(self):
        return f'Томат: {self._state}'
    


class Gardener:
    def __init__(self, name):
        self.name = name

    def work(self, _plant):
        _plant.grow()

    @classmethod
    def harvest(cls):
        if TomatoBush.all_are_ripe() == True:
            TomatoBush.give_away_all()
            print("Урожай собран")
        else:
            print("Нужен уход")  

    @staticmethod
    def knowledge_base():
        print("Используйте work для ухода за растением. harvest для сбора урожая" ) 

Gardener.knowledge_base()
gardener1 = Gardener("John")
bush = TomatoBush(3)
print(TomatoBush.tomatoes)
for i in range(3):
    gardener1.work(TomatoBush.tomatoes[i])
print(TomatoBush.tomatoes)
gardener1.harvest()
for i in range(3):
    gardener1.work(TomatoBush.tomatoes[i])
gardener1.harvest()

# for i in range(3):
#     gardener1.work(TomatoBush.tomatoes[i])
# print(TomatoBush.tomatoes)
    








        