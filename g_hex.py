import turtle, random, math
import ugly_hex as h
import unionfind as u

class Hexagon():

    num_sides = 6
    side_length = 30
    angle_deg = 360 / num_sides
    angle_rad = math.radians(angle_deg)
    radius = math.cos(angle_rad / 2) * side_length
    height = math.sin(angle_rad / 2) * side_length

    def __init__(self, turtle, position, index):

        self.t = turtle
        self.is_played = False
        self.colour = None
        self.position = [position[0], position[1]]
        self.index = index
        self.n_list = []  # neighbour list
        self.tree = []  # path
        self.parent = None
        
        self.centre_x = self.position[0] + Hexagon.side_length / 2
        self.centre_y = self.position[1] - Hexagon.radius
        self.centre = (self.centre_x, self.centre_y)

        # draw hexagon in position
        self.t.penup()
        self.draw_hexagon()

    def draw_hexagon(self):
        self.t.goto(self.position)
        self.t.pendown()
        self.t.setheading(0)
        self.t.right(Hexagon.angle_deg / 2)
        for side in range(Hexagon.num_sides):
            self.t.forward(Hexagon.side_length)
            self.t.right(Hexagon.angle_deg)
        self.t.setheading(0)
        self.t.penup()

    def is_selected(self, mouse_position):
        x = (self.centre[0] - mouse_position[0]) ** 2
        y = (self.centre[1] - mouse_position[1]) ** 2
        distance = math.sqrt(x + y)
        return distance < Hexagon.radius

    def fill_cell(self, turn):
        self.t.penup()
        self.t.goto(self.position)
        if turn % 2 == 0:
            colour = "navy"
        else:
            colour = "lavender"
        self.t.fillcolor(colour)
        self.t.begin_fill()
        self.draw_hexagon()
        self.t.end_fill()
        self.is_played = True
        self.colour = colour

class Board():

    diameter = Hexagon.radius * 2

    def __init__(self, turtle, board_size, starting_position, adj_list):
        self.t = turtle
        self.board_size = board_size
        self.start = starting_position
        self.adj_list = adj_list
        self.moves = 0
        self.board = []
        self.trees = []
        self.sizes = []
        self.draw_board()
        print("trees", self.trees)
        print("adj_list", self.adj_list)

    def draw_board(self):
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                index = [i, j, i * self.board_size + j]
                self.trees.append(index[2])
                self.sizes.append(1)
                row.append(Hexagon(self.t, self.start, index))
                self.start[0] += Board.diameter
            self.start[0] -= Board.diameter * (self.board_size - 1) + (Board.diameter / 2)
            self.start[1] -= (Hexagon.height + Hexagon.side_length)
            self.board.append(row)
        print("sizes", self.sizes)
    
    def select(self, x, y):
        for row in self.board:
            for cell in row:
                if cell.is_selected((x, y)) and not cell.is_played:
                    cell.fill_cell(self.moves)
                    self.check_cell_neighbours(cell)
                    self.win_check()
                    self.moves += 1

    def check_cell_neighbours(self, cell):
        for item in self.adj_list[(cell.index[0], cell.index[1])]:
            nbr_cell = self.board[item[0]][item[1]]
            if nbr_cell.colour == cell.colour:
                u.unite(nbr_cell.index[2], cell.index[2], self.trees, self.sizes)
                print("TREES", self.trees)
                print("SIZES", self.sizes)

    def win_check(self):

        # check is navy player (top and bottom sides of board) won
        for top_cell in self.board[0]:
            for bottom_cell in self.board[-1]:
                if top_cell.colour == "navy" and bottom_cell.colour == "navy" and u.find(top_cell.index[2], bottom_cell.index[2], self.trees):
                    print("Navy player wins!")

        # check if lavender player (right and left sides of board) won
        for row1 in self.board:
            cell = row1[0]
            for row2 in self.board:
                if cell.colour == "lavender" and row2[-1].colour == "lavender" and u.find(cell.index[2], row2[-1].index[2], self.trees):
                    print("Lavender player wins!")
        

def main():
    
    hex = h.make_board()
    adj_list = h.make_adj_list(hex)

    screen = turtle.Screen()
    
    t = turtle.Turtle()
    t.ht()
    t.speed(0)
    
    centre = [-250, 250]
    board = Board(t, len(hex), centre, adj_list)

    screen.onclick(board.select)

    turtle.done()
        
main()
