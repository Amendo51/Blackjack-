import random

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(i,j))
    def __str__(self):
        list_of_cards = []
        for card in self.cards:
            list_of_cards.append(str(card))
        return str(list_of_cards)
    def deal_card(self,person,card= 0):
        person.cards.append(self.cards.pop(card))
    def shuffle(self):
        random.shuffle(self.cards)


class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        self.score = value + 1
        if value + 1 > 10:
            self.score = 10



    suits = ["Spades", "Clubs", "Hearts"," Diamonds"]
    values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __str__(self):
        return '%s of %s'%(Card.values[self.value],Card.suits[self.suit])
def spades(Deck):
    def Spades(self,card= 0):
        self.New_Deck = []
        self.New_Deck.append(self.card.pop(card))
        return str(self.New_Deck)



class Player(Deck):
    def __init__(self):
        self.cards = []
    def score(self):
        x = 0
        for i in self.cards:
            x += i.score
        return x
    def play(self,D):
        for i in range(2):
            D.deal_card(self)
        print(self)
        print(self.score())
        hitting = True
        for i in self.cards:
            if i.value == 0:
                i.score = int(input('Declare your ace'))
        while hitting:

            go = input('Do you want to hit? y/n',)
            if go == 'y':
                D.deal_card(self)
                print(self)
                if self.cards[-1].value == 0:
                    self.cards[-1].score = int(input('Declare your ace'))
                print(self.score())
                if self.score() == 21:
                    print('Good Job you fool')
                    hitting == False
                if self.score() > 21:
                    hitting = False
                    print('You fool you busted')
            else:
                hitting = False

class Dealer(Player):
    #dealer has to hit if the have less than 17 point
    def __init__(self):
        self.cards = []

    def score(self):
        x = 0
        for i in self.cards:
            x += i.score
        return x

    def play(self, D):
        for i in range(2):
            D.deal_card(self)
        print(self)
        print(self.score())
        hitting = True
        for i in self.cards:
            if i.value == 0:
                i.score = 11
        while hitting:
                go = input('Do you want to hit? y/n')
                if self.score() >= 17:
                        hitting = False
                        print('You fool you cant take anymore')
                elif go == 'y':
                    D.deal_card(self)
                    print(self)
                    if self.cards[-1].value == 0:
                        self.cards[-1].score = int(input('Declare your ace'))
                    print(self.score())
                    if self.score() == 21:
                        print('Good Job you fool')
                        hitting == False
                    if self.score() > 21:
                        hitting = False
                        print('You fool you busted')
                else:
                    hitting = False


    







def blackjack(player1,player2,dealer):
    D = Deck()
    D.shuffle()
    print('player 1 is playing')
    player1.play(D)
    print('player 2 is playing')
    player2.play(D)
    print('dealer is playing')
    dealer.play(D)
    twenty = 21

    one = twenty - player1.score()
    two = twenty - player2.score()
    dea = twenty - dealer.score()
    list = [one,two,dea]


    if list.index(min(list)) == 0:
        print('player 1 won')
    if list.index(min(list)) == 1:
        print('player 2 won')
    if list.index(min(list)) == 3:
        print('dealer won')

    #func to see who won




micah = Player()
jeff = Player()
tony = Dealer()
blackjack(micah,jeff,tony)
