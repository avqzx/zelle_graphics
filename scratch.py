from graphics import *
def main():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(100,100), 50)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()

main()
