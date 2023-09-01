from creature import Creature
from dice_roll import roll_dice

all_walks_creatures_hit_points=[]
random_walk_creatures_hit_points={}

def run_battle_x_times(creatures, x):
    global all_walks_creatures_hit_points
    global random_walk_creatures_hit_points

    if len(creatures) != 2:
        raise ValueError("Only two creature battle possible right now!")
    else:
        for i in range(x):
            run_two_creature_battle(creatures[0], creatures[1])
            all_walks_creatures_hit_points.append(random_walk_creatures_hit_points)
            random_walk_creatures_hit_points={}

def run_two_creature_battle(creature1, creature2):
    reset_creatures_hit_points([creature1, creature2])
    creatures_sorted_by_initiative = roll_initiative([creature1, creature2])
    set_targets_to_next_creature(creatures_sorted_by_initiative)
    run_rounds(creatures_sorted_by_initiative)

def reset_creatures_hit_points(creatures):
    for creature in creatures:
        creature.reset_hit_points()

def run_rounds(creatures):
    combat_over = False
    global random_walk_creatures_hit_points
    for creature in creatures:
        random_walk_creatures_hit_points[creature.name] = [creature.max_hit_points]

    while not combat_over:
        run_one_round(creatures)
        combat_over = do_we_have_peace(creatures)

def do_we_have_peace(creatures):
    for creature in creatures:
        if (creature.is_alive() and creature.target.is_alive()):
            return False
    return True

def run_one_round(creatures):
    for creature in creatures:
        if creature.is_alive():
            creature.attack_with_all_attacks()

    global random_walk_creatures_hit_points
    for creature in creatures:
        random_walk_creatures_hit_points[creature.name].append(creature.hit_points)

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


    