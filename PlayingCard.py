#Chloe Nguyen - Phuong Ha Nguyen
#April 9, 2022
#COM 110 - Project 5
#Playing Card Class

from random import randrange
from graphics import*

class PlayingCard:
    #place the functions inside a class makes it a method of PlayingCard class 
   
    def __init__(self, rank, suit): #name of card as a paramenter
        self.rank = rank
        self.suit = suit

    def getRank(self): #return the value of rank
        return self.rank

    def getSuit(self): #return the value of rank
        return self.suit

    def value(self): #set the value for JQK
        if self.rank >= 10:
            self.rank = 10

        return self.rank

    def __str__(self):
        #set up a list of ranks
        cards = ["","Ace", "Two", "Three", "Four", "Five", "Six", "Seven",\
                 "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        #set up a dictionary of the suits
        suitName = {"d":"Diamonds", "c":"Clubs", "h":"Hearts", "s":"Spades"}

        rank = self.getRank() #get the value of rank
        suit = self.getSuit() #get the value of suit

        #get the card name
        name = cards[rank] + " of " + suitName[suit]

        return name

    def drawCard(self, gwin, xPos, yPos):
        """Function to draw the card to the graphics window"""
        image = Image(Point(xPos, yPos), "playingcards/" + self.suit + str(self.rank) + ".gif")
        image.draw(gwin)
        
def main():
    #create a list of suit
    suits = ["c", "h", "d", "s"]
    
    n = int(input("How many cards do you want to generate? "))
    win = GraphWin("Test", 400,400)
    x = 100
    y = 100
    for i in range(n):
        r = randrange(1,14)
        s = suits[randrange(0,4)]
        c = PlayingCard(r, s)
        c.drawCard(win, x, y)
        x = x + 30

if __name__ == "__main__":
    main()
