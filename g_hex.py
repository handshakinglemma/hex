import turtle, random, math
import ugly_hex as uh

class Hexagon():

    num_sides = 6
    side_length = 30
    angle_deg = 360 / num_sides
    angle_rad = math.radians(angle_deg)
    radius = math.cos(angle_rad / 2) * side_length
    temp = math.sin(angle_rad / 2) * side_length

    def __init__(self, turtle, position):

        self.t = turtle
        self.is_played = False
        self.top = [position[0], position[1]]
        
        self.centre_x = self.top[0] + Hexagon.side_length / 2
        self.centre_y = self.top[1] - Hexagon.radius
        self.centre = (self.centre_x, self.centre_y)

        # draw hexagon in position
        self.t.penup()
        self.t.goto(self.top)
        self.draw_hexagon()

    def draw_hexagon(self):
        self.t.goto(self.top)
        print(self.top)
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
        print("sdf", self.top)
        self.t.penup()
        self.t.goto(self.top)
        print(self.top)
        if turn % 2 == 0:
            self.t.fillcolor("navy")
        else:
            self.t.fillcolor("lavender")
        self.t.begin_fill()
        self.draw_hexagon()
        self.t.end_fill()
        self.is_played = True

class Board():

    radius = Hexagon.radius * 2

    def __init__(self, turtle, board_size, starting_position):
        self.t = turtle
        self.board_size = board_size
        self.start = starting_position
        self.moves = 0
        self.board = []
        self.draw_board()

    def draw_board(self):
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append(Hexagon(self.t, self.start))
                self.start[0] += Board.radius
            self.start[0] -= Board.radius * (self.board_size - 1)
            self.start[0] -= Board.radius / 2
            self.start[1] -= Hexagon.temp
            self.start[1] -= Hexagon.side_length
            self.board.append(row)
    
    def select(self, x, y):
        for row in self.board:
            for cell in row:
                if cell.is_selected((x, y)) and not cell.is_played:
                    cell.fill_cell(self.moves)
                    self.moves += 1

def main():
    
    hex = uh.make_board()
    uh.make_adj_list(hex)

    screen = turtle.Screen()
    
    t = turtle.Turtle()
    t.ht()
    t.speed(0)
    
    centre = [-250, 250]
    board = Board(t, len(hex), centre)

    screen.onclick(board.select)

    turtle.done()
        
main()
