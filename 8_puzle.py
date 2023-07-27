'''
Define move functions
'''
POSITION = 4

# Define a function to print the game board

def print_board(board):
	print("-------------")
	print("| {0} | {1} | {2} |".format(board[0], board[1], board[2]))
	print("-------------")
	print("| {0} | {1} | {2} |".format(board[3], board[4], board[5]))
	print("-------------")
	print("| {0} | {1} | {2} |".format(board[6], board[7], board[8]))
	print("-------------")


def get_actual_position(board):
    for i in range(9):
        if(board[i] == '-'):
            ACTUAL_POSITION = i;
    return ACTUAL_POSITION


# Movedown
def moveDown(board, ACTUAL_POSITION):
    status = False
    if ACTUAL_POSITION not in [6, 7, 8] :
        POSITION = ACTUAL_POSITION + 3
        TEMP_VAL = board[POSITION]
        board[POSITION] = board[ACTUAL_POSITION]
        board[ACTUAL_POSITION] = TEMP_VAL
        status = True
        print_board(board)
    else:
        print('----------------------')
        print('| Impossible to move |')
        print('----------------------')
    return status


# MoveUP
def moveUp(board, ACTUAL_POSITION):
    status = False
    if ACTUAL_POSITION not in [0, 1, 2] :
        POSITION = ACTUAL_POSITION - 3
        TEMP_VAL = board[POSITION]
        board[POSITION] = board[ACTUAL_POSITION]
        board[ACTUAL_POSITION] = TEMP_VAL
        status = True
        print_board(board)
    else:
        print('----------------------')
        print('| Impossible to move |')
        print('----------------------')
    return status


# MoveLeft
def moveLeft(board, ACTUAL_POSITION):
    status = False
    if ACTUAL_POSITION not in [0,3,6]:
        POSITION = ACTUAL_POSITION - 1
        TEMP_VAL = board[POSITION]
        board[POSITION] = board[ACTUAL_POSITION]
        board[ACTUAL_POSITION] = TEMP_VAL
        status = True
        print_board(board)
    else:
        print('----------------------')
        print('| Impossible to move |')
        print('----------------------')
    return status

# MoveRight
def moveRight(board, ACTUAL_POSITION):
    status = False
    if ACTUAL_POSITION not in [2, 5, 8]:
        POSITION = ACTUAL_POSITION + 1
        TEMP_VAL = board[POSITION]
        board[POSITION] = board[ACTUAL_POSITION]
        board[ACTUAL_POSITION] = TEMP_VAL
        status = True
        print_board(board)
    else:
        print('----------------------')
        print('| Impossible to move |')
        print('----------------------')
    return status


# MENU
def menu():
    ACTION = int(input('Where do you want to move : \n'
                       '[1] - LEFT\n'
                       '[2] - RIGHT\n'
                       '[3] - TOP\n'
                       '[4] - DOWN\n'
                       '[5] - View actual board\n'
                       '[6] - Check for goal\n#>'))
    while ACTION not in [1,2,3,4,5,6]:
        print("Bad action ! Please enter action between actions in the list")
        ACTION = int(input('Where do you want to move : \n'
                           '[1] - LEFT\n'
                           '[2] - RIGHT\n'
                           '[3] - TOP\n'
                           '[4] - DOWN\n'
                           '[5] - View actual board\n'
                            '[6] - Check for goal\n#>'))
    return ACTION

# check for Winner
def check(board, goal_board):
    status = True
    for i in range(9):
        if board[i] != goal_board[i]:
            status = False
            break
    return status
# play game

# RUN The program
# board = [8, 6, 5, 3, '-', 1, 7, 2, 4]
board = [4, 2, 3, 1, '-', 5, 8, 6, 7]
# board = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,'-' ,8]
goal_board = [1, 2, 3, 4, 5, 6, 7, 8, '-']
print('INITIAL BOARD')
print_board(board)
print('GOAL BOARD')
print_board(goal_board)
# print(check(goal_board, goal_board))
while not check(board, goal_board):
    POSITION = get_actual_position(board)
    action = menu()
    if action == 1:
        moveLeft(board, POSITION)
    elif action == 2:
        moveRight(board, POSITION)
    elif action == 3:
        moveUp(board, POSITION)
    elif action == 4:
        moveDown(board, POSITION)
    elif action == 5:
        print('INITIAL BOARD')
        print_board(board)
    elif action == 6:
        print('GOAL BOARD')
        print_board(goal_board)
else:
    print("Game Over, you have win !")
    # print(get_actual_position(board))
