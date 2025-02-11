# Challenge 1
user_number=int(input("enter a number: "))
user_lengh= int(input("entera lengh: "))
list_of_multiple_number=[]
for i in range(1,lengh+1):
    list_of_multiple_number.append(number*i)
    print(list_of_multiple_number)

# Challenge 2
word_user=input("enter word")
user_writing=[]
previous_char=None

for char in word_user:
    if char != previous_char:
        user_writing.append(char)
        previous_char = char

print("résultat:"".join(user_writing)")

if not word_user:
    print("no word")


