# convert_gui.pyw
# Program to convert Celsius to Fahrenheit using a simple
#   graphical interface.

from graphics import *

def main():
    win = GraphWin("Celsius Converter", 300, 200)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Draw the interface
    Text(Point(1,3), "   Celsius Temperature:").draw(win)
    Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
    input = Entry(Point(2,3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)
    clickBox= Rectangle(Point(1,1.5), Point(2,2.5))

    # wait for a mouse click

    def successAction():
            # convert input
            celsius = eval(input.getText())
            fahrenheit = 9.0/5.0 * celsius + 32

            # display output and change button
            output.setText(fahrenheit)
            button.setText("Quit")
                    
            # wait for click and then quit
            win.getMouse()
            win.close()
           
    for i in range(10000):
        click1= win.getMouse()
        X= click1.getX()
        Y=click1.getY()
        leftSide=1
        rightSide=2
        top=2.5
        bottom=1.5
    
        if X>leftSide:
            if X<rightSide:
                if Y>bottom:
                    if Y<top:
                     successAction();
                    else:
                        Text(Point(2,1),"Click convert")
                        continue
                else:
                    Text(Point(2,1),"Click convert")
                    continue
            else:
                Text(Point(2,1),"Click convert")
                continue
        else:
            Text(Point(2,1),"Click convert")
            continue

                       
    
            
    
  
        
    
    
        

main()
