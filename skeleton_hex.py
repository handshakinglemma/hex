import turtle, random, math

class Hexagon():

    # class attributes here
    # class attirbutes are information that is applicable to every
    # single instance of the class
    # to go back to our t-shirt factory example: every t-shirt has
    # two sleeves
    # an example of a class attribute is:
    # num_sides = 6

    # I'm leaving these class attributes here, since they have to do
    # with the fiddly arithmetic. You will need to add a few more.
    angle_deg = 360 / num_sides
    angle_rad = math.radians(angle_deg)
    radius = math.cos(angle_rad / 2) * side_length
    height = math.sin(angle_rad / 2) * side_length

    def __init__(self, turtle, position):

        # instance attributes here
        # instance attributes are information that is specific
        # to a specific instance of the class
        # from our t-shirt example: each t-shirt could be a different
        # colour
        # an example of an instance attribute is:
        # self.t = turtle

    # I left this method untouched, since it's kind of fiddly
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

    # use the distance function to calculate if the click was inside
    # the radius of the hexagon or not
    def is_selected(self, mouse_position):
        

    # this method should contain the code to fill the cell with colour
    def fill_cell(self, turn):
        

class Board():

    diameter = Hexagon.radius * 2

    def __init__(self, turtle, board_size, starting_position):

        # fill in some instance attributes and any code you need
        # to set your board up

    # I left the draw method untouched again, since it is again
    # somewhat fiddly (it's just arithmetic, but I already did it,
    # so no need for you to redo it)
    def draw_board(self):
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append(Hexagon(self.t, self.start))
                self.start[0] += Board.diameter
            self.start[0] -= Board.diameter * (self.board_size - 1) + (Board.diameter / 2)
            self.start[1] -= (Hexagon.height + Hexagon.side_length)
            self.board.append(row)

    # this method should get each hexagon to check whether or not
    # it has been clicked
    def select(self, x, y):

def main():

    screen = turtle.Screen()
    
    t = turtle.Turtle()
    t.ht()
    t.speed(0)
    
    # make an instance of your board here

    screen.onclick(board.select)

    turtle.done()
        
main()
