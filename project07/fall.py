"""
simon lartey
CS 152B
11/08/2023 
Project_07
"""

# importing required packages
import graphicsPlus as gr
import physics_objects as pho
import random
import time

# main function for implementing the test code
def main():
    '''undraws the block when a ball collides with it and positions ball to the center if the ball goes outside the window'''

    win = gr.GraphWin("Falling", 500, 500, False)  # create a graphics window
    ball = pho.Ball(win)  # create a ball
    ball.setPosition(25, 25)  # move it to the center of the screen and draw it
    ball.setVelocity(random.randint(0, 20), random.randint(0, 20))  # give it a random velocity
    ball.setAcceleration(0, -5)  # set the acceleration to (0, -20)
    ball.draw()  # draw the ball
    win_center = [25, 25]  # set the window's center to 25, 25

    block_list = []
    for i in range(20):  # looping 20 times
        block = pho.Block(win, 5, 5)  # creating a block
        block.setPosition(random.randint(0, 50), random.randint(0, 50))  # set block position
        block.block_color() # Set the block color to blue
        block.draw()  # draw the block
        block_list.append(block)  # append the block to block_list

    # Add blocks to the bottom of the screen
    for i in range(5):
        block = pho.Block(win, 5, 5)
        block.setPosition(i * 10, win.getHeight() - 5)
        block.draw()
        block.wall_color()  # Set the wall block color to a random color
        block_list.append(block)

    while True:
        ball.update(0.033)
        time.sleep(0.033)
        key = win.checkKey()  # checking the key entered
        if key == "q":
            break  # breaking if "q" is entered on the keyboard
        if win.checkMouse():
            break  # break if the mouse is clicked
        if key == "Left":
            v = ball.getVelocity()
            ball.setVelocity(v[0] - 3, v[1])  # if Left arrow, x velocity is decreased by 3
        if key == "Right":
            v = ball.getVelocity()
            ball.setVelocity(v[0] + 3, v[1])  # if right arrow, x velocity is increased by 3
        if key == "Up":
            v = ball.getVelocity()
            ball.setVelocity(v[0], v[1] + 3)  # if up arrow, y velocity is increased by 3
        if key == "Down":
            v = ball.getVelocity()
            ball.setVelocity(v[0], v[1] - 3)  # if down arrow, y velocity is decreased by 3

        for block in block_list:
            if block.collision(ball) == True:  # if collision occurs
                block.undraw()  # undraw the block
                block_list.remove(block)  # remove the block from the list

        pos = ball.getPosition()
        if (pos[0] * ball.scale <= 0) or (pos[0] * ball.scale >= win.getWidth()):  # condition for the ball to get out of the window
            ball.setPosition(win_center[0], win_center[1])  # position it to the center
            ball.setVelocity(random.randint(-5, 5), random.randint(-5, 5))  # give random velocity

        elif (pos[1] * ball.scale >= win.getHeight()) or (pos[1] * ball.scale <= 0):  # condition for the ball to get out of the window
            ball.setPosition(win_center[0], win_center[1])  # position it to the center
            ball.setVelocity(random.randint(-5, 5), random.randint(-5, 5))  # give random velocity

    win.close()  # close the window

if __name__ == "__main__":
    '''Executes main'''
    main()
