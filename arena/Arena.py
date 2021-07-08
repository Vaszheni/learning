from random import randint
from human import Knight
class Arena(Knight):
    def battle(self, knight1:Knight, knight2:Knight):
        while knight1.hp() > 0 or knight2.hp() > 0 :
            if randint(0, 9) < 5 :
                knight2.hp = knight2.hp() - knight1.power()
            else:
                knight1.hp = knight1.hp() - knight2.power()
