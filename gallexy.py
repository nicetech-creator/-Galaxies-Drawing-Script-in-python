import sys
import os
import turtle

WIDTH = 600
HEIGHT = 600
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"


#Draw Axes (function)
def screenCoor(x, y):
    Ratio = 300
    x0 = 300
    y0 = 300
    screenX = x0 + Ratio * x
    screenY = y0 + Ratio * y
    return screenX, screenY

def drawXAxisLabelTick(pointer, screenX, screenY, text):
        TICK = 5
        LABEL = 20
        pointer.goto(screenX, screenY)
        pointer.up()
        pointer.goto(screenX, screenY + TICK)
        pointer.down()
        pointer.goto(screenX, screenY - TICK)
        pointer.up()
        pointer.goto(screenX, screenY + LABEL)
        pointer.write(float(text), False, align = "center")
        pointer.goto(screenX, screenY)
        pointer.down()

def drawYAxisLabelTick(pointer, screenX, screenY, text):
        TICK = 5
        LABEL = 20
        pointer.goto(screenX, screenY)
        pointer.up()
        pointer.goto(screenX + TICK, screenY)
        pointer.down()
        pointer.goto(screenX - TICK, screenY)
        pointer.up()
        pointer.goto(screenX + LABEL, screenY)
        pointer.write(float(text), False, align = "center")
        pointer.goto(screenX, screenY)
        pointer.down()

def drawXAxis(pointer):
    xmin = 0
    xmax = float((WIDTH - 300) / 300)
    x = 0
    y = 0
    STEPX = 0.25
    screenX,screenY = screenCoor(x, y)
    pointer.up()
    pointer.goto(screenX, screenY)
    pointer.down()
    while screenX >= 0 :
        screenX,screenY = screenCoor(x, y)
        text = float(x)
        drawXAxisLabelTick(pointer, screenX, screenY, text)
        pointer.down()
        x = x - STEPX
    xmin = x + STEPX

    xmax = int((WIDTH - 300) / 300)
    x = 0
    y = 0
    STEPX = 0.25
    screenX,screenY = screenCoor(x, y)
    pointer.up()
    pointer.goto(screenX, screenY)
    pointer.down()
    while screenX <= WIDTH :
        screenX,screenY = screenCoor(x, y)
        text = float(x)
        drawXAxisLabelTick(pointer, screenX, screenY, text)
        pointer.down()
        x = x + STEPX
    xmax = x - STEPX
    return xmin, xmax

def drawYAxis(pointer):
    ymin = 0
    ymax = float((HEIGHT - 300)/300)
    x = 0
    y = 0
    STEPY = 0.25
    screenX,screenY = screenCoor(x, y)
    pointer.up()
    pointer.goto(screenX, screenY)
    pointer.down()
    while screenY >= 0 :
        screenX,screenY = screenCoor(x, y)
        text = float(y)
        drawYAxisLabelTick(pointer, screenX, screenY, text)
        pointer.down()
        y = y - STEPY
    ymin = y + STEPY

    ymax = float((WIDTH - 300)/300)
    x = 0
    y = 0
    STEPY = 0.25
    screenX,screenY = screenCoor(x, y)
    pointer.up()
    pointer.goto(screenX, screenY)
    pointer.down()
    while screenY <= HEIGHT :
        screenX,screenY = screenCoor(x, y)
        text = float(y)
        drawYAxisLabelTick(pointer, screenX, screenY, text)
        pointer.down()
        y = y + STEPY
    ymax = y - STEPY


def getColor(counter):
    NUMBERCOLOR = 3
    sColor = counter % NUMBERCOLOR
    if sColor == 0:
        return "red"
    elif sColor == 1:
        return "green"
    else:
        return "yellow"


#Read star information from file (function)
   

#Handle arguments
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)
    pointer.up()
    return pointer

def main():
    _names = False           # flag to print name or not
    stars_location_file = ''
    #Handle arguments
    if len(sys.argv) > 3:
        print ("Too many arguments.")
        sys.exit(1)
    _names = '-names' in sys.argv

    if _names == False and len(sys.argv) == 3:
        print ("Invalid argument as neither input was -names")
        sys.exit(1)
    
    if len(sys.argv) == 3:
        stars_location_file = sys.argv[sys.argv.index('-names') ^ 0x3]
    elif len(sys.argv) == 2 and not _names:
        stars_location_file = sys.argv[1]
    if stars_location_file == '':
        stars_location_file = input('Input start location file name:')
        pass    #prompt for file name

    print (stars_location_file, _names)

    #Read star information from file (function)
    pointer = setup()
    #Draw Axes (function)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer)
    drawYAxis(pointer)

    #Draw Stars (function)
    #Loop getting filenames
        #Read constellation file (function)
        #Draw Constellation (function)
      
        #Draw bounding box (Bonus) (function)

main()
