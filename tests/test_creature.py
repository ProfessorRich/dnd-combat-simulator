import pytest
from creature import Creature

@pytest.fixture
def orc():
    attacks = [{'number_of_attacks': 2, 'to_hit_bonus': 5, 'damage_roll': '1d6'}]
    return Creature('Orc', 13, 30, attacks)

@pytest.fixture
def goblin():
    attacks = [{'number_of_attacks': 1, 'to_hit_bonus': 4, 'damage_roll': '1d4'}]
    return Creature('Goblin', 12, 20, attacks)

def test_is_alive(orc):
    assert orc.is_alive() == True

def test_take_damage(orc):
    orc.take_damage(10)
    assert orc.hit_points == 20

def test_attack(orc, goblin):
    orc.attack(goblin)
    assert goblin.hit_points <= 20

def test_does_attack_hit(orc, goblin):
    assert orc.does_attack_hit(5, goblin) == True or False

def test_do_damage(orc, goblin):
    orc.do_damage('1d6', goblin)
    assert goblin.hit_points <= 20