# Rock Paper Scissor Game

"""
Program workflow
1. Input from user -Rock Paper Scissor
2. Input from computer 
3. Print the result
4. Show the Win History 

Cases 
1. Rock
    - Rock - Rock  : Tie
    - Rock - Paper : Lose
    - Rock - Scissor : Win

2. Paper
    - Paper - Paper : Tie
    - Paper - Scissor : Lose
    - Paper - Rock    : Win

3. Scissor
    - Scissor - Scissor : Tie
    - Scissor - Rock    : Lose
    - Scissor - Paper   : Win     

"""

import random
import os.path
import csv

user_input = ""
item_list = ["Rock","Paper","Scissor"]

# validating user input wrong input 
def user_choice():  
    no_of_invalid_input = 0
    while True:  
        user_input = input(" Choose from Rock, Paper, Scissor = ")
        if user_input not in item_list:
            no_of_invalid_input =+  1
            if no_of_invalid_input == 3:
                print("Choose Valid input. Exiting the program")
                exit()
            else:
                print("Please Try Again")
                print("No of Attemps left = ", 3 - no_of_invalid_input)
                print()
                continue
        else:
            return user_input        

computer_choice = random.choice(item_list)

var_user_choice = user_choice()
print("User Choice is ", var_user_choice)
print("Computer Choice is ", computer_choice)

no_of_match_tie = 0
no_of_users_wins = 0 
no_of_computer_wins = 0

if var_user_choice == computer_choice:
    print("Match Tie. User and Computer Choose same")
    no_of_match_tie = 1

elif var_user_choice == "Rock":
    if computer_choice == "Paper":
        print("You lost match. Paper covers Rock")
        no_of_computer_wins = 1
    elif computer_choice == "Scissor":
        print("You Won match. Rock smashes Scissor")
        no_of_users_wins = 1
            
elif var_user_choice =="Paper":
    if computer_choice == "Scissor":
        print("You lost match. Scissor cuts Paper")
        no_of_computer_wins = 1
    elif computer_choice == "Rock":
        print("You Won match. Paper covers Rock")
        no_of_users_wins = 1

elif var_user_choice == "Scissor":
    if computer_choice == "Rock":
        print("You lost match. Rock smashes Scissor")
        no_of_computer_wins = 1
    elif computer_choice == "Paper":
        print("You Won match. Scissor cuts Paper")
        no_of_users_wins = 1


def read_history_data():   
    with open('Rock_Paper_Scissor_History.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        read_data = []
        line_count = 1
        for row in csv_reader:
                a = ""    
                if line_count == 1 :
                    a = row[1]
                elif line_count == 2 :
                    a = row[1]
                elif line_count == 3 :
                    a = row[1]
                elif line_count == 4 :
                    a = row[1]
                read_data.append(a) 
                line_count += 1
    return read_data

total_no_of_matches = no_of_users_wins + no_of_computer_wins + no_of_match_tie
    
if os.path.isfile("Rock_Paper_Scissor_History.txt") :
    line_count = 1
    updated_history = read_history_data()

    print("Total number of Match :", int(updated_history[0]) +total_no_of_matches)
    print("Number of Users Win :",  int(updated_history[1])+ no_of_users_wins)
    print("Number of Computer Win :", int(updated_history[2]) + no_of_computer_wins)
    print("Number of Tie matches :", int(updated_history[3]) + no_of_match_tie )
    
    f = open("Rock_Paper_Scissor_History.txt", "w")
    f.write(f"Total number of Match : {int(updated_history[0]) +total_no_of_matches}\n")
    f.write(f"Number of Users Win : {int(updated_history[1])+ no_of_users_wins}\n")
    f.write(f"Number of Computer Win : {int(updated_history[2]) + no_of_computer_wins}\n")
    f.write(f"Number of Tie matches : {int(updated_history[3]) + no_of_match_tie}\n")
    f.close()
else:
    f = open("Rock_Paper_Scissor_History.txt", "w")
    f.write(f"Total number of Match : {total_no_of_matches}\n")
    f.write(f"Number of Users Win : {no_of_users_wins}\n")
    f.write(f"Number of Computer Win : {no_of_computer_wins}\n")
    f.write(f"Number of Tie matches : {no_of_match_tie}\n")
    f.close()























