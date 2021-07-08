class Human(object):
    def __init__(self, health: int, power: int):
        self.set_hp(health)
        self.set_power(power)

    # реалізація методів пов'язаних зі здоров'єм
    def get_hp(self):
        return self._health

    def set_hp(self, health: int):
        if health < 1:
            self._health = 1
        elif health > 101:
            self._health = 100
        else:
            self._health = int(health)

    health = property(get_hp, set_hp)

    # реалізація методів пов'язаних зі здоров'єм

    # реалізація методів пов'язаних силою
    def get_power(self):
        return self._power

    def set_power(self, power: int):
        if power < 1:
            self._power = 1
        elif power > 101:
            self._power = 100
        else:
            self._power = int(power)

    power = property(get_power, set_power)

    # реалізація методів пов'язаних зі здоров'єм


    # реалізація методу підвищення здоровья
    def restore_hp(self):
        self.set_hp(self._health + 5)


