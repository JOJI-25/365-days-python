class GameCharacter:

  def __init__(self, name, health, attack_power):
    self.name = name
    self.health = health
    self.attack_power = attack_power

  def attack(self, other_character):
    if not self.is_alive():
      print(f"{self.name} is defeated and cannot attack!")
      return

    print(f"{self.name} attacks {other_character.name}!")
    other_character.take_damage(self.attack_power)

  def take_damage(self, amount):
    self.health -= amount
    if self.health < 0:
      self.health = 0

    print(f"{self.name} takes {amount} damage.")
    self.display_status()

    if not self.is_alive():
      print(f"{self.name} has been defeated.")

  def is_alive(self):
    return self.health > 0

  def display_status(self):
    print(f"{self.name} Health: {self.health}\n")


wizard1 = GameCharacter("Wizard",200,20)
warlock1 = GameCharacter("Warlock",150,30)

wizard1.display_status()
warlock1.display_status()
wizard1.attack(warlock1)
warlock1.attack(wizard1)
warlock1.attack(wizard1)
warlock1.attack(wizard1)