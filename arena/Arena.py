from random import randint
from human.Knight import Knight
class Arena():
    #def areYouLuccky(self, knight:Knight, value): #реализация методали или повезло
    #    if value == knight.luckyNumber:
    #        return True
    #    else:
    #        return False
        
    #def checkingParticipants(self, value):#вроверка количества участников
    #    if len(value) != 2:
    #        print('неверное количество сражающихся')
    #        return False
        
    #def checkingRanks(self, knights):#проверяем ранги учасников на совпадение
    #    rank = self.knights[0].rank #запониманем ранг
    #    if knights[0].rank != knights[1].rank:
    #        print('ранги учасвствующих неравны')
    #        return False
    #    else:
     #       return True

    @staticmethod
    def battle(knights):
        if len(knights) != 2: #проверка на количество учавствующих в сражении
            print('неверное количество сражающихся')
            return False

        if knights[0].rank != knights[1].rank:#проверка на соответствие рангов
            print('ранги учасвствующих неравны')
            return False

        #проведение сражения
        while knights[0]._health > 0 and knights[1]._health > 0:
            if randint(0, 9) < 5: #определяем кто бьёт
                #attaking = knights[0]
                #defending = knights[1]
                if randint(0,4) !=  knights[1].luckyNumber:
                    knights[1]._health = knights[1]._health + knights[1].armor - knights[0].power
                else:
                    print(f"{knights[1].name} miss")
            else:
                #attaking = knights[1]
                #defending = knights[0]
                if randint(0, 4) != knights[0].luckyNumber:
                    knights[0]._health = knights[0]._health + knights[0].armor - knights[1].power
                else:
                    print(f"{knights[0].name} miss")
            #defending.health = defending.health + defending.armor - attaking.power
        else:
            #вывод и ап победителя
            for knight in knights:
                if knight.health > 0:
                    print(f"Winner are {knight.name}")
                    knight.rank += 1
                    if knight.rank > 3:
                        knight.rank = 3
                    print(f'{knight.name} rank {knight.rank}')
