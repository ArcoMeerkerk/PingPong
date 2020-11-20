import math
import random

#scores [links, rechts]
scores = [0,0]

counter = 0
firstTime = True

#Width, height
barDimensions = [25, 100]

#List of bars -> x, y, width, height
bars = [[50, 250, barDimensions[0], barDimensions[1]], [700, 250, barDimensions[0], barDimensions[1]]]

defaultBallLocation = [400, 300]
#Properties of the ball: x, y, width, height
ball = [defaultBallLocation[0], defaultBallLocation[1], 25, 25]

#Velocity of the bars 0 and 1
velBars = [[0, 0], [0, 0]]
barSpeed = 15

#velBall
velBall = [0, 0]
ballSpeed = 4.0
ballAngles = [30, -30, 45, -45, 120, -120, 135, -135]
ballDirection = random.choice(ballAngles)

#w,s,up,down
keysPressed = [0, 0, 0, 0]

#Width, height
appSize = [800, 600]


def setup():
    # The size of the canvas
    size(appSize[0], appSize[1])

def draw():
    # Required to edit the value of counter
    global counter, ball, bars, velBars, velBall, ballDirection, keysPressed, scores, appSize, barSpeed, firstTime, ballSpeed
    
    #Left bar movement
    if keysPressed[0] and bars[0][1] > 0:
        velBars[0] = [0, -barSpeed]
    elif keysPressed[1] and bars[0][1] < appSize[1] - 100:
        velBars[0] = [0, barSpeed]
    else:
        velBars[0] = [0, 0]
    # Right bar movement
    if keysPressed[2] and bars[1][1] > 0:
        velBars[1] = [0, -barSpeed]
    elif keysPressed[3] and bars[1][1] < appSize[1] - 100:
        velBars[1] = [0, barSpeed]
    else:
        velBars[1] = [0, 0]

    #print(ball[1])

    if (bars[0][0] + bars[0][2] >= int(ball[0]) - ball[2] // 2 and bars[0][1] <= ball[1] and bars[0][1] + bars[0][3] >= ball[1]
    or bars[1][0] <= int(ball[0]) + ball[2] // 2 and bars[1][1] <= ball[1] and bars[1][1] + bars[1][3] >= ball[1]):
        ballDirection = (360-ballDirection)%360
        
    # Bounce on top and bottom
    if ball[1] - ball[3] / 2 < 0 or ball[1] + ball[3] / 2 > appSize[1] :
        ballDirection = (180-ballDirection)%360

    # Reset ball when leaving screen and update score counter
    if ball[0] + ball[3] <  0 or ball[0] - ball[3] > appSize[0] :
        if ball[0] + ball[3] <  0:
            scores[1] += 1
        elif ball[0] - ball[3] > appSize[0]:
            scores[0] += 1

        counter = 0
        ball[0] = defaultBallLocation[0]
        ball[1] = defaultBallLocation[1]
        ballSpeed += 0.3
        ballDirection = random.choice(ballAngles)

    #Ball movement x and y value
    if counter > 180 :
        velBall = [ballSpeed * math.sin(math.radians(ballDirection)), -ballSpeed * math.cos(math.radians(ballDirection))]

    # The color of the background
    background(0)
    # Fill color of all the elements
    fill(255, 255, 255)

    # Text with scores: left & right
    textAlign(LEFT)
    textSize(32)
    text(str(scores[0]), 125, 100)
    
    textAlign(RIGHT)
    textSize(32)
    text(str(scores[1]), appSize[0] - 125, 100)

    # Displaytext
    if scores[0] == 11 or scores[1] == 11:
        textAlign(CENTER)
        textSize(64)
        text("WON!", appSize[0] // 2, 100)
    # if firstTime :
    #     textAlign(CENTER)
    #     textSize(64)
    #     text(str(3 - counter // 60), appSize[0] // 2, 100)
        
    #     if counter > 180 :
    #         firstTime == False

    # Left bar: moves up or down
    rect(bars[0][0], bars[0][1], bars[0][2], bars[0][3])
    # Movement bar
    bars[0][0] += velBars[0][0]
    bars[0][1] += velBars[0][1]

    # Right bar: moves up or down
    rect(bars[1][0], bars[1][1], bars[1][2], bars[1][3])
    # Movement bar
    bars[1][0] += velBars[1][0]
    bars[1][1] += velBars[1][1]

    # Ball: moves right down
    ellipse(ball[0], ball[1], ball[2], ball[3])
    # Movement ball
    if counter > 180 and (scores[0] != 11 and scores[1] != 11):
        ball[0] += velBall[0]
        ball[1] += velBall[1]

    # Increase the counter
    counter = counter + 1

def keyPressed():
    global keysPressed
    if key == 'w':
        keysPressed[0] = 1
    elif key == 's':
        keysPressed[1] = 1
    if keyCode == UP:
        keysPressed[2] = 1
    elif keyCode == DOWN:
        keysPressed[3] = 1


def keyReleased():
    global keysPressed
    keysPressed = [0, 0, 0, 0]
