import pytest
from creature import Creature

def test_is_alive():
    creature = Creature("Dragon", 18, 100, [])
    assert creature.is_alive() == True
    
    creature.take_damage(100)
    assert creature.is_alive() == False
    
def test_take_damage():
    creature = Creature("Dragon", 18, 100, [])
    assert creature.hit_points == 100
    
    creature.take_damage(10)
    assert creature.hit_points == 90
    
def test_attack_with_all_attacks():
    creature1 = Creature("Dragon", 18, 100, [{"number_of_attacks": 1, "to_hit_bonus": 10, "damage_roll": "1d10"}])
    creature2 = Creature("Goblin", 12, 20, [])
    creature1.target = creature2
