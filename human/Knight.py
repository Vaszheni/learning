#Реалізувати клас Hero з атрибутами ( ранг, здоров'я, сила )
#Зробити перевірки що ранг є 1, 2, 3. Здоров'я і сила >0 and <=100, реалізувати метод битися, що дозволяє бити іншого героя 
#і наносити йому урон відповідний силі. Реалізувати метод відновлення здоров'я.
from equip.Equip import Equip
from human.Human import Human
from random import randint

class Knight (Human, Equip):
    def __init__(self, name:str, rank: int, health: int, power: int, equip: list):
        self.luckyNumber = randint(0, 4) #добавили число для промаха
        self.name = name
        self.set_rank(rank)
        #self.rank = rank
        super().__init__(health, power)
        super(Human, self).__init__(equip)
        if "sword" in equip:
            self.power += 5

    # реалізація методів пов'язаних із рангом
    def set_rank(self, rank: int):
        if rank < 1:
            self.__rank = 1
        elif rank > 3:
            self.__rank = 3
        else:
            self.__rank = int(rank)

    def get_rank(self):
        return self.__rank

    rank = property(get_rank, set_rank)



    # реалізація методів пов'язаних із рангом
