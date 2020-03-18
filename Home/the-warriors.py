# https://py.checkio.org/en/miss
# Difficulty : Moderate

class Warrior:
    health : int = 50
    is_alive : bool = True
    attack: int = 5
    
class Knight(Warrior):
    attack= 7
    
def fight(unit_1,unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health-=unit_1.attack
        unit_1.health-=unit_2.attack
        if unit_2.health<=0:
            unit_2.is_alive=False
            return True
        elif unit_1.health<=0:
            unit_1.is_alive=False
            return False

# Example)
# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
#
# fight(chuck, bruce) == True
# fight(dave, carl) == False
# chuck.is_alive == True
# bruce.is_alive == False
# carl.is_alive == True
# dave.is_alive == False
