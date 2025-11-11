"""
simon lartey
CS 152B
11/08/2023 
Project_07
"""

'''Run this script and use arrow keys to control the movement of the ball. If a ball hits the block, the block turns green . The block
bounces back if it hits the wall. The ball changes its color every 0.033 sec'''

#importing required packages
import graphicsPlus as gr
import physics_objects as pho
import random
import time

def main():
    # Create a graphics window.
    win = gr.GraphWin("Mini Game: Bounce Back", 500, 500, False)        # create a graphics window
    
    # Create a ball, set its position, velocity, and acceleration, and draw it.
    ball = pho.Ball(win)       # create a ball
    ball.setPosition(25,25)       # move it to the center of the screen and draw it
    ball.setVelocity(random.randint(0,20), random.randint(0,20))    # give it a random velocity
    ball.setAcceleration(0,-10)       # set the acceleration to (0, -20)
    ball.draw()    #draw the ball
    win.setBackground("orange")   #setting the backgorund color to orange

    block_list= []
    for i in range(5):   #loop five times
        block = pho.Block(win, 5, 5)   #creates block
        block.setPosition(random.randint(6,44), random.randint(4,44))  #sets blocks at position
        block.draw()  #draw the block
        block_list.append(block)   #append each block to block_list

    wall_list = []   
    left_block = pho.Block(win, 5, 50)   #creating a wall to the left of the screen
    left_block.setPosition(0,25)   #set the position at 0,25
    left_block.draw()    #draw the wall
    left_block.wall_color()   #color the wall
    wall_list.append(left_block)   #append the wall to wall_list

    right_block = pho.Block(win, 5, 50) #similarly, for the right wall 
    right_block.setPosition(50,25)
    right_block.draw()
    right_block.wall_color()
    wall_list.append(right_block)

    top_block = pho.Block(win, 45, 2) #similarly, for the top wall 
    top_block.setPosition(25,50)
    top_block.draw()
    top_block.wall_color()
    wall_list.append(top_block)

    bottom_block = pho.Block(win, 45, 5)  #similarly, for the bottom wall 
    bottom_block.setPosition(25,0)
    bottom_block.draw()
    bottom_block.wall_color()
    wall_list.append(bottom_block)

    while True:
        ball.update(0.033)  #update each 0.033 sec
        time.sleep(0.033)  #sleep eevry 0.033 sec
        key = win.checkKey()   #check the key
        if key == "q":
            break   #breaking if q is entered in keyboard
        if win.checkMouse():
            break  #break if mouse is clicked
        
        if key=="Left":
            v = ball.getVelocity()
            ball.setVelocity(v[0]-2, v[1])   #if left arrow, decrease x velocity by 2
        if key == "Right":
            v = ball.getVelocity()
            ball.setVelocity(v[0]+2, v[1]) #if right arrow, increase x velocity by 2
        if key == "Up":
            v = ball.getVelocity()
            ball.setVelocity(v[0], v[1]+2)  #if up arrow, increase y velocity by 2
        if key =="Down":
            v = ball.getVelocity()
            ball.setVelocity(v[0], v[1]-2)   #if down arrow, decrease y velocity by 2
        if key =="space":
            v = ball.getVelocity()
            ball.setVelocity(v[0]/4, v[1]/4)   #if spacebar, decrease x and y velocity by 1/4

        for blocks in block_list:
            if blocks.collision(ball)==True:  #if the ball collides with the ball
                blocks.block_color()   #color the block
                ball_position = ball.getPosition()
                block_pos = block.getPosition()
                if ball_position[1]<=block_pos[1]:  #block is higher than the ball
                    ball_velocity = ball.getVelocity()
                    ball.setVelocity(ball_velocity[0], - (ball_velocity[1]))   #returns to the -ve of the y direction with the same magniture
                if ball_position[1]>=block_pos[1]:   #ball is higher than the block
                    ball_velocity = ball.getVelocity()
                    ball.setVelocity(ball_velocity[0], - (ball_velocity[1]))   #returns to the -ve of y direction with the same magniture
                if ball_position[0]<=block_pos[0]:    #ball is to the left than the block
                    ball_velocity = ball.getVelocity()
                    ball.setVelocity(-(ball_velocity[0]), ball_velocity[1])   #returns to the -ve of the x direction with the same magniture
                if ball_position[0]>=block_pos[0]:    #block is to the left than the ball
                    ball_velocity = ball.getVelocity()
                    ball.setVelocity(-(ball_velocity[0]), ball_velocity[1])   #returns to the -ve of the x direction with the same magniture
                    
        for walls in wall_list:
            if walls.collision(ball)==True:   #if the ball collides with the ball
                ball_position = ball.getPosition()
                block_pos = block.getPosition()
                if ball_position[1]<=block_pos[1]:  #block is higher than the ball
                    ball_velocity = ball.getVelocity()
                    ball.setVelocity(ball_velocity[0], -ball_velocity[1])    #returns to the -ve of the y direction with the same magniture
                if ball_position[1]>=block_pos[1]:   #ball is higher than the block
                    ball_velocity = ball.getVelocity()
                    ball.setVelocity(ball_velocity[0], -ball_velocity[1])  #returns to the -ve of the y direction with the same magniture
                if ball_position[0]<=block_pos[0]:    #ball is to the left than the block
                    ball_velocity = ball.getVelocity()
                    ball.setVelocity(-ball_velocity[0], ball_velocity[1])  #returns to the -ve of the x direction with the same magniture
                if ball_position[0]>=block_pos[0]:    #block is to the left than the ball
                    ball_velocity = ball.getVelocity()
                    ball.setVelocity(-ball_velocity[0], ball_velocity[1])  #returns to the -ve of the x direction with the same magniture
    win.close()    #close the window

if __name__ == "__main__":
    #execute main
    main()