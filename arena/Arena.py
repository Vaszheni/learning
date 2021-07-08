from random import randint
from human.Knight import Knight
class Arena(Knight):
    @staticmethod
    def battle(knights):
        #проверка количества участников
        if len(knights) != 2:
            print("неверное количество участников")
            return
        #проверка на соответсвие рангов
        if knights[0].rank != knights[1].rank:
            print("несоответствие рангов")
            return

        #проведение сражения
        while knights[0]._health > 0 and knights[1]._health > 0:
            if randint(0, 9) < 5:
                knights[1]._health = knights[1]._health - knights[0].power
            else:
                knights[0]._health = knights[0]._health - knights[1].power
        else:
            #вывод и ап победителя
            for knight in knights:
                if knight._health > 0:
                    print(f"Winner are {knight.name}")
                    knight.rank += 1
                    if knight.rank > 3:
                        knight.rank = 3
                    print(f'{knight.name} rank {knight.rank}')
