import random 

# How to play

    # To choose your answer use; 

    # rock as "1", paper as "2", and scissors as "3"

    # make sure you put a space before your answer

    # to play again re-run this code

computeranswer = random.randint(1,3)

# this is where the computer chooses their answer (rock, paper, or scissors)

useranswer = int(input("Choose rock, paper, or scissors"))

# this is where you, the user chooses your answer

print(computeranswer)

# this prints the computer's answer



# Below is where the different outputs are. The wins, losses, or ties.

if computeranswer ==1: 



    if useranswer ==1:



        print("Tie")



if computeranswer ==2:



    if useranswer ==2:



        print("Tie")



if computeranswer ==3:



    if useranswer ==3:



        print("Tie")



if computeranswer ==2:



    if useranswer ==3:



        print("You Win")



if computeranswer ==2:



    if useranswer ==1:



        print("Computer Wins")



if computeranswer ==3:



    if useranswer ==2:



        print("Computer Wins")



if computeranswer ==1:



    if useranswer ==2:



        print("You Win")

if computeranswer ==3:



    if useranswer ==1:



        print("You Win")

if computeranswer ==1:



    if useranswer ==3:



        print("Computer Wins")
