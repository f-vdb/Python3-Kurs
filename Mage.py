


import random
import time

TIME_DURATION_SHORT = 1
TIME_DURATION_LONG = 2

def show_abilitys():
    print("choose one Ability")
    print("1 Ember  5MP      2 Aqua 5MP      3 Thunder  10MP")
    print("4 Heal  10MP      5 Resist 0MP")
    print("")
    print("Type the number for the Ability")
    while True:
        try:
            att = int(input(""))
            if att < 0:
                print("type one of the listed numbers")
            elif att > 5:
                print("type one of the listed numbers")
            else:
                return att
        except:
            print("Type in a real number")

class Mage():
    '''Attempt to model an RPG'''

    def __init__ (self, name, mp, hp, zp, ip):
        self.name = name
        self.mp = mp
        self.hp = hp
        self.zp = zp
        self.ip = ip
        self.dp = 0

    # Methods
    def lose_hp(self,damage):
        '''the Mage getting damage'''
        print(self.name.title() + " lost", damage, "hp")
        self.hp = self.hp - damage

    # Attacks
    def use_ember(self):
        ''' The Mage use the attack ember'''
        if self.mp < 5:
            print("not enough mp")
            dmg = 0
        elif self.mp > 4:
            print(self.name.title() + " use 5 mp to use Ember")
            self.mp = self.mp - 5
            dmg = 5
        return dmg

    def use_aqua(self):
        ''' The Mage use the attack aqua'''
        if self.mp < 5:
            print("not enough mp")
            dmg = 0
        elif self.mp > 4:
            print(self.name.title() + " use 5 mp to use Aqua")
            self.mp = self.mp - 5
            dmg = 5
        return dmg

    def use_thunder(self):
        ''' The Mage use the attack thunder '''
        if self.mp < 10:
            print("not enough mp")
            dmg = 0
        elif self.mp > 9:
            print(self.name.title() + " use 10 mp to use Thunder")
            self.mp = self.mp - 10
            dmg = 8
        return dmg

    def use_heal(self):
        ''' The Mage use the ability heal '''
        if self.mp < 10:
            print("not enough mp")
        elif self.mp > 9:
            print(self.name.title() + " use 10 mp to use Heal")
            self.mp = self.mp - 10
            self.hp = self.hp + 20
            print(self.name.title() + " heal himself by 20 hp")

    def use_resist(self):
        ''' The Mage use the ability resist '''
        print(self.name.title() + " use resist.")
        print(self.name.title() + " defense increase by 2")
        self.dp = self.dp + 2

my_mage = Mage("Merlin", 500, 100, 5, 10)
random_enemy1 = Mage("Voldemord", 500, 150, 4, 9)
random_enemy2 = Mage("Gargamel", 500, 90, 6, 11)

print("There is an enemy at the tall gras")
time.sleep(TIME_DURATION_SHORT)
print("*epic Battle Theme*")
time.sleep(TIME_DURATION_SHORT)
enemy = random.choice([random_enemy1,random_enemy2])
print(enemy.name, "appears")
time.sleep(TIME_DURATION_SHORT)

enemy_hp = enemy.hp

if enemy.ip > my_mage.ip:
    print(enemy.name, "starts")
    print("")
    time.sleep(TIME_DURATION_LONG)
    enemy.use_resist()

elif enemy.ip < my_mage.ip:
    print(my_mage.name, "starts")

while True:
    time.sleep(TIME_DURATION_SHORT)
    '''current status is shown'''
    print("")
    print("your current hp is", my_mage.hp)
    print("your current mp is", my_mage.mp)
    print("")
    time.sleep(TIME_DURATION_SHORT)

    '''Battle'''
    '''Player turn'''
    att = show_abilitys()
    if att == 1:
        dmg = my_mage.use_ember()
        damage = my_mage.zp + dmg - enemy.dp
        if damage < 0:
            damage = 0
        time.sleep(TIME_DURATION_SHORT)
        enemy.lose_hp(damage)
    elif att == 2:
        dmg = my_mage.use_aqua()
        damage = my_mage.zp + dmg - enemy.dp
        if damage < 0:
            damage = 0
        time.sleep(TIME_DURATION_SHORT)
        enemy.lose_hp(damage)
    elif att == 3:
        dmg = my_mage.use_thunder()
        damage = my_mage.zp + dmg - enemy.dp
        if damage < 0:
            damage = 0
        time.sleep(TIME_DURATION_SHORT)
        enemy.lose_hp(damage)
    elif att == 4:
        my_mage.use_heal()
    elif att == 5:
        my_mage.use_resist()

    if enemy.hp < 1:
        print("")
        print(enemy.name,"is beaten")
        break

    if enemy.dp == 2:
        enemy.dp = 0
        print("")
        print(enemy.name.title() + "'s defense is 0 again")
        time.sleep(TIME_DURATION_SHORT)

    '''Enemy turn'''
    print("")
    time.sleep(TIME_DURATION_LONG)
    print("Enemy turn")
    time.sleep(TIME_DURATION_SHORT)
    '''Enemy choose what attack he use'''
    if enemy_hp > enemy.hp - 10 and enemy.dp == 0:
        bot_att = int(random.choice([1,2,3,5]))
    elif enemy_hp > enemy.hp - 10 and enemy.dp == 2:
        bot_att = int(random.choice([1,2,3]))
    elif enemy_hp < enemy.hp - 10 and enemy.dp == 0:
        bot_att = int(random.choice([1, 2, 3, 4, 5]))
    elif enemy_hp < enemy.hp - 10 and enemy.dp == 2:
        bot_att = int(random.choice([1, 2, 3, 4]))
    '''Enemy use the attack'''
    if bot_att == 1:
        dmg = enemy.use_ember()
        damage = enemy.zp + dmg - my_mage.dp
        if damage < 0:
            damage = 0
        time.sleep(TIME_DURATION_SHORT)
        my_mage.lose_hp(damage)
    elif bot_att == 2:
        dmg = enemy.use_aqua()
        damage = enemy.zp + dmg - my_mage.dp
        if damage < 0:
            damage = 0
        time.sleep(TIME_DURATION_SHORT)
        my_mage.lose_hp(damage)
    elif bot_att == 3:
        dmg = enemy.use_thunder()
        damage = enemy.zp + dmg - my_mage.dp
        if damage < 0:
            damage = 0
        time.sleep(TIME_DURATION_SHORT)
        my_mage.lose_hp(damage)
    elif bot_att == 4:
        enemy.use_heal()
    elif bot_att == 5:
        enemy.use_resist()

    '''Death if hp is 0'''
    if my_mage.hp < 1:
        print("")
        print(my_mage.name,"fainted")
        break

    if my_mage.dp == 2:
        my_mage.dp = 0
        print("")
        print(my_mage.name.title() + "'s defense is 0 again")
        time.sleep(TIME_DURATION_SHORT)
