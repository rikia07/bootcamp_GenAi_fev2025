# Old MacDonald’s Farm
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            info += f"{animal.ljust(10)} : {count}\n"

        info += "\n    E-I-E-I-O!\n"
        return info

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())

# Expand The Farm
class Farm:
    def _init_(self, farm_name):
        self.name= farm_name
        self.animals = {} 
    
    def get_animal_types(self, animal):
        self.animals.append(animal)
        