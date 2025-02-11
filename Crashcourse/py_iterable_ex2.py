# Exercice 2 : Dictionnaire
# 1
list1=[("name", "Elie"), ("job", "Instructor")]
# dictionary
dict_list= dict(list1)
print(dict_list)

# 2
list2=["CA", "NJ", "RI"]
list3=["California", "New Jersey", "Rhode Island"]
list_dict=dict (zip(list2, list3))
print(list_dict)

list4= ['a','e','i','u','o','y']
vowel_dict= {mimi :0 for mimi in list4 }
print (vowel_dict)

# fromkeys
list4= ['a','e','i','u','o','y']
y=0
dict_list=dict.fromkeys(list4,y)
print(dict_list)

list5= range(1,27)
