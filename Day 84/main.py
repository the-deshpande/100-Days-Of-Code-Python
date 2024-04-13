from data import graph, board, logo

PLAYER = {
    True: 'O',
    False: 'X'
}


def evaluate() -> int:
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == PLAYER[True]:
                return 10
            elif board[i][0] == PLAYER[False]:
                return -10

        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == PLAYER[True]:
                return 10
            elif board[0][i] == PLAYER[False]:
                return -10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == PLAYER[True]:
            return 10
        elif board[0][0] == PLAYER[False]:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == PLAYER[True]:
            return 10
        elif board[0][2] == PLAYER[False]:
            return -10

    return 0


def moves_left() -> bool:
    for i in board:
        for j in i:
            if j == ' ':
                return True
    return False


print(logo)
turn = True

print(graph())
while True:
    player_choice = list(map(int, input("Enter your choice (left-top): ").split('-')))

    if player_choice[0] not in [0, 1, 2] and player_choice[1] not in [0, 1, 2]:
        print("Incorrect Choice!")
        continue

    if board[player_choice[0]][player_choice[1]] != ' ':
        print("The position is already filled!")
        continue

    board[player_choice[0]][player_choice[1]] = PLAYER[turn]

    curr_score = evaluate()
    if curr_score < 0:
        print("You won!")
        print(graph())
        break
    elif curr_score > 0:
        print("You lost!")
        print(graph())
        break
    else:
        if not moves_left():
            print("It is a tie")
            print(graph())
            break

    turn = not turn
    print(graph())
