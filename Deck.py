#Chloe Nguyen - Phuong Ha Nguyen
#COM 110 - Project 5 - BlackJack
#April 9
#Deck Class

from PlayingCard import*
import random

class Deck:
    
    def __init__(self):
        """Initial function to create a deck"""
        
        self.cards = []
        suits = ["d", "c", "h", "s"]
        for s in suits:
            for i in range(1,14):
                card = PlayingCard(i, s)
                self.cards.append(card)
                
    def shuffle(self):
        """Function to shuffle the deck"""
        random.shuffle(self.cards)
        
    def dealCard(self):
        """Function to deal cards"""
        #taking the last card in the deck
        card = self.cards[-1]
        del self.cards[-1]

        return card

    def cardsLeft(self):

        count = len(self.cards)

        return count

def main():
    cards = Deck()
    cards.shuffle()
    card = cards.dealCard()
    print(card)
    print(cards.cardsLeft())

    for c in cards.cards:
        print(c.__str__())

if __name__ == "__main__":
    main()
                
                
