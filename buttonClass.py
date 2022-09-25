#Chloe Nguyen - Phuong Ha Nguyen
#COM 110 - Project 5
#Button Class
#April 18,2022


from graphics import*
class Button:
#the goal of the class is to create button objects
    #constructor method, always the first one you write in a class definition
    def __init__(self, win, center, width, height, label, color = "white"):

        """create a button where win is the GraphWin where the button will be drawn
        center will be a point object were the button is centered
        width is an integer that is the width of the button, height is an integer that is the height of the button
        label is a string that will appear on the button"""
        
        x, y = center.getX(), center.getY()
        self.xmin = x - width/2
        self.xmax = x + width/2
        self.ymin = y - height/2
        self.ymax = y + height/2
        
        pt1=Point(self.xmin, self.ymin)
        pt2=Point(self.xmax, self.ymax)
        self.rect = Rectangle(pt1, pt2)
        self.rect.draw(win)
        self.rect.setFill(color)
        self.words = Text (center, label)
        self.words.draw(win)
        self.words.setFace("courier")
        self.words.setStyle("bold")
        self.active = True
    def deactivate(self):
        """Set the button to deactivated so it is not clickable"""
        ##color text gray
        self.words.setTextColor("gray")
        ##set the outline to be thinner
        self.rect.setWidth("1")
        ##set the boolean flag self.active to False
        self.active = False
    def activate(self):
        """Set the button to activated so it is clickable"""
        
        #set the color of the label to "black"
        self.words.setTextColor("black")
        #set the outline to look bolder
        self.rect.setWidth("2")
        #set the boolean floag self.active to True
        self.active = True

    def isClick(self, pt):
        """return True if pt is in the boundary of the button, return False otherwise"""
        #if the point is inside the button and the button is activated
        if self.active and (self.xmin <= pt.getX() <= self.xmax) \
        and (self.ymin <= pt.getY() <= self.ymax):
            return True
        else:
            return False
def main():
    gwin=GraphWin("Roll the dice", 400, 400)
    #to create object of a class the syntax is follow
    # variable_name = className(parameter)
    button1 = Button(gwin, Point(200,250), 80, 40, "Roll Dice")
    button2 = Button(gwin, Point(200,350), 80, 40, "Quit")
    button1.activate()
    button2.deactivate()
    point = gwin.getMouse()
    while not button1.isClick(point):
        point = gwin.getMouse()
    button2.activate()
    while not button2.isClick(point):
        point = gwin.getMouse()
    gwin.close()
if __name__ == "__main__":
    
    main()
