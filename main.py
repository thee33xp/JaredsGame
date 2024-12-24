"""
    Project/Main
    
    Version 1 - Jared's Game 

    Tutorial for pygame

    My advice is to try and read it like a logical book, while/if/elif/else statements are conditional 
    while this is true, or false: > do action> if action is done> do next action> else: if all actions are done and conditions met>
    do else: 
"""
from src.injen import Game_Engine #we're calling our Game_Engine from the file named "injen.py" in the folder called"src"
if __name__ == "__main__":
    main = Game_Engine()  # we call our Game_Engine Class and refer to it as main
    main.Event_Loop() # we run our Event_Loop from the Game_Engine to run the actual game