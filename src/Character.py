import random


class Character:

    def __init__(self, hit_points):
        self.hit_points = hit_points

    def fight(self, character):
        random_number = random.randint(1, 20)
        if character.hit_points - random_number <= 0:
            character.hit_points = 0
        else:
            character.hit_points -= random_number
