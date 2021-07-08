#Реалізувати клас Hero з атрибутами ( ранг, здоров'я, сила )
#Зробити перевірки що ранг є 1, 2, 3. Здоров'я і сила >0 and <=100, реалізувати метод битися, що дозволяє бити іншого героя 
#і наносити йому урон відповідний силі. Реалізувати метод відновлення здоров'я.
from equip.Equip import Equip
from human.Human import Human

class Knight (Human, Equip):
    def __init__(self, rank: int, health: int, power: int, equip: list):
        self.set_rank(rank)
        super(Human, self).__init__(health, power)
        super(Equip, self).__init__(equip)

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