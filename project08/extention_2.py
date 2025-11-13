'''Simon Lartey
CS152B
11/07/2023
'''
import physics_objects as pho
import graphicsPlus as gr
import collision
import random

# Define a function named buildObstacles that takes a 'win' parameter (GraphWin object)
def buildObstacles(win):
    
     # Create Ball objects with specified properties
    ball1 = pho.Ball(win, radius=2, x0=13, y0=30)  
    ball2 = pho.Ball(win, radius=1.5, x0=20, y0=20)
    ball3 = pho.Ball(win, radius=2, x0=37, y0=30)
    ball4 = pho.Ball(win, radius=1.5, x0=30, y0=20)   
    
    # Create Block objects with specified properties and colors
    block1 = pho.Block(win, width=15, height=5, color=[0, 100, 200], x0=5, y0=43)  
    block2 = pho.Block(win, width=15, height=5, color=[0, 100, 200], x0=45, y0=43)
    block3 = pho.Block(win, width=10, height=5, color=[0, 100, 200], x0=5, y0=20)
    block4 = pho.Block(win, width=10, height=5, color=[0, 100, 200], x0=45, y0=20)
    
     # Create additional Block objects with specified properties and different colors
    block5 = pho.Block(win, width=2, height=50, color=[150, 100, 0], x0=0, y0=25)
    block6 = pho.Block(win, width=2, height=50, color=[150, 100, 0], x0=50, y0=25)
    block7 = pho.Block(win, width=50, height=2, color=[150, 100, 0], x0=25, y0=50)
    
    # Create Triangle objects with specified properties and color
    triangle2 = pho.Triangle(win, width=10, height=3, color=[0, 0, 0], x0=10, y0=10)    
    triangle3 = pho.Triangle(win, width=10, height=3, color=[0, 0, 0], x0=40, y0=10)   

    # Create a list containing all the created objects
    object_list = [ball1, ball2, ball3, ball4, block1, block2, block3, block4, block5, block6, block7, triangle2, triangle3]
    
    # Return the list of objects
    return object_list


# Define the main function that serves as the entry point for the pinball game
def main():
    win = gr.GraphWin("Pinball", 500, 500, False)
    
    # Set the background color of the window to lime green
    win.setBackground("lime")   

    # Call the buildObstacles function to create and draw various obstacles in the scene
    shapes = buildObstacles(win)

    # Loop through each shape in the list and draw it on the window
    for shape in shapes:
        shape.draw()

    # Assign a time step value of 0.01 seconds
    dt = 0.01

    # Create an empty list to store multiple ball objects
    balls = []

   # Start an infinite loop for the game
    while True:
         # Check for key input from the user
        key = win.checkKey()

        # Exit the loop and close the window if the 'q' key is pressed
        if key == "q":
            break

        # Launch a new ball if 'l' is pressed
        if key == "l":
            new_ball = pho.Unique_Ball(win, radius=1)
            new_ball.setPosition(25, 40)
            new_ball.setAcceleration(0, -20)
            new_ball.setVelocity(random.randint(-20, 20), random.randint(-10, 10))
            new_ball.setColor([50, 200, 100])
            new_ball.draw()
            balls.append(new_ball)

        # Control the velocity of all balls if arrow keys are pressed
        elif key in ["Up", "Down", "Left", "Right"]:
            for ball in balls:
                if key == "Up":
                    ball.setVelocity(ball.getVelocity()[0], ball.getVelocity()[1] + 5)
                elif key == "Down":
                    ball.setVelocity(ball.getVelocity()[0], ball.getVelocity()[1] - 5)
                elif key == "Left":
                    ball.setVelocity(ball.getVelocity()[0] - 5, ball.getVelocity()[1])
                elif key == "Right":
                    ball.setVelocity(ball.getVelocity()[0] + 5, ball.getVelocity()[1])

        # Update all balls and check for collisions
        for ball in balls:
            pos = ball.getPosition()

            # Reset ball if out of bounds
            if (pos[0] * ball.scale <= 0) or (pos[0] * ball.scale >= win.getWidth()) or \
               (pos[1] * ball.scale >= win.getHeight()) or (pos[1] * ball.scale <= 0):
                ball.setPosition(25, 45)
                ball.setVelocity(random.randint(-10, 10), random.randint(-10, 10))

            # Check for collisions with obstacles
            collided = False
            for shape in shapes:
                if collision.collision(ball, shape, dt):
                    collided = True

            if not collided:
                ball.update(dt)

        # Update the window
        win.update()

    # Close the window
    win.close()

if __name__ == "__main__":
    main()

