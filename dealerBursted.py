#Dealer Bursted
#Chloe Nguyen Aug 9 2022
#calculate the probability of dealer being busted given the first card

from random import *
class DealerBustedProb:
    """ class to calculate probability of dealer being busted given the first card"""
    def __init__(self, n, initCard):
        self.num = n
        self.value = initCard # the value of the first card

    def getBustedProb(self):

        def dealerBusts(self):

            initialcard = self.value
            
            if initialcard>10: #JQK = 10
                initialcard=10

                #Check if the initial card is an ace or not
            if initialcard!=1:
                hasAce=False
            else:
                hasAce=True
            total=initialcard
            
            #if total is smaller than 17, keep taking new cards until they reach soft 17
            while total<17:
                newCard=randrange(1,14) #choose a random number between 0 and 12 
                if newCard>10:
                    newCard=10
                total=total+newCard
                ##if there is an ace
                
                
                if newCard==1: #if there is an ace
                    hasAce=True
                if 17<=total+10<=21 and hasAce: #if the dealer hasn't busted
                    total=total+10 #the ace counts as 11

            if total>21:
                
                return True
            else:
                
                return False

            
        totalBustedGames = 0
        #do this n times:
        for i in range(self.num):
            ### Simulate game with the given initial showing card and see if dealer busts
            if dealerBusts(self): 
                #add one to the total number of busted games
                totalBustedGames += 1

        prob = totalBustedGames/self.num

        return int(prob*100)

        

   
        

def main():
    my = DealerBustedProb(100000, 1)
    print(round(my.getBustedProb(), 2))
    
if __name__ == "__main__":
    main()
    
        
