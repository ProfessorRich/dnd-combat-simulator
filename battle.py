from creature import Creature
from dice_roll import roll_dice

def run_two_creature_battle(creature1, creature2):
    creatures_sorted_by_initiative = roll_initiative([creature1, creature2])
    set_targets_to_next_creature(creatures_sorted_by_initiative)
    run_rounds(creatures_sorted_by_initiative)

def run_rounds(creatures):
    combat_over = False
    while not combat_over:
        for creature in creatures:
            if creature.is_alive():
                creature.attack_with_all_attacks()
        number_alive=0
        for creature in creatures:
            number_alive += creature.is_alive()
        if number_alive <= 1:
            combat_over = True

def roll_initiative(creatures):
    creatures_with_rolls = []
    for creature in creatures:
        initiative_roll=roll_dice('1d20')
        creatures_with_rolls.append((creature, initiative_roll))
    creatures_with_rolls.sort(key=lambda x: x[1], reverse=True)
    sorted_creatures = [creature for creature, initiative_roll in creatures_with_rolls]
    return(sorted_creatures)

def set_targets_to_next_creature(creatures):
    previous_creature = None
    for creature in creatures:
        creature.target = previous_creature
        previous_creature = creature
    creatures[0].target = previous_creature

