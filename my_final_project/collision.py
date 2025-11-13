
'''Simon Lartey
CS152B
11/07/2023
'''

import math

def length(v):
    """utility math function for calculating Euclidean length of a 2D vector"""
    return math.sqrt(v[0]*v[0] + v[1]*v[1])

def unit(v):
    """utility math function for creating a unit 2D vector"""
    l = math.sqrt(v[0]*v[0] + v[1]*v[1])
    if l > 0.0:
        return (v[0]/l, v[1]/l)
    return v


def collisionTest_ball_wall( ball, wall ):
    # Tests if there is a collision with the wall along the path of 
    # the ball. Returns the distance to the collision or 1e+6 (a big number)

    # get the ball's velocity and current position
    v = unit( ball.getVelocity() )
    ballP = ball.getPosition()

    # get the position of the floor
    wallP = wall.getPosition()

    # a variation on Liang-Barsky clipping
    p1 = -v[0]
    p2 = v[0]
    if ballP[0] < wallP[0]:
        # ball is to the left of the wall, so use the left boundary and ballx + radius
        q1 = (ballP[0]+ ball.getRadius()) - (wallP[0] - wall.getWidth()*0.5)
        q2 = (wallP[0] - wall.getWidth()*0.5) - (ballP[0] - ball.getRadius())
    else:
        # ball is on the right, so subtract radius and add wall width
        q1 = (ballP[0] - (ball.getRadius())) - (wallP[0] + wall.getWidth()*0.5)
        q2 = (wallP[0] + wall.getWidth()*0.5) - (ballP[0] - (ball.getRadius()))

    # running parallel to the wall, no collision for a stationary wall
    if p1 == 0.0: 
        return 1e+6

    if p1 < 0: # ball is heading in a +y direction
        if q1 > 0: # ball is headed away from the wall
            return 1e+6
        else: # ball is headed towards the wall
            return q1 / p1
    else: # ball is heading in a -y direction
        if q2 > 0: # ball is headed away from the wall
            return 1e+6
        else:
            return q2/p2
    

def collision_ball_wall(ball, wall, dt):
    tk = collisionTest_ball_wall(ball, wall)

    d = length(ball.getVelocity())
    if d == 0.0:
        return False

    delta = tk / (d * dt)
    if delta <= 1.0:
        ball.update(delta * dt)
        ball.setVelocity(-ball.getVelocity()[0], ball.getVelocity()[1])
        ball.update(dt - delta * dt)
        return True

    return False
def collisionTest_ball_floor( ball, floor ):
    # Tests if there is a collision with the floor along the path of the
    # ball. Returns the distance to the collision or 1e+6 (a big number)

    # get the trajectory and position of the ball
    v = unit( ball.getVelocity() )
    ballP = ball.getPosition()

    # get the y position of the floor
    floorP = floor.getPosition()

    # a variation on Liang-Barsky clipping
    p3 = -v[1]
    p4 = v[1]
    if ballP[1] > floorP[1]:
        q3 = (ballP[1]-ball.getRadius()) - (floorP[1] + floor.getHeight()*0.5)
        q4 = (floorP[1] + floor.getHeight()*0.5) - (ballP[1] - ball.getRadius())
    else:
        q3 = (ballP[1] + ball.getRadius()) - (floorP[1] - floor.getHeight()*0.5)
        q4 = (floorP[1] - floor.getHeight()*0.5) - (ballP[1] - ball.getRadius())

    if p4 == 0.0: # parallel traejectory to the wall
        return 1e+6

    if p3 < 0: # ball is heading in a +y direction
        if q3 > 0: # ball is headed away from the wall
            return 1e+6
        else: # ball is headed towards the wall
            return q3 / p3
    else: # ball is heading in a -y direction
        if q4 > 0: # ball is headed away from the wall
            return 1e+6
        else:
            return q4/p4

def collision_ball_floor(ball, floor, dt):
    tk = collisionTest_ball_floor(ball, floor)
    
    d = length(ball.getVelocity())
    if d == 0.0:
        return False

    delta = tk / (d * dt)
    if delta <= 1.0:
        ball.update(delta * dt)
        ball.setVelocity(ball.getVelocity()[0], -ball.getVelocity()[1])
        ball.update(dt - delta * dt)
        return True

    return False

def collisionTest_ball_ball(ball1, ball2):
    # Tests if there is a collision with another ball along the path of
    # the ball.  Returns the distance to the collision or 1e+6 (a big number)
    
    # Concept: hold ball2 still and test if ball1 will hit it
    # Ray-circle intersection
    v1 = ball1.getVelocity()
    p1 = ball1.getPosition()
    p2 = ball2.getPosition()
    r = ball1.getRadius() + ball2.getRadius()

    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    # quadratic equation
    a = v1[0]*v1[0] + v1[1]*v1[1]
    b = dx*v1[0] + dy*v1[1]
    c = dx*dx + dy*dy - r*r

    delta = b*b - a*c
    
    if  delta <= 0: # no intersection, imaginary roots
        return 1e+6

    deltaroot = math.sqrt(delta)
    t1 = (-b + deltaroot) / a
    t2 = (-b - deltaroot) / a

    if t1 < 0 and t2 < 0: # intersection is behind the ball
        return 1e+6

    # one of these could be negative
    tmin = min(t1, t2)

    # ball's already intersect, so move ball1 back to the boundary
    if t1 < 0 or t2 < 0:
        newpx = p1[0] + tmin*v1[0]
        newpy = p1[1] + tmin*v1[1]
        ball1.setPosition( newpx, newpy )
        return 0.0
        
    dx = tmin*v1[0]
    dy = tmin*v1[1]
    distToImpact = math.sqrt(dx*dx + dy*dy)

    return distToImpact
    

def collision_ball_ball(ball1, ball2, dt):
    distToImpact = collisionTest_ball_ball(ball1, ball2)

    vmag1 = length(ball1.getVelocity())
    if vmag1 == 0.0 or distToImpact > vmag1 * dt:
        return False

    delta = distToImpact / (vmag1 * dt)

    # Reset the ball's position to its initial position before updating
    initial_position = ball1.getPosition()
    ball1.setPosition(initial_position[0], initial_position[1])

    v1 = ball1.getVelocity()
    v2 = ball2.getVelocity()

    # Swap velocities only if ball1 is moving towards ball2
    if delta <= 1.0:
        if v1[0] * (ball2.getPosition()[0] - ball1.getPosition()[0]) > 0 and \
                v1[1] * (ball2.getPosition()[1] - ball1.getPosition()[1]) > 0:
            ball1.setVelocity(v2[0], v2[1])
            ball2.setVelocity(v1[0], v1[1])

    # Update the ball's position after the collision response
    ball1.update(dt - delta * dt)
    return True
def collisionTest_ball_block(ball, block):
    # Test if a ball is colliding with any side of a block, and indicate
    # which side. Sends out a line along the ball's velocity vector and
    # compares it with all four sides of the object.

    # get the trajectory and position of the ball
    v = unit( ball.getVelocity() )
    ballP = ball.getPosition()
    radius = ball.getRadius()

    # get the position of the block
    blockP = block.getPosition()

    # a variation on Liang-Barsky clipping
    # expands the block by the size of the ball before testing
    dx = block.getWidth()
    dy = block.getHeight()

    p = ( -v[0], v[0], -v[1], v[1] )
    q = (ballP[0] - (blockP[0] - dx*0.5 - radius),
         (blockP[0] + dx*0.5 + radius) - ballP[0],
         ballP[1] - (blockP[1] - dy*0.5 - radius),
         (blockP[1] + dy*0.5 + radius) - ballP[1] )


    # for all four cases
    tmin = -1e+6
    tmax = 1e+6
    side = -1
    sidemax = -1
    for i in range(4):
        if p[i] == 0.0: # no collision for this side of the block, motion is parallel to it
            if q[i] < 0: # outside the boundary of the box, no collision
                return 1e+6,0
            continue

        tk = q[i] / p[i]

        if p[i] < 0: # outside moving in
            if tk > tmin:
                tmin = tk
                side = i
        else:
            if tk < tmax:
                tmax = tk
                sidemax = i

        if tmax <= tmin: # no intersection with the box
            return 1e+6,0

    if tmin < 0 and tmax < 0: # both intersections behind the ball
        tmin = 1e+6
    elif tmin < 0 and tmax > 0: # ball is intersecting the block
        #print("ball is intersecting")

        # move the ball back along its velocity to the intersection point
        if v[0] == 0.0 and v[1] == 0.0:
            v = (1.0, 0.0)
            tmin = (blockP[0] - 0.5*dx - radius) - ballP[0]

        # move it to the closest side and set distance to impact to 0
        if -tmin < tmax:
            #print("setting position using tmin and velocity %.2f %d" % (tmin, side))
            ball.setPosition( ballP[0] + (tmin+1e-3)*v[0], ballP[1] + (tmin+1e-3)*v[1])
        else:
            #print("setting position using tmax and velocity %.2f %d" % (tmax, sidemax))
            ball.setPosition( ballP[0] + (tmax+1e-3)*v[0], ballP[1] + (tmax+1e-3)*v[1])
        tmin = 0

    # tmin is the closest intersection on side i
    # 0: coming up from below
    # 1: coming down from above
    # 2: coming from the left
    # 3: coming from the right
    return (tmin, side)


def collision_ball_block(ball, block, dt):
    distToImpact, side = collisionTest_ball_block(ball, block)

    vmag = length(ball.getVelocity())
    if vmag == 0.0 or distToImpact > vmag * dt:
        return False

    delta = distToImpact / (vmag * dt)

    # Reset the ball's position to its initial position before updating
    initial_position = ball.getPosition()
    ball.setPosition(initial_position[0], initial_position[1])

    v = ball.getVelocity()
    if side == 0 or side == 1:
        ball.setVelocity(v[0], abs(v[1]) * ball.getElasticity() * block.getElasticity())
        block.undraw()  # Undraw the block when a collision is detected
    elif side == 2 or side == 3:
        ball.setVelocity(abs(v[0]) * ball.getElasticity() * block.getElasticity(), v[1])
        block.undraw()  # Undraw the block when a collision is detected

    # Update the ball's position after the collision response
    ball.update((1 - delta) * dt)
    return True




def collisionTest_block_block(block1, block2):
    """Test if a block is colliding with any side of another block, and indicate
    which side. Sends out a line along the  moving block's velocity vector and
    compares it with all four sides of the object."""

    # get the trajectory and position of the ball
    v = unit( block1.getVelocity() )
    block1P = block1.getPosition()
    width1 = block1.getWidth()
    height1 =   block1.getHeight()
    

    # get the position of the block
    block2P = block2.getPosition()

    # a variation on Liang-Barsky clipping
    # expands the block by the size of the ball before testing
    dx = block1.getWidth()
    dy = block1.getHeight()

    dx2 = block2.getWidth()
    dy2 = block2.getHeight()

    p = ( -v[0], v[0], -v[1], v[1] )
    q = (block1P[0] - (block2P[0] - dx*0.5 - dx2*0.5),
         (block2P[0] + dx*0.5 + dx2*0.5) - block1[0],
         block1[1] - (block2P[1] - dy*0.5 - dy2*0.5),
         (block2P[1] + dy*0.5 + dy2*0.5) - block1P[1] )


    # for all four cases
    tmin = -1e+6
    tmax = 1e+6
    side = -1
    sidemax = -1
    for i in range(4):
        if p[i] == 0.0: # no collision for this side of the block, motion is parallel to it
            if q[i] < 0: # outside the boundary of the box, no collision
                return 1e+6,0
            continue

        tk = q[i] / p[i]

        if p[i] < 0: # outside moving in
            if tk > tmin:
                tmin = tk
                side = i
        else:
            if tk < tmax:
                tmax = tk
                sidemax = i

        if tmax <= tmin: # no intersection with the box
            return 1e+6,0

    if tmin < 0 and tmax < 0: # both intersections behind the ball
        tmin = 1e+6
    elif tmin < 0 and tmax > 0: # ball is intersecting the block
        #print("ball is intersecting")

        # move the ball back along its velocity to the intersection point
        if v[0] == 0.0 and v[1] == 0.0:
            v = (1.0, 0.0)
            tmin = (block1P[0] - 0.5*dx - dx2*0.5) - block1P[0]

        # move it to the closest side and set distance to impact to 0
        if -tmin < tmax:
            #print("setting position using tmin and velocity %.2f %d" % (tmin, side))
            block1.setPosition( block1P[0] + (tmin+1e-3)*v[0], block1P[1] + (tmin+1e-3)*v[1])
        else:
            #print("setting position using tmax and velocity %.2f %d" % (tmax, sidemax))
            block1.setPosition( block1P[0] + (tmax+1e-3)*v[0], block1P[1] + (tmax+1e-3)*v[1])
        tmin = 0

    # tmin is the closest intersection on side i
    # 0: coming up from below
    # 1: coming down from above
    # 2: coming from the left
    # 3: coming from the right
    return (tmin, side)
    
def collision_block_block(block1, block2, dt):
    distToImpact, side = collisionTest_block_block(block1, block2)

    vmag = length(block1.getVelocity())
    if vmag == 0.0 or distToImpact > vmag * dt:
        return False

    delta = distToImpact / (vmag * dt)
    block1.update(delta * dt)

    v = block1.getVelocity()
    if side == 0 or side == 1:
        block1.setVelocity(-v[0] * block1.getElasticity() * block2.getElasticity(), v[1])
        block2.undraw()  # Undraw the block when a collision is detected
    elif side == 2 or side == 3:
        block1.setVelocity(v[0], -v[1] * block1.getElasticity() * block2.getElasticity())
        block2.undraw()  # Undraw the block when a collision is detected

    block1.update((1 - delta) * dt)
    return True

def collision_balloon_block(balloon,block, dt):
    bblock = block(balloon.getWin())
    bblock.setPosition(balloon.getPosition()[0],balloon.getPosition()[1]+balloon.getSize()*balloon.getScale()++balloon.getSize()*balloon.getScale()*7)
    ball  = ball(balloon.getWin(),balloon.getSize()*balloon.getScale(),balloon.getPosition()[0],balloon.getPosition()[1] - balloon.getSize()*balloon.getScale())
    bblock.setHeight(balloon.getSize()*balloon.getScale()*4)

    return (collision_block_block(bblock, block, dt) or collision_ball_block(ball, block, dt))

collision_router = {}  #empty dictionary

#creating keys and storing proper functions as result of the dictionary
collision_router[ ('ball', 'ball') ] = collision_ball_ball   
collision_router[ ('ball', 'block') ] = collision_ball_block
collision_router[ ('ball', 'triangle') ] = collision_ball_block
collision_router[ ('triangle', 'triangle') ] = collision_block_block
collision_router[ ('triangle', 'ball') ] = collision_ball_block
collision_router[('triangle,','block')] = collision_block_block
collision_router[('ball', "pentagon")] = collision_ball_block

def collision(ball, thing, timestep):
    collision_router[('ball',thing.getType())](ball,thing,timestep)







    











