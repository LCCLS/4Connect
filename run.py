from connect_four import *

print("""
———————————————————————————————————
Welcome to Connect Four against an AI.
———————————————————————————————————
""")

playing = int(input(
    """If you want to play against an AI yourself press: 1 

If you want to see two AI's play against each other, press: 2

_"""))

if playing == 1:
    difficulty = int(input(
        """Please select a difficulty level from 1 to 7. (7 being the most difficult) """
    ))
    play_game(difficulty)

elif playing == 2:
    skill1 = int(input(
        """
To make the game more interesting, you can select the difficulty level of the two AIs. 
This will determine how "intelligent" the two AIs are. 

Please select a the difficulty level for the first AI from 1 to 7. (7 being the most difficult): 
_"""
    ))
    skill2 = int(input(
        """
Now please select a the difficulty level for the second AI from (1 to 7, where 7 is the most difficult):
_"""
    ))
    two_ai_game(skill1, skill2)
else:
    raise ValueError('Sorry this is not a valid option.')
