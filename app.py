current_player = "X"
stop = False
board = [
    "-","-","-",
    "-","-","-",
    "-","-","-",
]

def play(position):
    global current_player
    # your code here
    position=int(position)
    if position <0:
        print("Invalid Position")
        return
    if position >8:
        print("Invalid Position")
        return
    if board[position]=='-':
        board[position]=current_player
    else:
        print("Position taken")
        return
    return

def check_for_winner():
    # your code here
    winning_combinations=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(len(winning_combinations)):
        current_combination=[]
        current_combination.append(board[winning_combinations[i][0]])
        current_combination.append(board[winning_combinations[i][1]])
        current_combination.append(board[winning_combinations[i][2]])
        if "-" not in set(current_combination):
            if len(set(current_combination)) <= 1:
                return True
    return False

def new_game():
    # your code here
    global current_player
    global stop
    global board

    current_player = "X"
    stop = False
    board = [
        "-","-","-",
        "-","-","-",
        "-","-","-",
    ]
    return

def print_board():
    print(f"""
    Current board ({current_player} turn):

    [{board[0]}] [{board[1]}] [{board[2]}]
    [{board[3]}] [{board[4]}] [{board[5]}]
    [{board[6]}] [{board[7]}] [{board[8]}]
    """)

while stop == False:
    command = input("What do you want?: ")
    if command == "play":
        position = input("Position:")
        play(position)
        if check_for_winner():
            print("There is a winner")
            new_game()
        else:
            if current_player=="X":
                current_player="O"
            else:
                current_player="X"
        print_board()
    if command == "reset":
        new_game()
    if command == "stop":
        stop = True
    # add commands here (if needed)
