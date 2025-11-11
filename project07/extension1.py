'''simon lartey
11/08/2023
CS 152 B
PROJECT_07 '''

'''the program displays colorful atom collisions in a container, without arrow key control.'''

#importing required modules
import graphicsPlus as gr
import physics_objects as pho
import random
import time

# main function for implementing the test code
def main():
    win = gr.GraphWin("Collision of Atoms", 500, 500, False)        # create a graphics window
    win.setBackground("light pink")
    first_ball = pho.Ball(win)       # create a ball
    first_ball.setPosition(random.randint(10,40), random.randint(10,40))       # move it to the center of the screen and draw it
    first_ball.setVelocity(random.randint(-25,15), random.randint(-20,15))    # give it a random velocity
    first_ball.setAcceleration(0,-15)       # set the acceleration to (0, -20)
    first_ball.draw()    #draw the ball

    second_ball = pho.Ball(win)       # create a ball
    second_ball.setPosition(random.randint(10,40), random.randint(10,40))       # move it to the center of the screen and draw it
    second_ball.setVelocity(random.randint(-25,15), random.randint(-25,15))    # give it a random velocity
    second_ball.setAcceleration(0,-15)         # set the acceleration to (0, -20)
    second_ball.draw()    #draw the ball

    third_ball = pho.Ball(win)       # create a ball
    third_ball.setPosition(random.randint(10,40), random.randint(10,40))       # move it to the center of the screen and draw it
    third_ball.setVelocity(random.randint(-25,15), random.randint(-25,15))    # give it a random velocity
    third_ball.setAcceleration(0,-15)         # set the acceleration to (0, -20)
    third_ball.draw()    #draw the ball

    wall_list = []
    left_block = pho.Block(win, 5, 50)   #create the left wall 
    left_block.setPosition(0,25)  #set position for the left wall
    left_block.draw()   #draw the left wall
    left_block.wall_color()    #color the left wall
    wall_list.append(left_block)   #append the left wall to the wall_list

    right_block = pho.Block(win, 5, 50)    #similarly, for the right wall
    right_block.setPosition(50,25)
    right_block.draw()
    right_block.wall_color()
    wall_list.append(right_block)

    top_block = pho.Block(win, 45, 1)   #similarly, for the top wall
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
        first_ball.update(0.033)  #upate first_ball every 0.033 sec
        second_ball.update(0.033)   #update second_ball
        third_ball.update(0.033)    #update third_ball
        time.sleep(0.033)   #sleep for 0.033 sec
        key = win.checkKey()

        if key == "q":
            break   #breaking if q is entered in keyboard
        if win.checkMouse():
            break  #break if mouse is clicked
        
        if first_ball.ball_collision(second_ball)==True:  #if first_ball collides with second_ball
            velocity_1 = first_ball.getVelocity()  #get vel of first_ball
            velocity_2 = second_ball.getVelocity()   #get vel of second_ball
            first_ball.setVelocity(-velocity_1[0]+random.randint(-2,2),-velocity_1[1]+random.randint(-2,2))    #set new vel for first_ball
            second_ball.setVelocity(-velocity_2[0]+random.randint(-2,2),-velocity_2[1]+random.randint(-2,2))   #set new vel for second_ball

        if second_ball.ball_collision(third_ball)==True:
            velocity_2 = second_ball.getVelocity()
            velocity_3 = third_ball.getVelocity()
            second_ball.setVelocity(-velocity_2[0]+random.randint(-2,2),-velocity_2[1]+random.randint(-2,2))  #set new vel for second_ball
            third_ball.setVelocity(-velocity_3[0]+random.randint(-2,2),-velocity_3[1]+random.randint(-2,2))  #set new vel for third_ball
        
        if third_ball.ball_collision(first_ball)==True:
            velocity_3 = third_ball.getVelocity()
            velocity_1 = first_ball.getVelocity()
            third_ball.setVelocity(-velocity_3[0]+random.randint(-2,2),-velocity_3[1]+random.randint(-2,2))   #set new vel for third_ball
            first_ball.setVelocity(-velocity_1[0]+random.randint(-2,2),-velocity_1[1]+random.randint(-2,2))   #set new vel for first_ball

        for walls in wall_list:
            if walls.collision(first_ball)==True:  #if the ball collides with the wall
                velocity_1 = first_ball.getVelocity()
                first_ball.setVelocity(-velocity_1[0]+random.randint(-1,1),-velocity_1[1]+random.randint(-1,1))  #set new vel for the first_ball
                
            if walls.collision(second_ball)==True:
                velocity_2 = second_ball.getVelocity()
                second_ball.setVelocity(-velocity_2[0]+random.randint(-1,1), -velocity_2[1]+random.randint(-1,1))  #set new vel for the second_ball
            
            if walls.collision(third_ball)==True:
                velocity_3 = third_ball.getVelocity()
                third_ball.setVelocity(-velocity_3[0]+random.randint(-1,1), -velocity_3[1]+random.randint(-1,1))   #set new vel for the third_ball

    win.close()

if __name__ == "__main__":
    #execute main
    main()