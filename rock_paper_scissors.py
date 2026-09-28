import random
import time

print("Welcome to the Rock, Paper, Scissors game!")

def play_game():
 #countdown
   
    options = ['rock', 'paper', 'scissors']
    print('rock')
    time.sleep(0.7)
    print('paper')
    time.sleep(0.7)
    print('scissors')
    time.sleep(0.7)
    print('Shoot!')

 #Players input validation
    while True:
        player_choice = input("Enter your choice (rock, paper or scissors): ")
        if player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors (In lowercase).")
            
        else:
            break

            
 #Computer's choice
    computer_choice = random.choice(options)
    print(f'Computer chose {computer_choice}.')

 #Game logic to determine the winner
    if player_choice == computer_choice:
        print(f"It's a tie! Both chose {player_choice}.")
    elif (
        (player_choice =='rock' and computer_choice == 'scissors') or 
        (player_choice == 'paper' and computer_choice == 'rock') or 
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):  
        print(f"You win! {player_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {player_choice}.")

def main():
    player_decision = input("Do you want to proceed? (yes/no): ").lower() 

    if player_decision == 'no':
        print("Goodbye 👋🏽!!")
        return
    elif player_decision == 'yes':
        print("Let's play!!!")
        
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
            
    
    while True:
        play_game()

        proceed = input('Do you want to play again? (yes/no)').lower()
        if proceed == 'yes':
            continue
        elif proceed == 'no':
            print('Thanks for playing! Goodbye ✊🏻')
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            break


if __name__ == '__main__':
    main()

