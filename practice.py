#marine : attack unit, soldier, can shoot

name = "marine" # unit name
hp = 40 #unit health
damage = 5 #unit combat power

print("{0} unit is created.".format(name))
print("health {0}, combat power {1}\n".format(hp, damage))

# tank : attack unit, can shoot pho, normal mode, siege mode

tank_name = "tank"
tank_hp = 200
tank_damage = 40

print("{0} unit is created.".format(tank_name))
print("health {0}, Striking power {1}\n".format(tank_hp, tank_damage))

tank2_name = "tank"
tank2_hp = 200
tank2_damage = 40

print("{0} unit is created.".format(tank2_name))
print("health {0}, Striking power {1}\n".format(tank2_hp, tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} Attacks the enemy in the 2 o'clock direction [Striking power {2}]".format(\
        name, location, damage))

attack(name, "1 o'clock", damage)
attack(tank_name, "2 o'clock", tank_damage)
attack(tank2_name, "2 o'clock", tank2_damage)



