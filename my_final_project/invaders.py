
'''Simon lartey
CS 152B 
Final Project
mini space invaders simulation
'''
import matplotlib.pyplot as plt
import physics_objects as pho
import graphicsPlus as gr
import collision
from graphicsPlus import Text
import time
import random

def buildObstacles(win):
    """
    Build a list of obstacle objects in the graphics window.

    Parameters:
    - win (GraphWin): Graphics window in which the obstacles will be drawn.

    Returns:
    - object_list (list): List of obstacle objects.
    """


    ball_large_1 = pho.Ball(win, radius=2, x0=13, y0=25)  
    ball_medium_1 = pho.Ball(win, radius=1.5, x0=20, y0=10)
    ball_large_2 = pho.Ball(win, radius=2, x0=37, y0=25)
    ball_medium_2 = pho.Ball(win, radius=1.5, x0=30, y0=10)
    block_flapper_left = pho.Block(win, width=15, height=5, color=[0, 100, 100], x0=5, y0=14)
    block_flapper_right = pho.Block(win, width=15, height=5, color=[0, 100, 100], x0=45, y0=14)
    block_small_left = pho.Block(win, width=10, height=5, color=[0, 100, 100], x0=5, y0=20)
    block_small_right = pho.Block(win, width=10, height=5, color=[0, 100, 100], x0=45, y0=20)
    block_left_boundary = pho.Block(win, width=2, height=50, color=[150, 100, 0], x0=0, y0=25)
    block_right_boundary = pho.Block(win, width=2, height=50, color=[150, 100, 0], x0=50, y0=25)
    block_top_boundary = pho.Block(win, width=50, height=2, color=[150, 100, 0], x0=25, y0=50)

    triangle_left = pho.Triangle(win, width=10, height=3, color=[0, 0, 0], x0=10, y0=10)
    triangle_right = pho.Triangle(win, width=10, height=3, color=[0, 0, 0], x0=40, y0=10)

    obstacle_1 = pho.Block(win, width=10, height=2, color=[255, 0, 0], x0=15, y0=20)
    obstacle_2 = pho.Ball(win, radius=1, x0=30, y0=20)

    obstacle_3 = pho.Block(win, width=10, height=2, color=[255, 0, 0], x0=5, y0=2)
    obstacle_4 = pho.Block(win, width=10, height=2, color=[255, 0, 0], x0=25, y0=2)
    obstacle_5 = pho.Ball(win, radius=1, x0=40, y0=5)

    object_list = [ball_large_1, ball_medium_1, ball_large_2, ball_medium_2, block_flapper_left, block_flapper_right,
                   block_small_left, block_small_right, block_left_boundary, block_right_boundary, block_top_boundary,
                   triangle_left, triangle_right, obstacle_1, obstacle_2, obstacle_3, obstacle_4, obstacle_5]
    return object_list



def main():

    """
    The main function to run the simulation.

    This function initializes the graphics window, creates and draws obstacles,
    and then runs the simulation loop.
    """

    # Create a graphics window for the Mini Space Invaders game
    win = gr.GraphWin("Mini space Invaders", 500, 500, False)
    win.setBackground("orange")
    
    # Build and draw obstacles
    shapes = buildObstacles(win)
    for shape in shapes:
        shape.draw()

    # Create and draw a resting block at the bottom of the window
    resting_block = pho.Block(win, width=10, height=2, color=[0, 0, 255], x0=25, y0=48)
    resting_block.draw()
    
    # Initialize and draw the unique ball
    ball = pho.Unique_Ball(win, radius=1)
    ball.setPosition(25, 45)
    ball.setAcceleration(0, 0)
    ball.setVelocity(0, 0)
    ball.setColor([50, 200, 100])
    ball.draw()

    # Store the initial position of the ball for potential resets
    initial_position = ball.getPosition()
    # Flag to track whether the ball has been launched
    ball_launched = False

    # Exclude certain balls from collision checks
    balls_to_exclude = shapes[-4:]

    # List to store undrawn block count over time
    undrawn_blocks_count = []
    
    
    # Main simulation loop
    while True:
        # Update the graphics window
        win.update()

        # Check for user keyboard input
        key = win.checkKey()

        # Launch the ball if the space key is pressed and the ball hasn't been launched yet
        if key == "space" and not ball_launched:
            ball.setVelocity(0, -50)
            ball_launched = True

        # Break the loop if the 'q' key is pressed
        elif key == "q":
            break
        
        # Move the ball horizontally or adjust its velocity based on arrow key input
        elif key == "Left":
            pos = ball.getPosition()
            ball.setPosition(pos[0] - 5, pos[1])
        elif key == "Right":
            pos = ball.getPosition()
            ball.setPosition(pos[0] + 5, pos[1])
        
        
         # Adjust the vertical velocity of the ball based on arrow key input
        elif key == "Up":
            v = ball.getVelocity()
            ball.setVelocity(v[0], v[1] + 3)
        elif key == "Down":
            v = ball.getVelocity()
            ball.setVelocity(v[0], v[1] - 3)

        # Check if the ball goes out of bounds, reset if needed
        pos = ball.getPosition()
        if (pos[0] * ball.scale <= 0) or (pos[0] * ball.scale >= win.getWidth()):
            
            # Reset the ball's position and velocity
            ball.setPosition(initial_position[0], initial_position[1])
            ball.setVelocity(0, 0)
            
            # Move the resting block to the initial position
            resting_block.move(initial_position[0] - resting_block.getCenter().getX(), 0)
            
            # Mark the ball as not launched
            ball_launched = False

        elif (pos[1] * ball.scale >= win.getHeight()) or (pos[1] * ball.scale <= 0):
            ball.setPosition(initial_position[0], initial_position[1])
            ball.setVelocity(0, 0)
            resting_block.move(initial_position[0] - resting_block.getCenter().getX(), 0)
            ball_launched = False


        # Check for collisions with blocks and reset if needed
        collided = False
        collided_balls = []
        for shape in shapes:
            if isinstance(shape, pho.Block):

                # Check if the ball collided with a block
                if collision.collision_ball_block(ball, shape, 0.01):
                    collided = True
                    collided_balls.append(shape)

                    # Reset the ball's position and velocity
                    ball.setPosition(initial_position[0], initial_position[1])
                    ball.setVelocity(0, 0)

                    # Mark the ball as not launched
                    ball_launched = False
        
        # Update the simulation if no collisions occurred
        if not collided and ball_launched:

            # Remove collided blocks from the shapes list
            shapes = [shape for shape in shapes if shape not in collided_balls]
            
            # Count undrawn blocks and update the undrawn_blocks_count list
            undrawn_blocks_count.append(sum(1 for shape in shapes if isinstance(shape, pho.Block) and not shape.drawn))
            
            # Check for collisions with other balls to update the ball's position
            if not any(collision.collision(ball, other_ball, 0.01) for other_ball in balls_to_exclude):
                
                # Update the ball's position based on its velocity
                ball.update(0.01)

       

    win.close()

    # Plotting after the simulation is complete
    plt.plot(range(len(undrawn_blocks_count)), undrawn_blocks_count, marker='o')
    plt.xlabel('Time Steps')
    plt.ylabel('Undrawn Blocks Count')
    plt.title('Undrawn Blocks Count vs Time')
    plt.show()

if __name__ == "__main__":
    main()
