# Exercise 2 : Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_price=0
for name,age in family:
    if age < 3:
    price=0
    elif age<=12:
    price=10
    else:
    price=15

   print(f"{name} doit payer {price}")
   total_price += price

print(f"the family’s total cost for the movies is {total_price}")

# Exercise 3: Zara

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
}

brand["number_stores"] = 2
print(f"Zara clients are {brand['type_of_clothes'])}")
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(f"Dernier concurrent : {brand['international_competitors'][-1]}")
print(f"Couleurs populaires aux US : {brand['major_color']['US']}")
print(f"Nombre de paires clé-valeur : {len(brand)}")
print(f"Clés du dictionnaire : {list(brand.keys())}")

# Exercise 4 : Some Geography
def describe_city(name_city,country):
   print(f"{name_city} is in {country}")
   country="france"
describe_city("paris","france")

# Exercise 5 : Random
use Random
def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Félicitations, c'est le bon nombre")
    else:
        print(f"Dommage ! Votre nombre : {user_number}, Nombre attentu: {random_number}")
user_input = int(input("Entrez un nombre entre 1 et 100 : "))
compare_numbers(user_input)

# Exercise 6 : Let’s create some personalized shirts !
def make_shirt(size, text):
    print(f"Le t-shirt est de taille {size} avec le message : {text}")

make_shirt()
def make_shirt(size="L", text="I love Python"):
    print(f"Le t-shirt est de taille {size} avec le message : {text}")

make_shirt()
make_shirt("M")
make_shirt("S", "Python c'est génial !")
make_shirt(size="XL", text="Code & Chill")

# Exercise 7 : Temperature Advice
import random
def get_random_temp(numbers_degree):
    numbers_degree=random.randint(-10,40)

