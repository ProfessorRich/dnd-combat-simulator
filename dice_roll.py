import random

def roll_dice(dice_string):
    num_dice, num_sides = map(int, dice_string.split('d'))

    roll_total=0
    for _ in range(num_dice):
        roll_total += random.randint(1, num_sides) 
    return roll_total