print("Welcome to Tic-Tac-Toe")
choice = input('Choose your symbol: Type "x" for ❌ and "o" for ⭕\n')
if choice.lower() == "x":
    print("You are player 1")
elif choice.lower() == "o":
    print("You are player 2")
else:
    print("Error! Provide a valid choice.")
num = [n for n in range(9)]


def display_board():
    print(f"  {num[0]}  |  {num[1]}  |  {num[2]}\n __________________")
    print(f"  {num[3]}  |  {num[4]}  |  {num[5]}\n __________________")
    print(f"  {num[6]}  |  {num[7]}  |  {num[8]}")


def check_winner(num):
    if num[0] == num[1] == num[2] or \
            num[3] == num[4] == num[5] or \
            num[6] == num[7] == num[8] or \
            num[0] == num[4] == num[8] or \
            num[0] == num[3] == num[6] or \
            num[1] == num[4] == num[7] or \
            num[2] == num[4] == num[6] or \
            num[2] == num[5] == num[8]:
        return True


display_board()
print("Instruction:\nEnter the number as display above to choose your position when your turn comes."
      "Numbers should be between 0 to 8."
      "Example: If you choose number 4 then your chosen symbol will replace the number 4 in the display board."
      "Let's begin!!!")
is_continue = True
player_1 = True
turn_count = []
while is_continue:
    if player_1:
        print("Player 1, it's your turn!")
        try:
            num_choice = int(input("Enter your number: "))
        except ValueError:
            print('Please provide an integer between 0 to 8')
        if num_choice in num:
            try:
                num[num_choice] = "❌"
            except IndexError:
                print("Error! You have chosen an invalid input.")
            except ValueError:
                print("Error! You have chosen an invalid input.")
        turn_count.append("|")
        display_board()
        player_1 = False
        is_won = check_winner(num)
        if is_won:
            is_continue = False
            print('Player 1 has won!!!! 🤩')
            break
        if len(turn_count) == 9:
            is_continue = False
            print("It's a draw!!! 😊")
            break
    if not player_1:
        print("Player 2, now your turn!")
        try:
            num_choice = int(input("Enter your number: "))
        except ValueError:
            print('Please provide an integer between 0 to 8')
        if num_choice in num:
            try:
                num[num_choice] = "⭕"
            except IndexError:
                print("Error! You have chosen an invalid input.")
        turn_count.append("|")
        display_board()
        player_1 = True
        is_won = check_winner(num)
        if is_won:
            is_continue = False
            print('Player 2 has won!!!! 🤩')



