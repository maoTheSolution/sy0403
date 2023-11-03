import turtle as tt
import random as rd


def init(col, xSize, ySize):
    '''
    set-up at the beginning
    '''
    global window, pen
    window = tt.Screen()
    window.bgcolor(col)
    window.screensize(xSize, ySize)
    pen = tt.Turtle()


def changeBGColor(newCol):
    '''
    change the bgcolor
    '''
    global window
    window.bgcolor(newCol)

def changeWindowSize(xSize, ySize):
    '''
    change the size of the window
    '''
    global window
    window.screensize(xSize, ySize)

def move(xPos, yPos):
    global pen
    pen.penup()
    pen.goto(xPos, yPos)
    pen.pendown()
    
def randomMove():
    global pen
    pen.penup()
    xPos = rd.randint(-250, 250)
    yPos = rd.randint(-250, 250)
    pen.goto(xPos, yPos)
    pen.pendown()

def sizeSelector() -> int:
    global window, pen
    xTemp = abs(window.screensize()[0]/2) - abs(pen.pos()[0])
    yTemp = abs(window.screensize()[1]/2) - abs(pen.pos()[1])

    if xTemp > yTemp:
        return yTemp/2
    else:
        return xTemp/2

def drawCircle():
    global pen
    pen.circle(sizeSelector()/2)





if __name__ == "__main__":
    init("white", 700, 700)

    for each in range(10):
        randomMove()
        drawCircle()
    tt.done()





