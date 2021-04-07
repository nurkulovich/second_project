"""
1) Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:

dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"

Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
- init - инициализирует значение атрибута amount
- update - задаёт объекту новое значение amount
- repr - возвращает значение float
- str - метод, который реализует логику функции dollarize()

//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
"""

# def dollarize(cash):
#     if cash < 0:
#         cash = abs(cash)
#         main = str(cash).split('.')[0]
#         other = str(round(cash % 1, 2))[2:]
#         doll = []

#         while len(main) > 0:
#             doll.insert(0, main[-3:])
#             main = main[:-3]
#         return '-'+'$'+','.join(doll)+'.'+other
#     cash = abs(cash)
#     main = str(cash).split('.')[0]
#     other = str(round(cash % 1, 2))[2:]
#     doll = []

#     while len(main) > 0:
#         doll.insert(0, main[-3:])
#         main = main[:-3]
#     return '$'+','.join(doll)+'.'+other

def dollarize(num):
  return "${:,}".format(round(num, 2))

class MoneyFmt:
    Amount = 0

    def __init__(self, amount):
        self.Amount = amount

    def update(self, other):
        self.Amount = other

    def __repr__(self):
        print(self.Amount)
        return f'{self.Amount}'

    def __str__(self):
        return dollarize(self.Amount)

        

cash = MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
repr(cash)
# print(dollarize(-0.3))



"""
2) Велосипед.
Создайте класс Bike в котором будут инициализированы следующие атрибуты: self.cost
(стоимость)
self.make (производитель)
self.model (модель)
self.year (год выпуска)
self.condition (состояние)
self._sale_price = None (цена для продажи, по умолчанию None)
self.sold = False (продан или нет, по умолчания False)
Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод
для указания цены для продажи, который принимает цену и если она меньше стоимости, то
ставит дефолтную цену для продажи (стоимость + мин. прибыль).
Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость
ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда
возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи.
При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на True
и возвращает прибыль с продажи.

Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте
объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его
атрибутов.
"""
class Bike:
    min_profit = 2000

    def __init__(self, cost, make, model, year, condition, _sale_price = None,sold = False):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self._sale_price = _sale_price
        self.sold = sold

    def cost_to_sell(self, cost_):
        if self.cost + self.min_profit > cost_:
            self._sale_price = self.cost + self.min_profit
            return self._sale_price
        else:
            self._sale_price = cost_
            return self._sale_price

    def service(self, cost_to_service, new_condition):
        self.cost += cost_to_service
        self.condition = new_condition
        return self.cost_to_sell(cost_to_service)

    def sell(self):
        self.sold = True
        return self._sale_price - self.cost

    @classmethod
    def get_default_bike(cls):
        return cls(15000, 'Smimano', 'sport', 2020, 5)


bike = Bike.get_default_bike()
print(bike.cost_to_sell(16000))
print(bike.service(2000, 5))
print(bike._sale_price)
print(bike.cost)
print(bike.sell())






    
"""
3) Герой.
Разработайте программу по следующему описанию.
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
"герой". У героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, поднимается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""

# def get_number():
#   import random
#   return str(random.choice(range(100000, 200000)))

# class Heroes:
#   def __init__(self, team, number=None, level=0):
#     self.number = get_number()
#     self.team = team
#     self.level = level

#   def level_up(self):
#     self.level += 1

# class Soldiers:
#   def __init__(self, number):
#     self.number = number
  
#   def follow_heroes(self, heroes):
#     self.team = heroes.team

#   def __repr__(self):
#     return self.number

# heroes1 = Heroes('team1')
# heroes2 = Heroes('team2')

# soldiers = [Soldiers(get_number()) for _ in range(1, 11) ]
# team1 = []
# team2 = []
# for soldier in soldiers:
#   import random
#   team = random.randint(1, 2)
#   if team == 1:
#     team1.append(soldier)
#   else:
#     team2.append(soldier)

# print(f'Длина команды heroes1: {len(team1)}', f'\nДлина команды heroes2: {len(team2)}')

# if len(team1) > len(team2):
#   heroes1.level_up()
# else:
#   heroes2.level_up()

# print(heroes1.level, heroes2.level)

# if heroes2.level > heroes1.level:
#   team1[0].follow_heroes(heroes2)
# else:
#   team1[0].follow_heroes(heroes1)

# print(f'Первый герой: {heroes1.number}\nВторой герой: {heroes2.number}')
# print(f'Первая команда: {team1}\nВторая команда: {team2}')

class Game:
  id_list = []
  team1 = []
  team2 = []
  team3 = []
  team4 = []
  
  def generate_id(self):
      import random
      id_ = random.randint(9999, 99999)
      while id_ in self.id_list:
          id_ = random.randint(9999, 99999)
      self.id_list.append(id_)  
      return id_

  def choose_team(self):
    import random
    teams = ["team1", "team2", "team3", "team4"]
    self.team = teams[random.randint(0, 3)]
    self.check_team()

  def check_team(self):
    if self.team == "team1":
      self.team1.append(self.id_)
    elif self.team == "team2":
      self.team2.append(self.id_)
    elif self.team == "team3":
      self.team3.append(self.id_)
    elif self.team == "team4":
      self.team4.append(self.id_)      
    return self.team

class Hero(Game):
  def __init__(self, id_=None, team = None, level = 0, team_len=0):
    self.id_ = self.generate_id()
    self.team = team
    self.team_len = team_len
    self.level = level
    self.check_team()      

  def level_up(self):
    if self.id_ in self.max_team():
      self.level += 1
  
  @classmethod
  def max_team(cls):
    from functools import reduce
    max_team = reduce(lambda x, y: x if len(x) >= len(y) else y,[cls.team1, cls.team2, cls.team3, cls.team4])
    return max_team    

  def __str__(self):
    return f"Герой команды: {self.team}, мой id: {self.id_} мой уровень: {self.level}"
    
  def __repr__(self):
    return f"Герой команды: {self.team}, мой id: {self.id_} мой уровень: {self.level}"


class Unit(Game):
  def __init__(self, id_=None, team = None):
    self.id_ = self.generate_id()
    self.team = self.choose_team()

  @staticmethod
  def follow_hero(obj):
    print(f"Я иду за героем команды {obj.team}")

  def __str__(self):
    return f"Солдат с id: {self.id_}. Команда: {self.team}"
    
  def __repr__(self):
    return f"Солдат с id: {self.id_}. Команда: {self.team}"


def create_units(quantity:int):
  units = {"unit" + str(name): Unit() for name in range(quantity)}
  return units

def print_team_len():
  print(f"team1: {len(Game.team1)}")
  print(f"team2: {len(Game.team2)}")
  print(f"team3: {len(Game.team3)}")
  print(f"team4: {len(Game.team4)}")  



hero1 = Hero(team = "team1")
hero2 = Hero(team = "team2")
hero3 = Hero(team = "team3")
hero4 = Hero(team = "team4")

units = create_units(100) 

print_team_len()

units["unit24"].follow_hero(hero1)
print(units["unit24"])
print(hero1)

hero1.level_up()
hero2.level_up()
hero3.level_up()
hero4.level_up()
print(hero1)
print(hero2)
print(hero3)
print(hero4)




"""
4) Напишите класс учеников Makers, который будет содержать 4 атрибута: 

- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)

Также класс должен содержать следующие методы:

- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.
"""


# class MakersStudents:
#   students_count = 0

#   def __init__(self, name, language):
#     self.name = name
#     self.language = language

#   @classmethod
#   def new_student(cls, name, language):
#     cls.students_count += 1
#     return cls(name, language)

#   def get_info(self):
#     print(f'Name: {self.name}. Language: {self.language}')

#   def set_kpi(self, kpi):
#     self.kpi = kpi

# student1 = MakersStudents.new_student('Nikita', 'Python')
# student2 = MakersStudents.new_student('Raatbek', 'JS')
# student1.get_info()
# student2.set_kpi(90)
# print(student2.kpi)
# print(MakersStudents.students_count)
