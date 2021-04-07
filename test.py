class Tomato:
  states = {1: "green", 2: "almost ripe", 3: "ripe"}
  __state_count = 1

  def __init__(self,_index):
    self._index = _index
    self._state = self.states[1]

  def grow(self):
    if self.__state_count == 3:
      pass
    else:
      self.__state_count +=1
      self._state = self.states[self.__state_count]

  
  def is_ripe(self):
    if self.__state_count == 3:
      return True
    else:  
      return False

  def __str__(self):
    return f"Томат {self._index}"

  def __repr__(self):
    return f"Томат {self._index}"



class TomatoBush:
  tomatoes = []

  def __init__(self, quantity):
    self.quantity = quantity
    self.create_tomato(self.quantity)

  @classmethod
  def grow_all(cls):
    for i in TomatoBush.tomatoes:
      i.grow()

  @classmethod
  def all_are_ripe(cls):
    res = [True if i.is_ripe() == True else False for i in TomatoBush.tomatoes]
    return all(res)

  @classmethod
  def give_away_all(cls):
    TomatoBush.tomatoes.clear()

  def create_tomato(self, quantity):
    for i in range(quantity):
      tomato = Tomato(i)
      TomatoBush.tomatoes.append(tomato)


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
bush1 = TomatoBush(3)
print(TomatoBush.tomatoes)
gardener1.work(bush1.tomatoes[0])
gardener1.harvest()
bush1.grow_all()
gardener1.harvest()
bush1.grow_all()
gardener1.harvest()
