import random

print("Rock Paper Scissors \n"
      "RULES OF THE GAME \n"
      "Paper vs Scissors = Scissor wins \n"
      "Rock vs Scissor = Rock wins \n"
      "Rock vs Paper = Paper wins \n"
      "START GAME!!!")


choices = ["r", "p", "s"]
startgame = True

while startgame == True:
    player_choice = input("Enter your choice: R for Rock, \n P for Paper, \n S for Scissor \n")
    player_choice = player_choice.lower()
    computer_choice = random.choice(choices)
    

    print("You selected %s" % player_choice)
    print("Computer's choice is %s" % computer_choice)
    print("****checking****")
    
    if (player_choice == computer_choice):
        print("It's a tie")
    elif (player_choice == "s"):
        if (computer_choice == "p"):
            print("Scissors cuts paper, you win!")
        else:
            print("Rock smashes scissors, you loose!")
        startgame = False

    elif player_choice == "r":
        if (computer_choice == "s"):
            print("Rock smashes scissors, you win!")
        else:
            print("Paper covers rock, you loose!")

        startgame = False
    elif (player_choice == "p"):
        if (computer_choice == "R"):
            print("Paper cover's rock, you win!")
        else:
            print("Scissors cuts paper, you loose!")

        startgame = False
    else:
        print("please select a valid imput")
        startgame = True
