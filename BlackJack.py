#Chloe Nguyen - Phuong Ha Nguyen
#April 18, 2022
#COM 110 - Black Jack
#Black Jack class

from Deck import*



class BlackJack:
    """Attributes of this Blackjack class are as follows.

        dealerHand: a list of PlayingCard objects representing the dealer's hand

        playerHand: a list of PlayingCard objects representing the player's hand

        playingDeck: a Deck object representing the deck of cards the game is being played with"""
    
    def __init__(self, dHand = [], pHand = []):
        """Create a deck of cards, then shuffle it

             Set the initial list to contains the hands of both player and dealer later"""
        
        self.dealerHand = dHand
        self.playerHand = pHand
        self.playingDeck = Deck()
        self.playingDeck.shuffle()

    

    def initDeal(self, gwin, xposD, yposD, xposP, yposP):
         
        for i in range(2):
            playerCard = self.playingDeck.dealCard()
            self.playerHand.append(playerCard)
            
                #draw the card to the window
            playerCard.drawCard(gwin, xposP, yposP)
            xposP = xposP + 70
            
        for i in range(2):
            dealerCard = self.playingDeck.dealCard()
            self.dealerHand.append(dealerCard)
            
        #make the first dealer's card face down
        self.faceDown = Image(Point(xposD, yposD), "facedown.gif")
        self.faceDown.draw(gwin)
        
        xposD = xposD + 70
        #draw the second card
        dealerCard2 = self.dealerHand[1]
        dealerCard2.drawCard(gwin, xposD, yposD)
        xposD = xposD +70
            
        return self.playerHand, self.dealerHand, xposD, xposP

    def hit(self, gwin, xPos, yPos):
        """Give the user one more card when they click 'Hit'. Draw it on the graphic window"""
        #deal a new card for the player and append that card to player's hand
        newCard = self.playingDeck.dealCard()
        self.playerHand.append(newCard)

        newCard.drawCard(gwin, xPos, yPos)
        xPos = xPos + 70

        #return player's hand and the current x location 
        return self.playerHand, xPos

    def evaluateHand(self, hand):
        """Calculate the total value of the hands. Evaluate the value of the Ace card."""
        
        totalP = 0
        hasAce = False
        for card in hand:
            valueP = card.value()
            
            if valueP ==1:
                hasAce = True
                
            totalP = totalP + valueP
        
        #if there is an ace and the player hasn't busted yet, the ace counts as 11
        if ((totalP + 10) <= 21) and hasAce: 
            totalP = totalP +10
        
        return totalP

    def dealerPlays(self, gwin, xPos, yPos):

        """Function to handle Dealer's playing
            Dealer will stop after reaching soft 17"""

        #evaluate dealer's initial cards
        
        init1 = self.dealerHand[0]
        init2 = self.dealerHand[1]
        totalD = init1.value() + init2.value()
        #check if there is an ace in the first 2 cards
        if init1.value() == 1 or init2.value() == 1:
            hasAce = True
        else:
            hasAce = False
        #if the dealer reaches soft 17 with just 2 cards, return the score
        if 17 <= totalD+10 <= 21 and hasAce:
                totalD = totalD + 10
                return totalD
        #keep taking new cards until reaching soft 17
        while totalD<17:
    
            newCard = self.playingDeck.dealCard()
            newCard.drawCard(gwin, xPos, yPos)
            xPos = xPos + 70
            valueD = newCard.value()
            totalD = totalD + valueD

            if valueD == 1:
                hasAce = True
                
            #if the ace counts as 11 helps the dealer reach soft 17 and not busted
            if 17 <= totalD+10 <= 21 and hasAce:
                totalD = totalD + 10

        return totalD

        


def main():
    win = GraphWin("Black Jack", 800, 800)
    
    b = BlackJack()
    b.playerHand, b.dealerHand, xposD, xposP = b.initDeal(win, 200, 200, 600, 600)
    b.evaluateHand(b.dealerHand)
    print("The initial cards for the player is: \n")
    #for c in b.playerHand:
        
        #print(c.__str__())
    #print("\t -------------")
    #print("The initial cards for the dealer is: \n")
    
    #for c in b.dealerHand:
        #print(c.__str__())

    hit = input("\nDo you want to hit or stand? Type h or s. ")

    while hit == "h":
        b.playerHand, xposP = b.hit(win, xposP, 600)
        #print("Your current cards is: \n")
        for c in b.playerHand:
            print(c.__str__())
        hit = input("\nDo you want to hit or stand? Type h or s. ")

    b.totalP = b.evaluateHand(b.playerHand)
    print("\nYour score is: ", b.totalP)
    print("Dealer score is:", b.dealerPlays())
    
if __name__=="__main__":
    main()
    
                
            
            

        
            
        
