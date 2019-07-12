from random import randint


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 10000000)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):

        ratio = self.price / self.weight
        if ratio < 0.5:
            return 'Not so stealable...'
        elif ratio < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):

        exp_coef = self.flammability * self.weight
        if exp_coef < 10:
            return '...fizzle'
        elif exp_coef < 50:
            return '...boom!'
        else:
            return '...BABOOM!'


class BoxingGlove(Product):

    def __init__(self, weight=10):
        Product.__init__(self, weight)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif 5 >= self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
