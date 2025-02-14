# Exercice 1 : Les chats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1= Cat("pitou",2) 
cat2= Cat("fufu", 3)
cat3 = Cat("doudou",6)

def fin_oldest_cat(self, cats):
    oldest_cat=cats[0]






# Exercise 2 : Dogs
class Dog:
    def _init_(self, name_dog, height_dog):
       self.name = dog_name
       self.height = dog_height

    def Bark(self):
        print(f"{self.name} goes woof")
    
    def Jump(self, x):
        x= self.height*2
        print(f"{self.name} jumps {x} cm high!")

davids_dog= Dog("Rex", 50)
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.Bark()
davids_dog.Jump()


sarahs_dog= Dog("Teacup", 20)
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.Bark()
sarahs_dog.Jump()

bigger-dog = davids_dog if davids_dog.height > sarahs_dog.height
  else sarahs_dog if sarahs_dog.height > davids_dog.height
print(f"the bigger dog is {bigger_dog.name}.")


# Exercise 3 : Who’s the song producer ?
class Song:
    def _init_(self, lyrics):
         self.lyrics = lyrics

        def sing_me_a_song (self):
            for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sin_me_song ()

# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def _init_(self, zoo_name):
         self.name = zoo_name
         self.animals =[]
    
    def add_animals(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("animals in the zoo : " , self.animals)
    
    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        sorted_animals= sorted(self.animals)
        grouped_animals={}
        
        for animal in sorted_animals:
            first_letter=animal [0]
                 if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)

        return grouped_animals

    def get_groups(self):
        grouped_animals = self.sort_animals()
        for letter, animals in grouped_animals.items():
            print(f"{letter}: {animals}")

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Monkey")
ramat_gan_safari.add_animal("Bear")

ramat_gan_safari.get_animals()
# vente de Monkey
ramat_gan_safari.sell_animal("Monkey")
# après la vente
ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()


    






