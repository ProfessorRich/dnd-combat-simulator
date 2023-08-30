import pytest
from dice_roll import roll_dice

def test_roll_dice():
    # we test if the result is within the expected range
    result = roll_dice('2d6')
    assert 2 <= result <= 12

    result = roll_dice('1d10')
    assert 1 <= result <= 10

    result = roll_dice('3d4')
    assert 3 <= result <= 12