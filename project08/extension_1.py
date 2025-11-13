'''simon lartey 
November 20, 2023
CS152 B'''


'''Use left and right arrow key when you run this script to control the block at the bottom'''
#importing required moduels
import physics_objects as pho
import graphicsPlus as gr
import collision
import random

def buildObstacles(win):
    # Create large balls at specific positions
    # Create medium-sized balls at specific positions
    # Create left and right flapper blocks
    # Create small left and right blocks
     # Create left and right boundary blocks
     # Create top boundary block
     # Create left and right triangles
     # List of all created objects
    ball_large_1 = pho.Ball(win, radius=2, x0=13, y0=30)  #creating ball
    ball_medium_1 = pho.Ball(win, radius=1.5, x0=20, y0=20)
    ball_large_2 = pho.Ball(win, radius=2, x0=37, y0=30)
    ball_medium_2 = pho.Ball(win, radius=1.5, x0=30, y0=20)   
    block_flapper_left = pho.Block(win, width = 15, height = 5, color = [0,100,100], x0=5, y0=43)  #creating block
    block_flapper_right = pho.Block(win, width = 15, height = 5, color = [0,100,100], x0=45, y0=43)
    block_small_left = pho.Block(win, width = 10, height = 5, color = [0,100,100], x0=5, y0=20)
    block_small_right = pho.Block(win, width = 10, height = 5, color = [0,100,100], x0=45, y0=20)
    block_left_boundary = pho.Block(win, width = 2, height = 50, color = [150,100,0], x0=0, y0=25)
    block_right_boundary = pho.Block(win, width = 2, height = 50, color = [150,100,0], x0=50, y0=25)
    block_top_boundary = pho.Block(win, width = 50, height = 2, color = [150,100,0], x0=25, y0=50)
    
     
    # Create left and right triangles with specific positions and colors
    triangle_left = pho.Triangle(win, width=10, height=3, color = [0,0,0], x0 = 10, y0=10)    
    triangle_right = pho.Triangle(win, width=10, height=3, color = [0,0,0], x0 = 40, y0=10)   #creating a triangle
    
    # Create additional obstacles (you can customize positions, sizes, and types)
    obstacle_1 = pho.Block(win, width=10, height=2, color=[255, 0, 0], x0=15, y0=35)
    obstacle_2 = pho.Ball(win, radius=1, x0=30, y0=35)


     # List of all created objects including balls, blocks, and triangles
    object_list = [ball_large_1, ball_medium_1, ball_large_2, ball_medium_2, block_flapper_left, block_flapper_right, block_small_left, block_small_right, block_left_boundary, block_right_boundary, block_top_boundary, triangle_left , triangle_right, obstacle_1,obstacle_2 ]  
    return object_list

def  main():
    
    # Create a window for the pinball game
    win = gr.GraphWin("Pinball", 500, 500, False)
    win.setBackground("white")   
    
    # Build obstacles and draw them on the window
    shapes = buildObstacles(win)
    for shape in shapes:
        shape.draw()
    
    # Set up initial conditions for the main and secondary balls, and the flapper block
    dt = 0.01
    frame = 10
    ball_large_1 = pho.Unique_Ball(win, radius = 1)   
    ball_large_1.setPosition(25,40)  
    ball_large_1.setAcceleration(0,-20)   
    ball_large_1.setVelocity(random.randint(-20,20), random.randint(-10,10))  
    ball_large_1.setColor([50,200,100])  
    ball_large_1.draw()

    
    ball_medium_1 = pho.Unique_Ball(win, radius = 1)
    ball_medium_1.setPosition(20,45)
    ball_medium_1.setAcceleration(0,-20)
    ball_medium_1.setVelocity(random.randint(-20,20), random.randint(-10,10))
    ball_medium_1.setColor([50,200,100])
    ball_medium_1.draw()

    block = pho.Block(win, width = 15, height = 1, color = [150,100,0], x0=25, y0=1)  
    block.draw()
    
    
    while True:
        if frame%10 ==0:
            win.update()
        
       
        key = win.checkKey()

        if key== "Left":
            position = block.getPosition()
            block.setPosition(position[0]-10, position[1])  

        if key == "Right":
            position = block.getPosition()
            block.setPosition(position[0]+10, position[1])   
        if key == "q":
            break
        
        if win.checkMouse():
            break
        
        pos1 = ball_large_1.getPosition()
        if (pos1[0]*(ball_large_1.scale) <= 0) or (pos1[0]*ball_large_1.scale >=win.getWidth()):  
            ball_large_1.setPosition(25,45)   
            ball_large_1.setVelocity(random.randint(-10,10), random.randint(-10,10))   

        elif (pos1[1]*ball_large_1.scale >= win.getHeight()) or (pos1[1]*ball_large_1.scale <=0):  
            ball_large_1.setPosition(25, 45)   
            ball_large_1.setVelocity(random.randint(-10,10), random.randint(-10,10))    

        collided = False

        for shape in shapes:   
            if collision.collision(ball_large_1, shape, dt)==True:  
                collided = True

        if collision.collision(ball_large_1, block, dt)==True:
            collided = True

        if collided == False:
            ball_large_1.update(dt)   

       
        pos2 = ball_medium_1.getPosition()
        if (pos2[0]*(ball_medium_1.scale) <= 0) or (pos2[0]*ball_medium_1.scale >=win.getWidth()):  
            ball_medium_1.setPosition(20,40)   
            ball_medium_1.setVelocity(random.randint(-10,10), random.randint(-10,10))   

        elif (pos2[1]*ball_large_1.scale >= win.getHeight()) or (pos2[1]*ball_large_1.scale <=0):  
            ball_medium_1.setPosition(20, 40)   
            ball_medium_1.setVelocity(random.randint(-10,10), random.randint(-10,10))    

        collided = False
        for shape in shapes:
            if collision.collision(ball_medium_1, shape, dt)==True:
                collided = True

        if collision.collision(ball_medium_1, block, dt)==True:
            collided = True

        if collision.collision(ball_large_1,ball_medium_1, dt)==True:
            collided = True

        if collided == False:
            ball_medium_1.update(dt)

        
        win.update()
        frame += 1

      
    win.close()

if __name__ == "__main__":
    
    
    main()


