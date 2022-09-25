#Chloe Nguyen - Phuong Nguyen
#Flapy Bird Project
#May 4, 2022

from graphics import*
from time import*
from random import randrange

class Pipe:
    """Class to initiate pipes with given space and speed"""
    def __init__(self, xPos, yPos, win, space, speed):
        """Constructor method to create pipes"""
        self.xPos = xPos
        self.yPos = yPos #the center of the space between two pipes
        self.speed = speed #the speed of the pipes

        pipe = Image(Point(xPos, self.yPos), "img/pipe1.png")
        
        #only to have the size of the image do not draw to the window
        pipe_length = pipe.getHeight()/10
        self.width = pipe.getWidth()/10
        #the distance from the center of the space to the center of the pipe
        dis = (space + pipe_length)//2

        #y position of the upper pipe
        y1 = self.yPos-dis
        #y position of the lower pipe
        y2 = self.yPos+ dis
        
        self.pipe1 = Image(Point(self.xPos, y1), "img/pipe1.png")
        self.pipe1.draw(win)
        self.pipe2 = Image(Point(self.xPos, y2), "img/pipe2.png")
        self.pipe2.draw(win)

        
    def move(self):
        """method to move the pipes"""
        self.pipe1.move(-1, 0)
        self.pipe2.move(-1, 0)
        self.xPos -= 1
        
        sleep(self.speed)
        return self.xPos
        

    def undraw(self):

        """method to undraw the pipes""" 
        self.pipe1.undraw()
        self.pipe2.undraw()
    
def main():
    win = GraphWin("Flappy Bird", 600, 600)
    win.setCoords(0, 0, 60, 60)
    xPos = 62
    
    

    while True:
        
        pipeY = randrange(15, 45)
        
        pipes = Pipe(xPos, pipeY, win, 7, 0.03)
        while int(pipes.xPos) > -2:
            pipes.xPos = pipes.move()
        pipes.undraw()
        
if __name__ == "__main__":
    main()
    
