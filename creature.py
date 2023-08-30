from dice_roll import roll_dice

class Creature:
    def __init__(self, name, armor_class, max_hit_points, attacks, hit_points=None, ability_scores=None, immunities=None, resistances=None, vulnerabilities=None):
        self.name=name
        self.armor_class=armor_class
        self.max_hit_points=max_hit_points
        self.attacks=attacks
        self.hit_points=hit_points if hit_points is not None else max_hit_points
        self.ability_scores=ability_scores if ability_scores is not None else {'str':10,'dex':10,'con':10,'int':10,'wis':10,'cha':10}
        self.immunities=immunities if immunities is not None else {}
        self.resistances=resistances if resistances is not None else {}
        self.vulnerabilities=vulnerabilities if vulnerabilities is not None else {}

    def is_alive(self):
        return self.hit_points > 0
    
    def take_damage(self, damage):
        self.hit_points -= damage

    def attack(self, target):
        for attack in self.attacks:
            counter = 0
            while counter < attack['number_of_attacks']:
                if self.does_attack_hit(attack['to_hit_bonus'], target):
                    #hit
                    self.do_damage(attack['damage_roll'], target)
                counter += 1
    
    def does_attack_hit(self, to_hit_bonus, target):
        roll_to_hit = roll_dice('1d20')
        total_hit_roll = roll_to_hit + to_hit_bonus
        return total_hit_roll >= target.armor_class
    
    def do_damage(self, damage_roll, target):
        target.take_damage(roll_dice(damage_roll))