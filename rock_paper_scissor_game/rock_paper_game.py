import random

def main():
    # staring the game
    print("\n🎮 Welcome to Rock, Paper, Scissors!\n")

    # options to choose from 
    options = ["rock","paper","scissor"]
    emoji_map = {"rock": "🪨", "paper": "📄", "scissor": "✂️"} 
    user_score = 0
    computer_score = 0
    draw = 0

    while True:
        # getting user choice 
        user_choice = get_user_choice(options)
        print(f"\nUser Choice: {user_choice.capitalize()} {emoji_map[user_choice]}\n")

        # generating computer choicee
        computer_choice = generate_computer_choice(options)
        print(f"💻 Computer chose: {computer_choice.capitalize()} {emoji_map[computer_choice]}\n")
        
        # declaring the winner
        winner = declaring_winner(user_choice,computer_choice)

        if winner == "draw":
            print("🤝 It's a draw!\n")
            draw += 1
        elif winner == "user":
            print("🎉 You win!\n")
            user_score += 1
        else:
            print("😢 Computer wins!\n")
            computer_score += 1
        
        print(f"📊 Score => You : {user_score} , Computer: {computer_score}, Draw: {draw}")

        # asking the user if they want to play again
        if not ask_play_again():
            print("\n🏁 Game Over!")
            print(f"\n🧾 Final Score:\nYou: {user_score}\nComputer: {computer_score}\nDraws: {draw}")
            break       

# getting user choice
def get_user_choice(options):
    while True:
        user_choice = input("Choose rock, paper or scissor: ").strip().lower()
        if user_choice in options:
            return user_choice
        # if user choose invalid  option
        else:
            print("❌ Invalid choice. Try again.")


# generating computer choice
def generate_computer_choice(options):
    return random.choice(options)

# comparing user choice and computer choice to declare winner
def declaring_winner(user,computer):
    if user == computer:
        return "draw"
    elif(user == "rock" and computer == "scissor") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissor" and computer == "paper"):
        return "user"
    else:
        return "computer"

# to ask if the user want to play again
def ask_play_again():
    while True:
        play_again = input("\n🔁 Do you want to play another round? (yes/no): ").strip().lower()

        if play_again in ["yes","y"]:
            return True
        elif play_again in ["no","n"]:
            return False
        else:
            print("❌ Invalid Input. Please enter yes or no.")


main()       