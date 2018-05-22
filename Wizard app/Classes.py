import random

class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Monster: {} of level {}'.format(
            self.name, self.level
        )

    def defensiveRoll(self):
        return random.randint(1, 12) * self.level


class Wizard(Monster):

    def attack(self, monster):
        print('The wizard {} attacks the {}'.format(
            self.name, monster.name
        ))

        myRoll = self.defensiveRoll()
        monsterRoll = monster.defensiveRoll()

        print('You rolled a {}'.format(myRoll,))
        print('The {} rolled a {}'.format(monster.name, monsterRoll))

        if myRoll >= monsterRoll:
            print('The Wizard is victorious over the {}.\n'.format(monster.name))
            return True
        else:
            print('The wizard was defeated\n')
            return  False


class SmallAnimal(Monster):

    def defensiveRoll(self):
        baseRoll = super().defensiveRoll()
        return baseRoll / 2

class Dragon(Monster):
    def __init__(self, name , level, scaliness, breathsFire):
        super().__init__(name, level)
        self.breathsFire = breathsFire
        self.scaliness = scaliness

    def defensiveRoll(self):
        baseRoll = super().defensiveRoll()
        fireModifier = 5 if self.breathsFire else 1
        scaleModifier = self.scaliness / 10

        return baseRoll * fireModifier * scaleModifier