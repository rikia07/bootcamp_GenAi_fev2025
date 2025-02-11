# Exercice 1 : Additionner deux nombres
def add_two_numbers(a, b):  
    return a + b  

result1 = add_two_numbers(1, 3)  
print(result1)  

def add_three_number(a,b,c):
    return a + b + c

result = add_three_number(1,5,8)
print(result)

# Exercice 2 : Imprimez une salutation
def greet(name):
    return f"Bonjour, {name}"

result2 = greet("nihel")    
print(result2) 

# fonction check_even_odd
def check_even_odd (a):
    if a % 2 == 0: 
      return "even"
    else :
      return "odd"

result3 = check_even_odd (6)
print(result3)

#  Exercice 4 : Somme des nombres dans une liste
def sum_list(numbers):
    return sum(numbers) 

result4= sum_list([1,5,8,2,8])
print(result4)

# Exercice 5 : Imprimer les jours de la semaine
def print_days():
    days=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    for didi in days:
        print(didi)

#  Exercice 6 : Vérifiez si le nombre est positif, négatif ou nul
def check_sign(a):
    if a > 0 :
        return "positive"
    elif a < 0 :
         return "negative"    
    else:
        return "zero"
result5= check-sign(8)
print(result5)

# Exercise 7 : Repeat a Word
def repeat_word(word, num)
    for _ in range (num)
      print(word)

# a function find_largest
def find_largest(numbers):
    return max(numbers)


      
    