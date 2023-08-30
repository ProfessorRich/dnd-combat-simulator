import pytest
from battle import run_two_creature_battle, roll_initiative, set_targets_to_next_creature, run_rounds, creatures_hit_points_random_walk
from creature import Creature

# mock roll_dice to make the tests deterministic
def mock_roll_dice(dice_string):
    return 10

@pytest.fixture(autouse=True)
def mock_dice_roll(monkeypatch):
    monkeypatch.setattr('battle.roll_dice', mock_roll_dice)
    monkeypatch.setattr('creature.roll_dice', mock_roll_dice)

def test_run_two_creature_battle():
    creature1 = Creature("Dragon", 18, 100, [{'number_of_attacks': 1, 'to_hit_bonus': 5, 'damage_roll': '1d10'}])
    creature2 = Creature("Goblin", 12, 20, [{'number_of_attacks': 1, 'to_hit_bonus': 2, 'damage_roll': '1d6'}])
    run_two_creature_battle(creature1, creature2)
    assert creature1.is_alive() == True
    assert creature2.is_alive() == False

def test_roll_initiative():
    creature1 = Creature("Dragon", 18, 100, [])
    creature2 = Creature("Goblin", 12, 20, [])
    creatures = roll_initiative([creature1, creature2])
    assert creatures == [creature1, creature2]

def test_set_targets_to_next_creature():
    creature1 = Creature("Dragon", 18, 100, [])
    creature2 = Creature("Goblin", 12, 20, [])
    set_targets_to_next_creature([creature1, creature2])
    assert creature1.target == creature2
    assert creature2.target == creature1

def test_run_rounds():
    creature1 = Creature("Dragon", 18, 100, [{'number_of_attacks': 1, 'to_hit_bonus': 5, 'damage_roll': '1d10'}])
    creature2 = Creature("Goblin", 12, 20, [{'number_of_attacks': 1, 'to_hit_bonus': 2, 'damage_roll': '1d6'}])
    creature1.target = creature2
    creature2.target = creature1
    run_rounds([creature1, creature2])
    assert creature1.is_alive() == True
    assert creature2.is_alive() == False

def test_creatures_hit_points_random_walk():
    creature1 = Creature("Elder Dragon", 19, 500, [{'number_of_attacks': 1, 'to_hit_bonus': 8, 'damage_roll': '1d10'}])
    creature2 = Creature("Dragon", 18, 150, [{'number_of_attacks': 1, 'to_hit_bonus': 8, 'damage_roll': '1d10'}])
    creature1.target = creature2
    creature2.target = creature1
    run_rounds([creature1, creature2])
    print(creatures_hit_points_random_walk[creature1.name])
    print(creatures_hit_points_random_walk[creature2.name])