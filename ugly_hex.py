import random

def make_board():
    size = int(input("Size of board: "))

    # if board size empty set to traditional 11 by 11
    if size == "" or size == 0:
        size = 11

    # creates n by n board
    board = []
    for i in range(size):
        board.append(["__"] * size)

    return board

def make_adj_list(board):
    adj_list = dict()

    # calculates adjacency list for given hex board
    for i in range(len(board[0])):
        for j in range(len(board)):
            adj_list[(i, j)] = []
            if ((i - 1) >= 0) and ((i - 1) <= (len(board[0]) - 1)) and (j >= 0) and (j <= (len(board) - 1)):
                adj_list[(i, j)].append((i - 1, j))
            if ((i - 1) >= 0) and ((i - 1) <= (len(board[0]) - 1)) and ((j + 1) >= 0) and ((j + 1) <= (len(board) - 1)):
                adj_list[(i, j)].append((i - 1, j + 1))
            if (i >= 0) and (i <= (len(board[0]) - 1)) and ((j - 1) >= 0) and ((j - 1) <= (len(board) - 1)):
                adj_list[(i, j)].append((i, j - 1))
            if (i >= 0) and (i <= (len(board[0]) - 1)) and ((j + 1) >= 0) and ((j + 1) <= (len(board) - 1)):
                adj_list[(i, j)].append((i, j + 1))
            if ((i + 1) >= 0) and ((i + 1) <= (len(board[0]) - 1)) and ((j - 1) >= 0) and ((j - 1) <= (len(board) - 1)):
                adj_list[(i, j)].append((i + 1, j - 1))
            if ((i + 1) >= 0) and ((i + 1) <= (len(board[0]) - 1)) and (j >= 0) and (j <= (len(board) - 1)):
                adj_list[(i, j)].append((i + 1, j))

def print_board(board):

    # prints alpha character column indices along top of board
    start_char = ord('A')
    for i in range(len(board[0])):
        print("  ", chr(start_char), end = "")
        start_char += 1
    print("\n")

    # displays board spaces
    # and numeric character row indicies along left side
    # and W's along right side to indicate white player's side
    start_num = 0
    for row in board:
        print("  " * start_num, start_num, end = "  ")
        for cell in row:
            print(cell, end = "  ")
        print('W' + "\n")
        start_num += 1

    # prints a row of B's along the bottom edge
    # to indicate black player's sides of boards
    print("  " * start_num, "   ", end = "")
    for i in range(len(board[0])):
        print('B   ', end = "")
    print("\n\n")
    

def random_move(move_count, board):
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    while board[row][col] != "__":
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - 1)
    if move_count % 2 == 0:
        board[row][col] = " ○"
    else:
        board[row][col] = " ●"

def add_move_adj_list(move, adj_list, board):
    # pass
    return 0
        
def main():
    
    hex = make_board()
    make_adj_list(hex)
    print_board(hex)

    moves = 0
    while moves < len(hex[0]) * len(hex):
        random_move(moves, hex)
        moves += 1
        print_board(hex)

# main()
