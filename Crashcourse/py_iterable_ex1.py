list1= [1,2,3,4]
 for num in list1:
  print(num)
# print out all the values in the list multipliées par 20.
  print(num*20)

# list1= [1,2,3,4]
#     for num in list1:
#   print(num*20)

list2=["Elie", "Tim", "Matt"]
first__lettre=[name[0] for name in list2]
# print(first_lettre)= ["E","T","M"]

list3=[1,2,3,4,5,6]
# opérateur modulo % pour savoir si pairs ou impair
#  if numbre %2 == 0 >> si divisible par 2 >> pairs
# #  if numbre %2!= 0>> si pas divisible par 2 >> impairs
even_values= [num for num in list3 if num %2 == 0 ]
print (even_values)

#  odd_values= [num for num in list3 if num %2 != 0]

list4=[1,2,3,4] 
list5=[3,4,5,6]
both_list= [num for num in list4 if num in list5]
#  Vérifie si num est dans les deux listes
print(both_list)

# new list with each word reversed and in lowercase
# Tu dois :
# Parcourir la liste des mots
# Inverser chaque mot
# Mettre chaque mot en minuscule
# Créer une nouvelle liste contenant ces mots transformés
#  inverser une chaîne de caractères avec [::-1]
list6=["Elie", "Tim", "Matt"]
final_list={word[::-1].lower() for word in list6]
print(final_list) 
# Résultat : ['eile', 'mit', 'ttam']

word1="first"
word2="third"
word_list= [wowo for wowo in word1 if wowo in word2]
print (word_list)

# range(start, stop, step) increment by 1(by default)/starting from 0 by default
all_number= list(range(1,101))
number_12= (numu for numu in all-number if numu %12==0)
print(number_12)
# [12, 24, 36, 48, 60, 72, 84, 96]

# a list with all the vowels removed
word3="amazing"
vowel="aeiouy"
vowel_removed=[lettre for lettre in word3 if lettre not in vowel]
print(vowel_removed)

# Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
value1=[0,1,2]
list_generated= [[value1]]*3
print(list_generated)

# a revoir 
# list_generated = [list(range(10)) for _ in range(10)]

# Affichage sur plusieurs lignes
for sublist in list_generated:
    print(sublist)