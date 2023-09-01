import pytest
from battle import run_two_creature_battle, roll_initiative, set_targets_to_next_creature, run_rounds, run_battle_x_times, reset_creatures_hit_points, random_walk_creatures_hit_points, all_walks_creatures_hit_points
from creature import Creature

def test_run_battle_x_times():

    creature1 = Creature("Goblin", 15, 7, [{'number_of_attacks': 1, 'to_hit_bonus': 4, 'damage_roll': '1d6'}])
    creature2 = Creature("Orc", 13, 15, [{'number_of_attacks': 1, 'to_hit_bonus': 5, 'damage_roll': '1d12'}])

    run_battle_x_times([creature1, creature2], 1000)

    import matplotlib.pyplot as plt
    test_number = 0
    colours = {'Orc': 'b', 'Goblin': 'r'}

    for random_walk in all_walks_creatures_hit_points:
        test_number += 1
        for key, values in random_walk.items():
            plt.plot(values, label=(str(key) + " " + str(test_number)), color=colours[key])
    plt.xlabel('Round')
    plt.ylabel('Hit Points')
    plt.show()

    print(all_walks_creatures_hit_points)