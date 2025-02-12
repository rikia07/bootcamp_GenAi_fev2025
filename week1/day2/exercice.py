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
def get_random_temp():
    return random.randint(-10,40)
get_random_temp()
print(get_random_temp())

def main():
    temp=get_random_temp()
print(f"La température actuelle est de {temp} degrés Celsius.")
main()

    if temp < 0:
        print("il fait très froid !")
    elif 0 <= temp <= 16:
        print("Il fait frais !")
    elif 16 < temp <= 23:
        print("agréable température aujourd'hui !")
    elif 24 <= temp <= 32:
        print("Il fait chaud !")
    else:
        print("Canicule ! ")

main()

# Hiver : entre -10°C et 16°C
# Printemps : entre 5°C et 25°C
# Été : entre 20°C et 40°C
# Automne : entre 0°C et 20°C

get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring":
        return random.randint(5, 25)
    elif season == "summer":
        return random.randint(20, 40)
    elif season == "autumn" or season == "fall":
        return random.randint(0, 20)
    else:
        return random.randint(-10, 40)

def main():
    season=input(f"entrer une saison:")
    temp= get_random_temp ()


get_random_temp(season)

# Exercise 8 : Star Wars Quiz
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_question():
    correct_answer=0
    incorrect_answer=0
    wrong_answer=[]

    for item in data:
        user_answer=input(item["question"] + " ")
        if user_answer.strip().lower() == item["answer"]:
            print("correct!")
            correct_answer += 1
        else:
            print(f"Wrong! The correct answer was: {item['answer']}")
            incorrect_answers += 1
            wrong_answers.append({
                question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })
return correct_answers, incorrect_answers, wrong_answers

def show_results(correct, incorrect, wrong_answers):
    print("\n Quiz Finished! ")
    print(f" Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

    if incorrect > 0:
        print("\nHere are the questions you got wrong:")
        for item in wrong_answers:
            print(f"- Question: {item['question']}")
            print(f" Your answer: {item['your_answer']}")
            print(f"  Correct answer: {item['correct_answer']}\n")

    if incorrect > 3:
        print(" You had more than 3 wrong answers. Try again!")
        play_quiz()

def play_quiz():
    correct, incorrect, wrong_answers = ask_questions()
    show_results(correct, incorrect, wrong_answers)

play_quiz()







