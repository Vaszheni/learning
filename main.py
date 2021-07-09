from human.Knight import Knight
from arena.Arena import Arena

Arture = Knight(name="Arture", rank=3, health=100, power=15, equip=['sword', 'shield'])
Barbarossa = Knight(name="Barbarossa", rank=3, health=100, power=10, equip=['sword'])
Arena.battle(knights=[Arture, Barbarossa])