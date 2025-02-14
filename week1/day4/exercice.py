# Exercice 1 : Les animaux de compagnie
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [(Bengal , Chartreux, Siamois)]

sara_pets = Pets(all_cats)

sara_pets.walk()


# Exercice 2 : Les chiens

class Dog ():
    def _init_(self, og_name, dog_age, dog_weight):
        self.name = dog_name
        self.age = dog_age
        self.weight = dog_weight
    
    def bark(self):
        return(f" {self.name}")
    def run_speed(self)
        return(self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = self.dog.run_speed() * other_dog.weight

        if self_power > other_power :
            return (f"{self.name] is the winner")
        if self_power < other_power :
            return (f"{other_dog_name} is the winner)
        else:
            return "Match nul!"

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Max", 4, 18)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog3))
    

# Exercice 3 : Chiens domestiqués
import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dogs):
        names = [dog.name for dog in dogs] + [self.name]
        print(f"{', '.join(names)} jouent ensemble!")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} fait un tonneau!",
                f"{self.name} se tient sur ses pattes arrières!",
                f"{self.name} te serre la main!",
                f"{self.name} fait le mort!"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} n'est pas encore dressé!")


pet_dog1 = PetDog("Charlie", 4, 22)
pet_dog2 = PetDog("Rocky", 5, 28)

pet_dog1.train()
pet_dog1.do_a_trick()
pet_dog1.play(pet_dog2)


# Exercise 4 : Family

class Family:
    def __init__(self, nom_de_famille, membres):
        self.nom_de_famille = nom_de_famille
        self.membres = membres

    def born(self, **kwargs):
        self.membres.append(kwargs)
        print(f"Félicitations! La famille {self.nom_de_famille} s'agrandit!")

    def is_18(self, name):
        for membre in self.membres:
            if membre['name'] == name:
                return membre['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Famille {self.nom_de_famille}:")
        for membre in self.membres:
            print(membre)

# Création de la famille
famille = Family("Dupont", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

famille.family_presentation()
famille.born(name="Emma", age=1, gender="Female", is_child=True)
famille.family_presentation()


# 5
class TheIncredibles(Family):
    def use_power(self, name):
        for membre in self.membres:
            if membre['name'] == name:
                if membre['age'] < 18:
                    raise Exception(f"{name} est trop jeune pour utiliser son pouvoir!")
                print(f"{membre['name']} utilise son pouvoir: {membre['power']}!")

    def incredible_presentation(self):
        print(f"Voici notre puissante famille {self.nom_de_famille}!")
        super().family_presentation()

# Création de la famille des Indestructibles
indestructibles = TheIncredibles("Indestructibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

indestructibles.incredible_presentation()
indestructibles.use_power("Michael")

# Ajout de Baby Jack
indestructibles.born(name="Baby Jack", age=1, gender="Male", is_child=True, power="unknown", incredible_name="BabyJack")

indestructibles.incredible_presentation()
