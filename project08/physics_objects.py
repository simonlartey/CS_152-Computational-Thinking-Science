'''Simon Lartey
CS152B
11/07/2023
'''
import graphicsPlus as gr
import random
import time

# Parent class for various objects in the simulation
class Thing:
    def __init__(self, win, the_type ):
        # Initialize common attributes for all objects
        self.type = the_type
        self.position = [0,0]  
        self.velocity = [0,0]   
        self.acceleration = [0,0]  
        self.elasticity = 1  
        self.win = win   
        self.scale = 10   
        self.vis = []
        self.color = (0,0,0)
        self.drawn = False

    # Getter methods for various attributes
    def getType(self):
        return self.type
    
    def getMass(self):  
        return self.mass 
    
    def getPosition(self):
        return self.position[:]
    
    def getVelocity(self):
        return self.velocity[:]   

    def getAcceleration(self):
        return self.acceleration[:]  

    def getElasticity(self):
        return self.elasticity
    
    def getScale(self):
        return self.scale
    
    def getColor(self): 
        return self.color
    
    # Method to draw the object
    def draw(self):
        for item in self.vis:
            item.draw(self.win)
        self.drawn = True

    # Method to undraw the object 
    def undraw(self):
        for item in self.vis:
            item.undraw()
        self.drawn = False      

    # Setter method for mass
    def setMass(self, m):
        self.mass = m 
    
     # Setter method for velocity
    def setVelocity(self, vx, vy):
        self.velocity[0]=vx   
        self.velocity[1]=vy   
    
     # Setter method for acceleration
    def setAcceleration(self, ax, ay):
        self.acceleration[0]=ax  
        self.acceleration[1]=ay   

     # Setter method for elasticity
    def setElasticity(self, E):
        self.elasticity = E

     # Setter method for position
    def setPosition(self,px,py):
        x_old = self.getPosition()[0]  
        y_old = self.getPosition()[1]  
        self.position[0]=px   
        self.position[1]=py   

        dx = (px - x_old)*self.scale   
        dy = (py - y_old)*(-self.scale)   
        for item in self.vis:
            item.move(dx,dy)   
     # Setter methods for color
    def setColor(self, c):
        
        self.color = c
        if c != None:
            for item in self.vis:
                item.setFill(gr.color_rgb(c[0],c[1],c[2])) 

    # Method to update the position based on current velocity and acceleration
    def update(self, dt):
        
        x_old = self.position[0]
        y_old = self.position[1]
        self.position[0] = x_old+self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt   
        self.position[1] = y_old+self.velocity[1]*dt+0.5*self.acceleration[1]*dt*dt    

        dx = self.scale *self.velocity[0]*dt   
        dy = - self.scale *self.velocity[1]*dt 
        
        for item in self.vis:
            item.move(dx,dy)  
        self.velocity[0]+=self.acceleration[0]*dt  
        self.velocity[1]+= self.acceleration[1]*dt  

# Child class representing a Ball
class Ball(Thing):
   
    def __init__(self, win, radius=1, x0=0, y0=0, color=[50,200,250]):   
        Thing.__init__(self, win, "ball")  
        self.radius = radius
        self.position = [x0,y0]  
        self.refresh()  
        self.setColor(color) 

     # Method to redraw the ball
    def refresh(self):
        '''draws the ball'''
        drawn = self.drawn
        if drawn:
            self.undraw()

        # Create a circle representing the ball
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        self.radius*self.scale)]
        if drawn:
            self.draw(self.win)
    
    # Getter for the radius
    def getRadius(self):
        return self.radius
    
    # Getter for the radius
    def setRadius(self, R):
        self.radius = R
        self.refresh()


# Child class representing a Block
class Block(Thing):
    def __init__(self, win, x0=0, y0=0, width=2, height=1, color=None):
        Thing.__init__(self, win, "block")
        self.width = width
        self.height = height
        self.position = [x0, y0]
        self.dx = width  
        self.dy = height  
        self.refresh()
        self.setColor(color)

    
    # Method to redraw the block
    def refresh(self):
        '''draws the block'''
        drawn = self.drawn
        if drawn:
            self.undraw()

        # Create a rectangle representing the block
        self.vis = [gr.Rectangle(gr.Point((self.position[0] - 0.5 * self.dx) * self.scale,
                                         self.win.getHeight() - (self.position[1] - 0.5 * self.dy) * self.scale),
                                 gr.Point((self.position[0] + 0.5 * self.dx) * self.scale,
                                         self.win.getHeight() - (self.position[1] + 0.5 * self.dy) * self.scale))]
        if drawn:
            self.draw(self.win)

    # Getter for the width
    def getWidth(self):
        '''returns the width of the block'''
        return self.width
    
    # Getter for the height
    def getHeight(self):
        '''returns the height of the block'''
        return self.height

    # Setter for the width
    def setWidth(self, width):
        '''updates the width of the block'''
        self.width = width
        self.dx = width
        self.refresh()

    # Setter for the height
    def setHeight(self, height):
        '''updates the height of the block'''
        self.height = height
        self.dy = height
        self.refresh()

# Child class representing a Triangle
class Triangle(Thing):
    '''create a Triangle child class'''
    def __init__(self, win, x0=0, y0=0, width=5, height=5, color = [0,0,0]): 
        Thing.__init__(self, win, "triangle")  
        self.width = width
        self.height = height
        self.position = [x0, y0]
        self.refresh()
        self.setColor(color)

    def refresh(self):
        '''draw the triangle'''
        if self.drawn:
            self.undraw()
        
        x = self.position[0]*self.scale
        y = self.position[0]*self.scale
        h = self.height*self.scale
        w = self.width * self.scale

        self.vis = [gr.Polygon(gr.Point(self.position[0]*self.scale, self.win.getHeight()-(self.position[1]+ self.height/2)*self.scale),
                gr.Point((self.position[0]+self.width/2)*self.scale,self.win.getHeight()-(self.position[1]-self.height/2)*self.scale),
                gr.Point((self.position[0]-self.width/2)*self.scale, self.win.getHeight()-(self.position[1]-self.height/2)*self.scale))]

        for item in self.vis:
            item.setFill(self.color)   
        
        if self.drawn:
            self.drawn(self.win)  
    
    def getHeight(self):
        '''get height of triangle'''
        return self.height
    
    def getWidth(self):
        '''get width of triangle'''
        return self.width
    
    def setHeight(self,dy):
        '''set height of triangle'''
        self.height = dy
        self.redraw()
    
    def setWidth(self,dx):
        '''set width of triangle'''
        self.width = dx
        self.redraw()

# Define a class named New_Shape that inherits from the Thing class.
class New_Shape(Thing):
    
    def __init__(self, win, radius=1, x0=0, y0=0, width = 1, height = 1, color=[50,200,250]):  
        # Call the constructor of the parent class (Thing) with specified parameters.
        Thing.__init__(self, win, "ball")  
       
        # Initialize instance variables with provided or default values.
        self.radius = radius
        self.position = [x0,y0]
        self.width = width
        self.height = height
        
        # Call the refresh method to update the appearance of the shape.
        self.refresh()  
        
        # Set the color of the shape using the provided color values.
        self.setColor(color) 

       
        # Create a circle and a block (rectangle) representing the shape.
        # The circle is positioned based on the scaled position and radius.
        # The block is positioned based on the scaled position, width, and height.
        self.circle = gr.Circle(gr.Point(self.position[0]*self.scale+17,
                                        self.win.getHeight()-self.position[1]*self.scale +17), 
                                        self.radius*self.scale)  
        self.block = gr.Rectangle(gr.Point((self.position[0]-0.5*self.width)*self.scale, (self.win.getHeight()-(self.position[1]-0.5*self.height)*self.scale)),
                    gr.Point((self.position[0]+0.5*self.width)*self.scale,(self.win.getHeight()-(self.position[1]+0.5*self.height)*self.scale)))
        
        # Add the circle and block to the visualization list.
        self.vis += self.circle, self.block

    def refresh(self):
        
        drawn = self.drawn
        if drawn:
            self.undraw()
    
        # Create a new visualization list with a circle representing the shape.
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        self.radius*self.scale)] 
        
        # If the shape was originally drawn, redraw it on the window.
        if drawn:
            self.draw(self.win)

    # Define a method to update the position and velocity of the shape based on elapsed time (dt).
    def update(self, dt):
        # Store the current x and y positions.
        x_old = self.position[0]
        y_old = self.position[1]
        
        # Update the x and y positions based on velocity and acceleration using the kinematic equations.
        self.position[0] = x_old+self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt 
        self.position[1] = y_old+self.velocity[1]*dt+0.5*self.acceleration[1]*dt*dt    
        
        # Calculate the change in x and y based on the scaled velocity and time.
        dx = self.scale *self.velocity[0]*dt   
        dy = - self.scale *self.velocity[1]*dt 
        
        # Move the visualization elements (circle) by the calculated change in x and y.
        for circle in self.vis:
            circle.move(dx,dy)  

        # Update the velocity based on acceleration and time.
        self.velocity[0]+=self.acceleration[0]*dt
        self.velocity[1]+= self.acceleration[1]*dt
    
    # Define a method to get the radius of the shape.
    def getRadius(self):
        return self.radius
    
    # Define a method to set the radius of the shape and refresh its appearance.
    def setRadius(self, R):
        self.radius = R
        self.refresh()




# This is a new class created for the extension. 
# To achieve colorful balls with concentric radii, several attributes of the Ball class needed modification.
# Therefore, this new class was introduced to encapsulate the changes and additions required for the extension.


# Define a class named Unique_Ball that inherits from the Thing class.
class Unique_Ball(Thing):
    
    # Constructor method for initializing the Unique_Ball object.
    def __init__(self, win, radius=1, x0=0, y0=0, color=[50,200,250]):
        Thing.__init__(self, win, "ball")   
        
        # Initialize instance variables with provided or default values.
        self.radius = radius
        self.position = [x0,y0]
        
        # Call the refresh method to update the appearance of the concentric circles. 
        self.refresh()  
        # Set the color of the circles using the provided color values.
        self.setColor(color) 

       # Create three circles with different radii and add them to the visualization list.
        self.circle1 = gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        self.radius*self.scale)
        self.circle2 = gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        0.75*self.scale)
        self.circle3 = gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        0.5*self.scale)
        self.vis += self.circle1, self.circle2, self.circle3


    # Method to refresh the appearance of the concentric circles.
    def refresh(self):       
        drawn = self.drawn
        # Check if the circles are already drawn, if so, undraw them.
        if drawn:
            self.undraw()

        # Create a new visualization list with a circle representing the concentric circles.
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        self.radius*self.scale)]
        
        # If the circles were originally drawn, redraw them on the window.
        if drawn:
            self.draw(self.win)

    # Method to update the position, velocity, and color of the concentric circles based on elapsed time (dt).
    def update(self, dt):
        # Store the current x and y positions.
        x_old = self.position[0]
        y_old = self.position[1]
        
        # Update the x and y positions based on velocity and acceleration using the kinematic equations.
        self.position[0] = x_old+self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt   
        self.position[1] = y_old+self.velocity[1]*dt+0.5*self.acceleration[1]*dt*dt    

        # Calculate the change in x and y based on the scaled velocity and time.
        dx = self.scale *self.velocity[0]*dt   
        dy = - self.scale *self.velocity[1]*dt 
        
        
        # Move each circle in the visualization list by the calculated change in x and y.
        # Also, randomly set the fill color of each circle.
        for circle in self.vis:
            circle.move(dx,dy)  
            circle.setFill(random.choice(["red", "blue", "green", "brown", "pink"]))
        self.velocity[0]+=self.acceleration[0]*dt
        self.velocity[1]+= self.acceleration[1]*dt
    
    # Method to get the radius of the concentric circles.
    def getRadius(self):
        return self.radius
    
    # Method to set the radius of the concentric circles and refresh their appearance.
    def setRadius(self, R):
        self.radius = R
        self.refresh()


