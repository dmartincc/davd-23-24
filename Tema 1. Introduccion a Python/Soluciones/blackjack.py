import random

class balckjack():

  def __init__(self):	
    self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]	
    self.dealerWin = 0  	
    self.playerWin = 0  	
    self.dealerLose = 0  	
    self.playerLose = 0  	
    self.playerChips = 100	
    self.games = 1
    
  def intro(self):
    print
    print(" -----------------------------------------------------------------------------")
    print(" |                * Welcome to the data-driven BACKJACK     *                |")
    print(" |                                                                           |")
    print(" |       You have 100 free chips for playing at our data-driven Casino       |")
    print(" |                                              created by: @dmartincc       |")
    print(" -----------------------------------------------------------------------------")

  def newgame(self):
    print(" ---------------------------------- HAND #{} -----------------------------------".format(self.games))

  def gameover(self):
    print(" --------------------------------- GAME OVER -----------------------------------")

  def shuffle(self):    
    card = random.randint(0,12)
    return self.cards[card]

  def countPoints(self, hand):    
    aces = hand.count(11)
    points = sum(hand)
    if points > 21 and aces > 0:
      while aces > 0 and points > 21:
        points -= 10
        aces -= 1
    return points

  def stats(self):
    print(" ----------------------------- STATS after {} hands ---------------------------".format(self.games))
    print("                    Player %   Dealer %")
    print(" Wins   -            {} %      {} %".format(round(self.playerWin*100/self.games,1), round(self.dealerWin*100/self.games,1)))
    print(" Chips  -              {} ".format(self.playerChips))

  def play(self):	

    while True: 

      player = []
      dealer = []

      playerBust = False
      dealerBust = False 

      self.newgame()
      
      player.append(self.shuffle())
      player.append(self.shuffle())
      
      dealer.append(self.shuffle())
      
      if self.playerChips == 0:
        print(" You have run out of chips. More luck next time!")
        self.gameover()
        False
        break
      
      playerBet = input(" How many chips do you want to bet from your {} chips (default = 1 chip): ".format(self.playerChips))		
      if playerBet:
        try:
          if int(playerBet) > 1 and int(playerBet) <= self.playerChips:
            playerBet = int(playerBet)
          elif int(playerBet) > self.playerChips:
            playerBet = input(" Please bet less than your {} chips:".format(self.playerChips))
            playerBet = int(playerBet)
          else:
            playerBet = 1
        except:
          playerBet = input(" Please enter a numeric number and bet less than your {} chips: ".format(self.playerChips))
          playerBet = int(playerBet)
      else:
        playerBet = 1  

      while True:
          playerPoints = self.countPoints(player) 
          dealerPoints = self.countPoints(dealer)   
          print                  
          print(" Player has these cards {} with a total value of {}".format(player, playerPoints))
          print(" Dealer has these cards {} with a total value of {}".format(dealer, dealerPoints))
          print
          if playerPoints > 21:
              print(" --> Player is busted!")
              playerBust = True                
              break
          elif playerPoints == 21:
              print("\a --> BLACKJACK!!!")                             
              break
          else:
              hitOrStand = input(" (H)it or (S)tand (type 'h' or 's'): ").lower()
              if 'h' in hitOrStand:
                  player.append(self.shuffle())
              else:
                  break
      while True:		    
          dealer.append(self.shuffle())

          while True:
              dealerPoints = self.countPoints(dealer)                
              if dealerPoints < 17:
                  dealer.append(self.shuffle())
              else:
                  break
          
          print
          print(" The dealer has {} for a total of {}".format(dealer, dealerPoints))
          print

          if dealerPoints > 21:
              print(" --> Dealer is busted!")
              dealerBust = True
              if playerBust == False:
                  print(" --> Player wins!")
                  self.playerChips = self.playerChips + playerBet
                  self.playerWin += 1
                  self.dealerLose += 1  

          elif dealerPoints > playerPoints:
              print(" --> Dealer wins!")
              self.playerChips = self.playerChips - playerBet
              self.dealerWin += 1
              self.playerLose += 1

          elif dealerPoints == playerPoints:
              print(" It's a draw!")

          elif dealerPoints < playerPoints:
              if playerBust == False:
                  print(" --> Player wins!")
                  self.playerChips = self.playerChips + playerBet
                  self.playerWin += 1
                  self.dealerLose += 1

              elif dealerBust == False:
                  print(" --> Dealer wins!")
                  self.playerChips = self.playerChips - playerBet
                  self.dealerWin += 1
                  self.dealerLose += 1
          break  
      
      self.stats()
      self.games += 1

      exit = input(" Press Enter or type (Q)uit: ").lower()
      if str(exit) == 'q':
          break

if __name__ == '__main__':

    g = balckjack()
    g.intro()
    g.play()