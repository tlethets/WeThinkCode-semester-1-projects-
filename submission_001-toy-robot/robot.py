

# TODO: Decompose into functions
def move_forward(size):
    print("* Move Forward "+str(size))

def turn_right(degrees):
    print("* Turn Right "+str(degrees)+" degrees")

def move_square():
    """ This funtion moves the square of size 10 """
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        move_forward(size)
        turn_right(degrees)

def move_rectangle():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        move_forward(length)
        turn_right(degrees)
        move_forward(width)
        turn_right(degrees)

def move_circle():
    """ It moves the circle in various directions """
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        move_forward(length)
        turn_right(degrees)

def square_dancing():
    """ It moves 3 squares in various dirctions """
    print("Square dancing - 3 squares of size 20")
    size = 20
    for i in range(3):
        length = 20
        move_forward(length)
        print("Moving in a square of size 20")
        degrees = 90
        for j in range(4):
            move_forward(size)
            turn_right(degrees)
            

def crop_circles():
    """ This function crops the circle """
    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        move_forward(length)
        print("Moving in a circle")
        degrees = 1
        length = 1
        for k in range(360):
            move_forward(length)
            turn_right(degrees)
            

def move():
    """ Shapes_in_motion - The function moves the shapes """
    move_square()
    move_rectangle()
    move_circle()
    square_dancing()
    crop_circles()

def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
