from Character import Character


class Fighter(Character):

    def __repr__(self):
        return f'The fighter has {self.hit_points}'
