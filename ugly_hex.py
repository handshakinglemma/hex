import random

def make_board():
    size = int(input("Size of board: "))

    # if board size empty set to traditional 11 by 11
    if size == "":
        size = 11

    # creates n by n board
    board = []
    for i in range(size):
        board.append(["__"] * size)

    return board

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
    

def random_move(board, move_count):
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    while board[row][col] != "__":
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - 1)
    if move_count % 2 == 0:
        board[row][col] = " ○"
    else:
        board[row][col] = " ●"
        
def main():
    
    hex = make_board()
    print_board(hex)

    moves = 0
    while moves < len(hex) ** 2:
        random_move(hex, moves)
        moves += 1
        print_board(hex)

main()
