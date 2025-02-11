# Exercice 1 : Bonjour le monde
    # wai 1
print(("hello world\n")*4)
    # wai 2
for hello in range(4):
    print("hello word")

#  Exercise 2 : Some Math
result =(99**3)*8
print(result)

# Exercise 3 : What’s your name ?
my_name="riri"
user_name=input("what is your name?")
if user_name == my_name:
    print("yeah ! we have the same name")
else:
    print("not the same name, i am sad")

# Exercise 4 : Tall enough to ride a roller coaster
user_height= int(input("what is your height (centimeters? "))
if user_height >145:
    print("your enough tall to ride")
else:
    print("sorry, you need to grow some more to ride")

# Exercise 5 : Favorite Numbers
my_fav_numbers={7,10}
my_fav_numbers.add(15)
my_fav_numbers.add(26)
my_fav_numbers.remote(max(my_fav_numbers))

friend_fav_numbers={5,8,12}
our_fav_numbers= my_fav_numbers.union(friend_fav_numbers)

# Exercise 6: Tuple
tuple_value=(25,55,69)
# it is not possible to add more integer to the tuple

# Exercise 7: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove(banana)
basket.remove(Blueberries)
basket.add(kiwi)
basket.insert(0,Apples)
x= basket.count("Appels")
print (x)
basket.clear()
print(basket)

# Exercise 8 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
sandwich_orders.remove(Pastrami sandwich)
finished_sandwiches=[]
while sandwich_orders:
    sandwich_current=sandwich_orders.opp(0)
    print(f"i made your {sandwich_current}")
    finished_sandwiches.append(sandwich_current)

print()


