# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught 

  def speak(self):
    print(self.name + ", " + self.name + "!\n")

  def display_details(self):
    print("Entry Number: " + str(self.entry))
    print("Name: " + self.name)
    print("Type: " + str(self.types))
    print("Description" + self.description)
    if (self.is_caught == True):
      print("Pikachu has already been caught!\n")
    else: 
      print("Not Caught, yet!\n")

Bulbasaur = Pokemon(1, "Bulbasaur", ["Grass", "Poison"],"For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.", True)
Pikachu = Pokemon(25, "Pikachu", ["Electric"], "When it is angered, it immediately discharges the energy stored in the pouches in its cheeks.", False)
Pidgeot = Pokemon(25, "Pidgeot", ["Normal", "Flying"], "This Pokémon flies at Mach 2 speed, seeking prey. Its large talons are feared as wicked weapons.", False)

Bulbasaur.display_details()
Pikachu.display_details()
Pidgeot.speak()