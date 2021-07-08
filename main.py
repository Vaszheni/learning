from human.Knight import Knight
from arena.Arena import Arena

Arture = Knight(name="Arture", rank=1, health=100, power=10, equip=['sword', 'shield'])
Barbarossa = Knight(name="Barbarossa", rank=3, health=100, power=8, equip=['sword'])
Hexagon = Arena.battle([Arture, Barbarossa])