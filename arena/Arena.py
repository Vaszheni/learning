from random import randint
from human.Knight import Knight
class Arena():
    def areYouLuccky(self, knight:Knight, value): #реализация методали или повезло
        if value = knight.luckyNumber:
            return True
        else:
            return False
        
    def checkingParticipants(knights):#вроверка количества участников
        if len(knights) != 2:
            return False
        
    def checkingRanks(knights):#проверяем ранги учасников на совпадение
        rank = knights[0].rank #запониманем ранг
        if knights[0].rank != knights[1].rank:
            return false
        else:
            return True
        
        
    @staticmethod
    def battle(knights):#необходимо переделать с учётом имеющихся 2 методов проверки рангов и длинны масива учасников
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
            if randint(0, 9) < 5: #определяем кто бьёт
                attaking = knights[0]
                defending = knights[1]
                #knights[1]._health = knights[1]._health - knights[0].power
            else:
                attaking = knights[1]
                defending = knights[0]
                #knights[0]._health = knights[0]._health - knights[1].power
        else:
            #вывод и ап победителя
            for knight in knights:
                if knight._health > 0:
                    print(f"Winner are {knight.name}")
                    knight.rank += 1
                    if knight.rank > 3:
                        knight.rank = 3
                    print(f'{knight.name} rank {knight.rank}')
