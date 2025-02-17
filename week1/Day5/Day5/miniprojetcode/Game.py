# Mini Project : Rock Paper Scissors

# part 1: create Game.py

class Game():
    def _init_ (self, user_name):
        self.name = user_name
        
                                            # user select an item
    def get_user_item(self):
        user_item = input.lower("choice one letter : "r" for rock , or "p" for paper, or "s" for scissor")
        if user_item != r or p or s:
            print(f" x + "is not correct"")
            print(user_item)
        else:
            return user_item

                                               #  user select an item
    def get_computer_item(self):
        import random
        list_item = ["r", "p", "s"]
        computer_item = random.choice(list_item)
        return computer_item

                                                # result of game
    def get_game_result(self, user_item, computer_item):
        if (user_item == p and computer_item == r) or (user_item == r and computer_item == s) or (user_item == s and computer_item == p): 
            return win
        if user_item == computer_item:
            return draw 
        if (user_item == r and computer_item == p) or (user_item == s and computer_item == r) or (user_item == p and computer_item == s):
            return lost 

    def play(self):
        user_choice = get_user_item()
        computer_choice = get_computer_item()
        result_game = get_game_result ( user_choice, computer_choice)
        print(f"you are won this game")
        return result_game

    


   

    

        
        
        








    def get_game_result(self, user_item, computer_item):


