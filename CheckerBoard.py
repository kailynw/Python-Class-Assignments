from graphics import *
win=GraphWin("Chess Board",500,500)
win.setCoords(-4,-4,4,4)


for i in range(4,-4,-1):
    
    Rectangle(Point(-i,-i),Point(-i+1,-i+1)).draw(win)
    Rectangle(Point(-i,-i),Point(-i+2,-i+2)).draw(win)
    Rectangle(Point(-i,-i),Point(-i+3,-i+3)).draw(win)
    Rectangle(Point(-i,-i),Point(-i+4,-i+4)).draw(win)
    Rectangle(Point(-i,-i),Point(-i+5,-i+5)).draw(win)
    Rectangle(Point(-i,-i),Point(-i+6,-i+6)).draw(win)
    Rectangle(Point(-i,-i),Point(-i+7,-i+7)).draw(win)
    Rectangle(Point(-i,-i),Point(-i+8,-i+8)).draw(win)

for i in range(4,-4,-1):
    ### Doesnt Work
    Rectangle(Point(-i,-i),Point(-i+1,-i+1)).setFill("black")
    Rectangle(Point(-i,-i),Point(-i+2,-i+2)).setFill("white")
    Rectangle(Point(-i,-i),Point(-i+3,-i+3)).setFill("black")
    Rectangle(Point(-i,-i),Point(-i+4,-i+4)).setFill("white")
    Rectangle(Point(-i,-i),Point(-i+5,-i+5)).setFill("black")
    Rectangle(Point(-i,-i),Point(-i+6,-i+6)).setFill("white")
    Rectangle(Point(-i,-i),Point(-i+7,-i+7)).setFill("black")
    Rectangle(Point(-i,-i),Point(-i+8,-i+8)).setFill("white")
#############################################################
rect1=Rectangle(Point(-4,-4),Point(-3,-3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-3,-3),Point(-2,-2))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-2,-2),Point(-3,-3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-2,-2),Point(-1,-1))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-1,-1),Point(0,0))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(0,0),Point(1,1))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(1,1),Point(2,2))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(2,2),Point(3,3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(3,3),Point(4,4))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(4,4),Point(5,5))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(5,5),Point(5,5))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(5,5),Point(6,6))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(6,6),Point(7,7))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(7,7),Point(8,8))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-4,-4),Point(-3,-3))
rect1.draw(win)
rect1.setFill("black")
##################################################
rect1=Rectangle(Point(-2,-4),Point(-1,-3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-1,-3),Point(0,-2))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(0,-2),Point(1,-1))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(1,-1),Point(2,0))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(1,1),Point(2,2))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(2,0),Point(3,1))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(3,1),Point(4,2))
rect1.draw(win)
rect1.setFill("black")
######################################################
rect1=Rectangle(Point(2,4),Point(1,3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(1,3),Point(0,2))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(0,2),Point(-1,1))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-1,1),Point(-2,0))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-1,-1),Point(-2,-2))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-2,0),Point(-3,-1))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-3,-1),Point(-4,-2))
rect1.draw(win)
rect1.setFill("black")
###########################################################    
rect1=Rectangle(Point(0,-4),Point(1,-3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(1,-3),Point(2,-2))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(2,-2),Point(3,-1))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-1,1),Point(-2,0))
rect1.draw(win)
rect1.setFill("black")


rect1=Rectangle(Point(3,-1),Point(4,0))
rect1.draw(win)
rect1.setFill("black")
#########################################################
rect1=Rectangle(Point(0,4),Point(-1,3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-1,3),Point(-2,2))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-2,2),Point(-3,1))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(1,-1),Point(2,0))
rect1.draw(win)
rect1.setFill("black")


rect1=Rectangle(Point(-3,1),Point(-4,0))
rect1.draw(win)
rect1.setFill("black")
#######################################################
rect1=Rectangle(Point(2,-4),Point(3,-3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(3,-3),Point(4,-2))
rect1.draw(win)
rect1.setFill("black")

######################################################
rect1=Rectangle(Point(-2,4),Point(-3,3))
rect1.draw(win)
rect1.setFill("black")

rect1=Rectangle(Point(-3,3),Point(-4,2))
rect1.draw(win)
rect1.setFill("black")

win.getMouse()
win.close()
