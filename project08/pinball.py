'''Simon Lartey
CS152B
11/07/2023
'''

import physics_objects as pho
import graphicsPlus as gr
import collision
import random

def buildObstacles(win):
    # Create all of the obstacles in the scene and put them
    # in a list
    # Each obstacle should be a Thing (e.g. Ball, Block, other)
    # You might want to give one or more obstacles an elasticity > 1
    # Return the list of Things

    ball1 = pho.Ball(win, radius=2, x0=13, y0=30)  
    ball2 = pho.Ball(win, radius=1.5, x0=20, y0=20)
    ball3 = pho.Ball(win, radius=2, x0=37, y0=30)
    ball4 = pho.Ball(win, radius=1.5, x0=30, y0=20)   
    block1 = pho.Block(win, width=15, height=5, color=[0, 100, 200], x0=5, y0=43)  
    block2 = pho.Block(win, width=15, height=5, color=[0, 100, 200], x0=45, y0=43)
    block3 = pho.Block(win, width=10, height=5, color=[0, 100, 200], x0=5, y0=20)
    block4 = pho.Block(win, width=10, height=5, color=[0, 100, 200], x0=45, y0=20)
    block5 = pho.Block(win, width=2, height=50, color=[150, 100, 0], x0=0, y0=25)
    block6 = pho.Block(win, width=2, height=50, color=[150, 100, 0], x0=50, y0=25)
    block7 = pho.Block(win, width=50, height=2, color=[150, 100, 0], x0=25, y0=50)
    triangle2 = pho.Triangle(win, width=10, height=3, color=[0, 0, 0], x0=10, y0=10)    
    triangle3 = pho.Triangle(win, width=10, height=3, color=[0, 0, 0], x0=40, y0=10)   

    object_list = [ball1, ball2, ball3, ball4, block1, block2, block3, block4, block5, block6, block7, triangle2, triangle3]
    return object_list

def main():
    # create a GraphWin
    win = gr.GraphWin("Pinball", 500, 500, False)
    win.setBackground("gold")   

    # call buildObstacles, storing the return list in a variable (e.g. shapes)
    shapes = buildObstacles(win)

    # loop over the shapes list and have each Thing call its draw method
    for shape in shapes:
        shape.draw()

    # assign to dt the value 0.02
    dt = 0.02

    # assign to frame the value 0
    frame = 0

    # create a ball, give it an initial velocity and acceleration, and draw it
    ball = pho.Unique_Ball(win, radius=1)
    ball.setPosition(25, 40)
    ball.setAcceleration(0, -20)
    ball.setVelocity(random.randint(-20, 20), random.randint(-10, 10))
    ball.setColor([50, 200, 100])
    ball.draw()

    # start an infinite loop
    while True:
        # if frame modulo 10 is equal to 0
        if frame % 10 == 0:
            # call win.update()
            win.update()

        # using checkKey, if the user typed a 'q' then break
        key = win.checkKey()
        if key == "q":
            break

        # if the ball is out of bounds, re-launch it
        pos = ball.getPosition()
        if (pos[0] * ball.scale <= 0) or (pos[0] * ball.scale >= win.getWidth()):
            ball.setPosition(25, 45)
            ball.setVelocity(random.randint(-10, 10), random.randint(-10, 10))

        elif (pos[1] * ball.scale >= win.getHeight()) or (pos[1] * ball.scale <= 0):
            ball.setPosition(25, 45)
            ball.setVelocity(random.randint(-10, 10), random.randint(-10, 10))

        # assign to collided the value False
        collided = False

        # for each item in the shapes list
        for shape in shapes:
            # if the result of calling the collision function with the ball and the item is True
            if collision.collision(ball, shape, dt):
                # set collided to True
                collided = True

        # if collided is equal to False
        if not collided:
            # call the update method of the ball with dt as the time step
            ball.update(dt)

        # increment frame
        frame += 1

    # close the window
    win.close()

if __name__ == "__main__":
    main()
