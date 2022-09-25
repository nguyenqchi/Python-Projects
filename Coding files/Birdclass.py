#Phuong Nguyen - Chloe Nguyen
#Flappy Bird Project
#May 4, 2022

from graphics import*
from time import*

class Bird:
    """Class to create the bird"""
    def __init__(self, point, win, speed, character):
        "Constructor method"""
        self.win = win
        self.speed = speed
        self.xPos = point.getX()
        self.yPos = point.getY()

        #different characters
        if character == "squirrel":
            self.bird = Image(point, "img/squirrel.png")
        elif character == "fish":
            self.bird = Image(point, "img/fish.png")
        else:
            self.bird = Image(point, "img/bird.png")
        self.height = self.bird.getHeight()/10
        self.bird.draw(self.win)
        
    def fly(self):
        """method to make the bird fly"""
        self.bird.move(0, 3)
        self.yPos +=3
        sleep(self.speed)
        
    def fall(self):
        """method to make the bird fall"""
        self.bird.move(0, -1)
        self.yPos -= 1
        sleep(self.speed)

    def getPos(self):
        """method to get the current position of the bird"""
        bottom = int(self.yPos + self.height/2)
        top = int(self.yPos - self.height/2)
        return bottom, top, self.xPos
       
def main():
    win = GraphWin("Flappy Bird", 600, 600)
    win.setCoords(0,0, 60, 60)
    bird = Bird(Point(5, 20), win, 0.05, "bird")
    bottom, top, bird_x = bird.getPos()
    command = win.checkKey()
    
    while bottom > 0 and top < 60:
        
        fall = True
        if command == "space":
            fall = False
        if fall:
            bird.fall()
        else:
            bird.fly()
        command = win.checkKey()
        bottom, top, bird_x = bird.getPos()
        
    win.close()
if __name__ == "__main__":
    main()
