class GameCharacter:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self,enemy):
        enemy.health -= self.attack_power
        print(self.name ,"attacked", enemy.name)
        print(enemy.name ,"health: ", enemy.health)

    def take_damage(self,damage):
        self.health -= damage
        print(self.name ,"took", damage,"damage")
        print(self.name ,"health: ", self.health)


    def is_alive(self):
        return self.health > 0

    def display(self):
        print("Name: ",self.name)
        print("Health: ",self.health)
        print("Attack Power: ",self.attack_power)



character1 = GameCharacter("Warrior",100,20)
character2 = GameCharacter("Mage",100,20)

print("Initial State")
character1.display()
character2.display()
print("--------------------------")

print("Attacking...")
character1.attack(character2)
character1.attack(character2)
print("--------------------------")
character2.attack(character1)
character2.attack(character1)


    