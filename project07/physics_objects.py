'''Simon Lartey
CS152B
11/07/2023
'''
import graphicsPlus as gr
import random
import time
class Ball:
    def __init__(self, win, position=[0, 0], radius=1):
        # Initialize the fields
        self.mass = 1
        self.radius = radius
        self.position = position
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.win = win
        self.scale = 10

        # Calculate the screen coordinates for visualization
        x_screen = self.position[0] * self.scale
        y_screen = win.getHeight() - self.position[1] * self.scale

        # Create a Zelle Graphics Circle object for visualization
        self.vis = [gr.Circle(gr.Point(x_screen, y_screen), self.radius * self.scale)]

    def draw(self):
        # Loop over self.vis and call the draw method for each item
        for item in self.vis:
            item.draw(self.win)

    # Getter and Setter methods
    def getPosition(self):
        return self.position[:]

    def setPosition(self, px, py):
        x_old = self.getPosition()[0]  #getting current x coordinate of position
        y_old = self.getPosition()[1]   #getting current y coordinate of position
        # Update the x and y positions
        self.position[0] = px
        self.position[1] = py

        # Calculate the change in position in screen coordinates
        dx = (px - x_old) * self.scale
        dy = (py - y_old) * -self.scale

        # Move the visualization object to the new position
        for item in self.vis:
            item.move(dx, dy)

    def getVelocity(self):
        return self.velocity[:]

    def setVelocity(self, vx, vy):
        self.velocity[0] = vx
        self.velocity[1] = vy

    def getAcceleration(self):
        return self.acceleration[:]

    def setAcceleration(self, ax, ay):
        self.acceleration[0] = ax
        self.acceleration[1] = ay

    def getMass(self):
        return self.mass

    def setMass(self, m):
        self.mass = m

    def getRadius(self):
        return self.radius

    #  setRadius method
    def setRadius(self, r):
        self.radius = r
        # Update the visualization object's radius
        for item in self.vis:
            item.undraw()
            x_screen = self.position[0] * self.scale
            y_screen = self.win.getHeight() - self.position[1] * self.scale
            self.vis = [gr.Circle(gr.Point(x_screen, y_screen), r * self.scale)]

    def update(self, dt):
        # Get the current x and y positions
        x_old = self.getPosition()[0]
        y_old = self.getPosition()[1]

        # Update the x and y positions based on the equations of motion
        self.position[0] = x_old + self.getVelocity()[0] * dt + 0.5 * self.getAcceleration()[0] * dt*dt
        self.position[1] = y_old + self.getVelocity()[1] * dt + 0.5 * self.getAcceleration()[1] * dt*dt
        
        # Calculate the change in position in screen coordinates
        dx = (self.position[0] - x_old) * self.scale
        dy = (self.position[1] - y_old) * -self.scale

        # Move the visualization object to the new position
        for item in self.vis:
            item.move(dx, dy)
            item.setFill(random.choice(["red", "blue", "green", "brown"]))
        # Update the x and y velocities based on the accelerations
        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt

    
    
    def collision(self, ball):
        #this function returns true if the ball collides with the block
        r = ball.getRadius()  #radius of the ball
        ball_pos = ball.getPosition()   #position of center of the ball
        block_pos = self.getPosition()   #positon of center of the rectangle
        min_ball_block_x = ball_pos[0]+block_pos[0]  #x distance between center of ball and block when collide horizontally
        min_ball_block_y = ball_pos[1]+block_pos[1]   #y distance between center of ball and block when collide vertically
        x_distance = abs(ball_pos[0]-block_pos[0])  #any x distance between center of ball and block
        y_distance = abs(ball_pos[1]-block_pos[1])   #any y distance between center of ball and block
        if (x_distance<= min_ball_block_x) and (y_distance<=min_ball_block_y):  #condition for collision
            return True
        else:
            return False
    
    def ball_collision(self, ball):
        #this function returns true if the ball collides with the block
        r = ball.getRadius()  #radius of the ball
        ball_pos = ball.getPosition()   #position of center of the ball
        block_pos = self.getPosition()   #positon of center of the rectangle
        min_ball_block_x = 2*r   #x distance between center of ball and block when collide horizontally
        min_ball_block_y = 2*r   #y distance between center of ball and block when collide vertically
        x_distance = abs(ball_pos[0]-block_pos[0])  #any x distance between center of ball and block
        y_distance = abs(ball_pos[1]-block_pos[1])   #any y distance between center of ball and block
        if (x_distance<= min_ball_block_x) and (y_distance<=min_ball_block_y):  #condition for collision
            return True
        else:
            return False





class Block:
    def __init__(self, win, dx, dy):
        #Creates a block with mass, position, velocity, acceleration
        self.dx = dx   # Initial width of dx
        self.dy = dy    # Initial height dy
        self.mass = 1   # Initial mass of 1
        self.position = [0, 0]   # Initial position at 0,0
        self.velocity = [0, 0]   # Initial velocity of 0,0
        self.acceleration = [0, 0]  # Initial acceleration of 0,0
        self.win = win   # GraphWin
        self.scale = 10   # Scale
        self.vis = [gr.Rectangle(gr.Point((self.position[0]-0.5*self.dx)*self.scale,   #creating a block
                    self.win.getHeight() - (self.position[1]-0.5*self.dy)*self.scale),
                    gr.Point((self.position[0]+0.5*self.dx)*self.scale,
                    self.win.getHeight()-(self.position[1]+0.5*self.dy)*self.scale))]
                    
    def draw(self):
        #Takes each block in self.vis and draws them in the window
        for rectangle in self.vis:
            rectangle.draw(self.win)  #draw a block in the window
    
    def undraw(self):
        #undraws the rectangle
        for rectangle in self.vis:
            rectangle.undraw()   #undraw a block from window

    def getPosition(self):
        #Returns a 2 element tuple with the x,y position
        return self.position[:]  #getting a copy of position

    def setPosition(self,px,py):
        #sets the position to new coordinates and moves the rectangle to that coordinates
        x_old = self.position[0]   #old x position
        y_old = self.position[1]    #old y position

        self.position[0]=px   #new x position
        self.position[1]=py   #New y position

        dx = (px - x_old)*self.scale   #difference in the x position
        dy = (py - y_old)*(-self.scale)   #difference in the y position

        for rectangle in self.vis:
            rectangle.move(dx,dy)   #moving the block by dx,dy

    def getVelocity(self):
        #returns a 2 element tuple with x and y velocities
        return self.velocity[:] 

    def setVelocity(self, vx, vy):
        #returns new vx,vy velocities
        self.velocity[0]=vx    #x vel is vx
        self.velocity[1]=vy   #y vel is vy

    def getAcceleration(self):
        #returns a 2-element tuple with x and y acceleration values
        return self.acceleration[:]  #getting copy of acceleration

    def setAcceleration(self, ax, ay):
        #returns a new ax, ay accelerationv values
        self.acceleration[0]=ax  #x acceleration is ax
        self.acceleration[1]=ay   #y acceleration is ay
    
    def getWidth(self):
        #returns the width of the block
        return self.dx   #gets width of block
    
    def getHeight(self):
        #returns the height of the block
        return self.dy

    def update(self, dt):
        #updates the dx, dy and velocity using kinematics equation
        x_old = self.position[0]   #old x position
        y_old = self.position[1]   #old y position
        x_new = x_old+self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt   #updating the x postion using equation of kinematics
        y_new = y_old+self.velocity[1]*dt+0.5*self.acceleration[1]*dt*dt     #updating the x postion using equation of kinematics
        self.setPosition(x_new, y_new)   #setting new position
        
        dx = (x_new - x_old)*self.scale   #difference in x position
        dy = (y_new - y_old)*(-self.scale)

        for circle in self.vis:
            circle.move(dx,dy)  #move circle by dx,dy
        self.velocity[0]+=self.acceleration[0]*dt  #x velocity
        self.velocity[1]+= self.acceleration[1]*dt   #y velocity


    def collision(self, ball):
            #this function returns true if the ball collides with the block
            r = ball.getRadius()  #radius of the ball
            ball_pos = ball.getPosition()   #position of center of the ball
            block_pos = self.getPosition()   #positon of center of the rectangle
            min_ball_block_x = r + self.dx/2   #x distance between center of ball and block when collide horizontally
            min_ball_block_y = r + self.dy/2    #y distance between center of ball and block when collide vertically
            x_distance = abs(ball_pos[0]-block_pos[0])  #any x distance between center of ball and block
            y_distance = abs(ball_pos[1]-block_pos[1])   #any y distance between center of ball and block
            if (x_distance <= min_ball_block_x) and (y_distance<=min_ball_block_y):  #condition for collision
                return True
            else:
                return False


    def block_color(self):
        #fills blue color to the block
        for i in self.vis:
            i.setFill("green")
    
    def wall_color(self):
        #fills random color to the wall (block)
        for i in self.vis:
            i.setFill(random.choice(["red", "black"]))
    





