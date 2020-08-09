import sys
import random
import math


def drawBoard(board, x, y, current_move):
    if current_move == 0:
        print("Initial Board:")
    else:
        print("Current Move : ", current_move)
    print("-------------------")
    for i in range(0, 3):
        for j in range(0, 3):
            left_align = int(math.ceil(5 - len(str(board[i][j]))) / 2)
            if board[i][j] < 0:
                right_align = int(math.floor(6 - len(str(board[i][j]))) / 2)
            else:
                right_align = int(math.floor(5 - len(str(board[i][j]))) / 2)
            print("|", end="")
            if x == i and y == j:
                left_align -= 1
                right_align -= 1
                print("*", end="")
            for k in range(0, left_align):
                print(" ", end="")
            print(board[i][j], end="")
            for k in range(0, right_align):
                print(" ", end="")
            if x == i and y == j:
                print("*", end="")
        print("|")
    print("-------------------")
    print()
	
	


def game(board):
    x = 2
    y = 0
    drawBoard(board, x, y, 0)
    for level in range(1, maxMoves+1):
        temp, moved_to = alpha_beta_max(tempBoard(board), maxMoves - level + 1, x, y, '0', -sys.maxsize, sys.maxsize)
        board, x, y = getDirection(board, moved_to, x, y)
        drawBoard(board, x, y, level)
        if board[x][y] >= minGoal:
            return board[x][y]
    return board[x][y]


def alpha_beta_max(board, depth, alpha, beta, ch, a, b):
    if depth == 0:
        for i in range(0, 4):
            if come_from[i] == ch:
                return board[alpha][beta] + board[alpha + index[i]][beta + indexXY[i]], ch
        return board[alpha][beta], ch
    max_value = -sys.maxsize
    to = ''
    for i in range(0, 4):
        if (0 <= (alpha + index[i]) <= 2) and (0 <= (beta + indexXY[i]) <= 2):
            current_eval, temp = alpha_beta_min(board, depth, alpha + index[i], beta + indexXY[i], go_to[i], a, b)
            if current_eval > max_value:
                max_value = current_eval
                to = temp
            a = max(a, current_eval)
            if b <= a:
                break
    return max_value, to


def alpha_beta_min(board, depth, alpha,beta, ch, a, b):
    indexX = alpha
    indexY = beta
    for i in range(0, 4):
        if come_from[i] == ch:
            indexX += index[i]
            indexY += indexXY[i]
            board[alpha][beta] += board[indexX][indexY]
    old_value = board[indexX][indexY]
    min_value = sys.maxsize
    for i in range(-1, 2):
        board[indexX][indexY] = i
        current_eval, temp = alpha_beta_max(board, depth - 1, alpha, beta, ch, a, b)
        min_value = min(min_value, current_eval)
        b = min(b, current_eval)
        if b <= a:
            break 
        
    board[indexX][indexY] = old_value
    board[alpha][beta] -= old_value
    return min_value, ch


def getDirection(board, move, x, y):
    indexX = x
    indexY = y
    for i in range(0, 4):
        if go_to[i] == move:
            indexX += index[i]
            indexY += indexXY[i]
            board[indexX][indexY] += board[x][y]
            board[x][y] = random.randint(-1, 1)
    return board, indexX, indexY


def tempBoard(board): #copy board 
    temp_board = []
    for i in range(0, 3):
        temp_list = []
        for j in range(0, 3):
            temp_list.append(board[i][j])
        temp_board.append(temp_list)
    return temp_board





print("\n\t\t\t*****************Welcome!*****************\n")
minGoal = int(input('Enter Your Minimal level goal: \n>> '))
maxMoves = int(input('Enter Your Maximum number of moves: \n>>
                     '))
initial_board = [[1, -1,  0],
                 [1,  0,  1],
                 [0,  1, -1]]

index = [-1, 1, 0, 0]
indexXY = [0, 0, -1, 1]
come_from = ['d', 'u', 'r', 'l']
go_to = ['u', 'd', 'l', 'r']
score = game(initial_board)
print('Score :', score)

if score >= minGoal:
    print('Player Wins')
else:
    print('Computer Wins')
