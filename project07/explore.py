'''simon lartey
11/08/2023
CS 152 B
PROJECT_07 '''

import graphicsPlus as gr
import random
import time
# Define a function named 'test1'
def test1():
	win = gr.GraphWin( 'My First Window WhooHoo!', 500, 500 )
	point = gr.Point(100, 200)
	circle = gr.Circle( point, 10 )
	#circle = gr.Circle( gr.Point(100, 200), 10 )
	circle.draw( win )

    # Wait for the user to click the mouse and print the mouse coordinates
	point_2 = win.getMouse()
	print( "X: " + str( point_2.getX() ) + ", Y: " + str( point_2.getY() ) )
     # Close the window
	win.close()

# Define a function named 'test2'
def test2():
    win = gr.GraphWin('MY WINDOW', 500, 500)
    shapes = []
# Enter an infinite loop for interactive drawing
    while True:
        pos = win.checkMouse()
        if pos:
            point = pos  # Create the circle at the position of the mouse click
            circle = gr.Circle(point, 10)
            circle.setFill('blue')
            circle.draw(win)
            shapes.append(circle)
# Check if the user pressed the 'q' key to exit the loop
        key = win.checkKey()
        if key == 'q':
            break  # Exit the loop if the 'q' key is pressed

        time.sleep(0.03)

# Move each circle in random directions
        for shape in shapes:
            change_in_x = random.randint(-10, 10)
            change_in_y = random.randint(-10, 10)
            shape.move(change_in_x, change_in_y)

    # Close the window outside the loop
    win.close()

if __name__ == '__main__':
    test2()
