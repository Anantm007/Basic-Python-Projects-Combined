import random


suits=['Diamond','Hearts','Clubs','Spades']

val=['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']

ranks={'Ace':11,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}

class Card():
    
    def __init__(self,suit,val):
        self.suit=suit
        self.val=val
        
    def __str__(self):
        return(f'{self.val} of {self.suit}')
    
class Hand:
    
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
        
    def add_cards(self,card):
        self.cards.append(card)
        self.value+=ranks[card.val]

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class player():
    
    def __init__(self,name,chips=0,deck=[]):
        self.name=name
        self.chips=chips
        
    def __str__(self):
        return("\nName : {} \nAvailable Chips : {}".format(self.name,self.chips))

def show_some(player_hand,dealer_hand):
    
    print("\n\nDealer's Hand ")
    print('<Card Hidden>')
    print(dealer_hand.cards[1])
    
    print("\n\nPlayer's Hand")
    
    for item in player_hand.cards:
        print(item)

def show_all(player_hand,dealer_hand):
    
    print("\n\nDealer's Hand ")
    for item in dealer_hand.cards:
        print(item)
    
    print("\n\nPlayer's Hand")
    
    for item in player_hand.cards:
        print(item)

def bust_check(player_hand,dealer_hand):
    if player_hand.value>21 or dealer_hand.value>21:
        return True
    
    else:
        return False

def win_check(p,player_hand,dealer_hand,bet):
    if player_hand.value==21 and dealer_hand.value==21:
        print('\n\nGAMES ENDS IN A TIE!!')
        
    
    elif player_hand.value==21:
        print('\n\nPLAYER WINS')
        p.chips+=2*bet
        
    elif dealer_hand.value==21:
        print('\n\nDEALER WINS')
        
    
    elif player_hand.value>dealer_hand.value:
        print('\n\nPLAYER WINS!!')
        p.chips+=2*bet
    
    elif player_hand.value<dealer_hand.value:
        print('\n\nDEALER WINS')

def player_play(p,player_hand,dealer_hand,deck):
    
    while True:
        
            choice=input('\n\nDo you want to hit or stand? (h/s)     -   ')
            
            if choice.lower()=='h':
                
                player_hand.add_cards(deck.deal())
                show_some(player_hand,dealer_hand)
                
                # CHECKING IF PLAYER HAS BUSTED
                if bust_check(player_hand,dealer_hand):
                    
                    show_all(player_hand,dealer_hand)
                    print('\nPLAYER LOSES..')
                    f=1     # DEALER WILL NOT PLAY
                    return False
                
                    
            
            elif choice.lower()=='s':
                print('\n\nDEALER TO PLAY NOW')
                return True
            
            else:
                print('\nWRONG CHOICE!!')


def dealer_play(p,player_hand,dealer_hand,deck,bet):
      
    while True:
        
        if dealer_hand.value>17:
            return True
                    
        dealer_hand.add_cards(deck.deal())
                
        if player_hand.value == 21 and dealer_hand.value==21:
            print('\n\nGAME ENDS IN A DRAW')
            show_all(player_hand,dealer_hand)
            p.chips+=bet
            return False
                    
        if bust_check(player_hand,dealer_hand):
            show_all(player_hand,dealer_hand)
            print('\n\nPLAYER WINS..')
            p.chips+=2*bet
            return False
                    
        if dealer_hand.value>17:
            return True
        
def play():
    
    match=1
    
    while True:
               
        print("\t\tWELCOME TO THE BLACKJACK CARD GAME\n\n")

        
        # IF IT IS THE FIRST MATCH THEN ASK FOR PLAYER DETAILS
        if match==1:
            
            s=input("Please enter your name   -    ")
            
            try:
                n=int(input("Please enter the amount of initial chips you want    -    "))
            except :
                print("\nHey, that's invalid....Please enter again!!")
            else:
                print("\nThank you, we are now starting the game")    
                p=player(s,n)
                print(p)
                
                
        
        # PLAY BEGINS FROM HERE   
        while True:
            bet=int(input("Please Enter the value of your bet    -    "))
            
            if bet>p.chips or bet<0:
                print("\nSorry, invalid chips...\n")
            else:
                p.chips-=bet
                match+=1
                break
                
       
        print(p)
        
        # SHUFFLING AND INITIAL DISTRIBUTION OF CARDS
        deck=Deck()
        deck.shuffle()
        
        player_hand=Hand()
        player_hand.add_cards(deck.deal())
        player_hand.add_cards(deck.deal())
        
        
        dealer_hand=Hand()
        dealer_hand.add_cards(deck.deal())
        dealer_hand.add_cards(deck.deal())
        
        # SHOWING INITIAL CARDS
        show_some(player_hand,dealer_hand)
        
        print('\n\nPLAYER TO PLAY FIRST')
        
        # PLAYER TO START PLAY NOW
        
        if player_play(p,player_hand,dealer_hand,deck)==True:
         
            if dealer_play(p,player_hand,dealer_hand,deck,bet) == True:   # DEALER WILL PLAY NOW AS PLAYER HAS NOT BUSTED AND DECIDED TO STAND
                win_check(p,player_hand,dealer_hand,bet)
                show_all(player_hand,dealer_hand)
                
        
        print(f"\nPLAYER'S TOTAL   =    {player_hand.value}")
        print(f"\nDEALER'S TOTAL   =    {dealer_hand.value}")
        
        print('\n')
        print(p)
        
        again=input("\nThank you, do you want to play again? (y/n)  -    ")
        if again.lower()=='n':           
            break

play()