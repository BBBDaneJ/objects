
class Player:
    def __init__(self,health,gender,name, defaultWeapon, credits):
        print("Player Object Created")
        self. health=health
        self. gender=gender
        self. name=name
        self.defaultWeapon=defaultWeapon
        self. credits=credits

    def playerHurt(self,damage):
        self.health=self.health-damage
        print("Damage=",damage,"New Health=",self.health)

    def isDead(self):
        if self.health<=0:
            return True
        else:
            return False

p1=Player(100,"F")
p2=Player(0,"M")
print(p1.isDead())
print(p2.isDead())


print(p1.health,p1.gender)
print(p2.health,p2.gender)

p1.health=200
p2.health=p2.health-40
print(p1.health)
print(p2.health) 