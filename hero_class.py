#Реалізувати клас Hero з атрибутами ( ранг, здоров'я, сила )
#Зробити перевірки що ранг є 1, 2, 3. Здоров'я і сила >0 and <=100, реалізувати метод битися, що дозволяє бити іншого героя 
#і наносити йому урон відповідний силі. Реалізувати метод відновлення здоров'я.
class Hero():
    def __init__(self, rank:int, health:int, power:int):
        self.set_hp(health)
        self.set_rank(rank) 
        self.set_power(power)
    
    #реалізація методів пов'язаних зі здоров'єм
    def get_hp(self):
        return self.__health
    
    def set_hp(self, health:int):
        if health < 1:
            self.__health = 1
        elif health > 101:
            self.__health = 100
        else:
            self.__health = int(health)
            
    health = property(get_hp, set_hp)
    #реалізація методів пов'язаних зі здоров'єм
    
    #реалізація методів пов'язаних силою
    def get_power(self):
        return self.__power
    
    def set_power(self, power:int):
        if power < 1:
            self.__power = 1
        elif power > 101:
            self.__power = 100
        else:
            self.__power = int(power)
            
    power = property(get_power, set_power)
    #реалізація методів пов'язаних зі здоров'єм
    
    #реалізація методів пов'язаних із рангом    
    def set_rank(self, rank:int):
        if rank < 1:
            self.__rank = 1
        elif rank > 3:
            self.__rank = 3
        else:
            self.__rank = int(rank)
    
    def get_rank(self):
        return self.__rank
        
    rank = property(get_rank, set_rank)
    #реалізація методів пов'язаних із рангом
        
    #реалізація методу підвищення здоровья  
    def restore_hp(self):
        self.set_hp(self.__health + 5)
        
    #реалізація методу удару
    def hit(self, auther_Hero):
        auther_Hero.__health -= self.__power
        
            
a1 = Hero(10,100,10)
b2 = Hero(1,80,2)
a1.hit(b2)
print(b2.health)
b2.restore_hp()
print(b2.health)

