# IT IS A DICE  GAME
# PLAYERS SHOULD  MUST BE (2-4)
# WHO ACHEIVE THE MAX SCORE . HE IS THE WINNER OF THE GAME.
# WHEN THE PLAYER GOT 1 IN ROLL BEFORE ACHEIVE THE MAX SCORE . HIS SCORE RETURNS TO 0:
import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players=int(input("enter players between (2-4):"))
    if 2<= players <=4:
        break
    print("please enter valid players")


max_score=50
players_scores=[ 0 for _ in range(players)]

while max(players_scores)<max_score:
    for player_index in range(players):
        print("\n player number", player_index+1 ,"your turn has started")
        print("your total score  is:",players_scores[player_index],"\n")
        current_score=0
        

        while True:
            should_roll=input("would you like to roll type(yes):")
            if should_roll !="yes":
                break
            value=roll()
            if value==1:
                print("you rolledd A 1 ! your turn is done")
                current_score=0
                break
            else:
                current_score+=value
                print("your rolled A:",value)
            print("your score is ",current_score)

            players_scores[player_index]+=value
            print("your total score is:",players_scores[player_index])
            if players_scores[player_index]>50:
                print(player_index,"yoour total score is",players_scores[player_index],"so you are the winner")