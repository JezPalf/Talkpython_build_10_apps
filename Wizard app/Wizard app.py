import random
import time

from Classes import Wizard, Monster, SmallAnimal, Dragon


def main():
    printHeader()
    gameLoop()


def printHeader():
    print('--------------------')
    print('    Wizard App')
    print('--------------------')
    print()


def gameLoop():

    monsters = [
        SmallAnimal('Toad', 1),
        Monster('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]
    hero = Wizard('Gandolf', 75)


    while True:

        activeMonster = random.choice(monsters)
        print('A {} of level {} has appeard from the woods...\n'.format(activeMonster.name, activeMonster.level))

        cmd = input('Do you [a]ttack, [r]un or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(activeMonster):
                monsters.remove(activeMonster)
            else:
                print('The wizard runs and hides to recover....\n')
                time.sleep(3)
                print('The wizard returns at full strength...\n')

        elif cmd == 'r':
            print('The wizard doubts his power and runs away.\n')
        elif cmd == 'l':
            print('The wizard {} takes a close look around himself and sees: '.format(hero.name))
            for m in monsters:
                print(' * A {} of level {}'.format(m.name, m.level))
        else:
            print('Exiting game')
            break

        if not monsters:
            print('Well done!!!\nYou have defeated all of the monsters!')
            break


if __name__ == '__main__':
    main()

