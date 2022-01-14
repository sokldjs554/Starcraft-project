class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} A unit has been created.".format(name))

        def move(self, location):
            print("[ground unit movement]")
            print("{0} : {1} Move to 1 o'clock. [speed {2}"\
                .format(self.name, location, self.speed))

        def damaged(self, damage):
            print("{0} : {1} took damage.".format(self.name, damage))
            self.hp -=damage
            print("{0} : Current health is 1".format(self.name, self.hp))
            if self.hp <=0:
                print("{0} : destroyed.".format(self.name))

        
class AttackUnit:
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} Attacks the enemy in the 1 o'clock direction. [ATK {2}"\
            .format(self.name, location, self.damage))

#marine
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "marine", 40, 13, 20)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : use a stimpack. (HP 10 decrease)".format(self.name))
        else:
            print("{0} : You can't use Stimpak because you don't have enough stamina.".format(self.name))

#tank
class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "tank", 150, 200, 40)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

         #Not currently in Seize Mode
        if self.seize_mode == False:
             print("{0} : Switch Seize Mode.".format(self.name))
             self.damage *= 2
             self.seize_mode = True

        else: 
            print("{0} : Turn off Seize Mode.".format(self.name))
            self.damage /= 2
            self.seize_mode = False    

#flying function class
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} Fly to 1 o'clock [speed {3}]"\
            .format(name, location, self.flying_speed))

#fly unit
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[air unit movement]")
        self.fly(self.name, location)

#wraith
class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__("wraith", 80, 30, 15)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : Turn off cloaking mode".format(self.name))
            self.clocked = False
        else:
            print("{0} : Turn on cloaking mode".format(self.name))
            self.clocked = True


