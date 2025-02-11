# Create a dictionary by using all the given variables.

# first_name = 'John'
# last_name = 'Doe'
# favorite_hobby = 'Python'
# sports_hobby = 'gym'
# age = 82

user= {first_name:'John',last_name : 'Doe', avorite_hobby: 'Python',sports_hobby: 'gym', age: 82 }

# Print the total duration of the playlist
playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}

# aller dans la liste songs puis sur la durée: 
liste_musique = playlist["songs"]
duration_first_music = playlist ["songs"][0]["duration"]
total=0
for music in playlist["songs"] :
    music_duration= music["duration"]
    total+= music_duration
    print (f"je vais écouter {total}")
    

total_duration= playlist

# Exercise 1
# Create a function average_length_of_words which takes a string as an argument and returns the average length of the words in the string. 
# You can assume that there is a single space between each word and that the input does not have punctuation. The result should be rounded to one decimal place (hint: see round).
# average_length_of_words('only four lett erwo rdss') == 4

Def average_length_of_words(string):
     average_string= string.count()/len(string)
     return average_string

    