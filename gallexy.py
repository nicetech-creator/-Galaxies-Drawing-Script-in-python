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
        text = float(x)
        drawXAxisLabelTick(pointer, screenX, screenY, text)
        pointer.down()
        x = x - STEPX
        screenX,screenY = screenCoor(x, y)
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
        text = float(x)
        drawXAxisLabelTick(pointer, screenX, screenY, text)
        pointer.down()
        x = x + STEPX
        screenX,screenY = screenCoor(x, y)
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
        text = float(y)
        drawYAxisLabelTick(pointer, screenX, screenY, text)
        pointer.down()
        y = y - STEPY
        screenX,screenY = screenCoor(x, y)
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
        text = float(y)
        drawYAxisLabelTick(pointer, screenX, screenY, text)
        pointer.down()
        y = y + STEPY
        screenX,screenY = screenCoor(x, y)
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
def ReadStarts(strFileName):
    if not os.path.isfile(strFileName):
        print ("Invalid Data file path.")
        sys.exit(1)
    try:
        starfile = open(strFileName)
        stars = starfile.readlines()
        star_data = []                  # list for all star tuples
        named_stars = {}                # a dictionary for named stars
        for star in stars:
            words = star.split(',')
            words = [w.strip() for w in words if len(w.strip()) > 0]
            if len(words) < 6 or len(words) > 7:
                raise Exception('Woring data format and we are not able to accept this file')
            s =( float(words[0]), float(words[1]), float(words[4]) )
            names = []
            if len(words) == 7: #when named star
                names = words[-1].split(';')
                print ('{0} is at ({1}, {2}) with magnitude {3}'.format(names[0].strip(), s[0], s[1], s[2]))
                for name in names:
                    named_stars[name.strip()] = s
            star_data.append((s[0], s[1], s[2], names))
        starfile.close()

        return (star_data, named_stars)
    except:
        print ("Some format error occures in your star file")
        sys.exit(1)
    
#Draw stars from given data
def DrawStars(pointer, _stars, _names):
    """
    in : 
        pointer: turtle pointer
        _stars : array of tuples (x, y, mag, names:array)
        _names : flag to indicate to draw name or not
    """
    for star in _stars:
        screenX,screenY = screenCoor(star[0], star[1])
        pointer.up()
        pointer.goto(screenX,screenY)
        pointer.down()
        if len(star[3]) > 0:#named star
            pointer.color(STARCOLOR)
            if _names == True:
                pointer.write(star[3][0],font=("Arial", 5, "normal"))
        else:
            pointer.color(STARCOLOR2)
        radius = (10 / (star[2] + 2)) / 2
        pointer.begin_fill()
        pointer.circle(radius)
        pointer.end_fill()


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
    AllStars, NamedStars = ReadStarts(stars_location_file)



    pointer = setup()
    #Draw Axes (function)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer)
    drawYAxis(pointer)

    #Draw Stars (function)
    DrawStars(pointer, AllStars, _names)
    #Loop getting filenames
        #Read constellation file (function)
        #Draw Constellation (function)
      
        #Draw bounding box (Bonus) (function)
    a = input()

main()
