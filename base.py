#Rules for cards and decks


class Card(object):
    """Cards used for play"""
    def __init__(self, name, toughness, shooting, melee, leadership):
        self.name = name
        self.toughness = toughness
        self.shooting = shooting
        self.melee = melee
        self.leadership = leadership

    def __str__(self):
        n = "Name: " + self.name
        t = "Toughness: " + str(self.toughness)
        s = "Shooting: " + str(self.shooting)
        m = "Melee: " + str(self.melee)
        l = "Leadership: " + str(self.leadership)
        att = (n, t, s, m, l)
        rep = ""
        for attrib in att:
            rep += attrib + "\n"
        return rep

class Stack(object):
    """A stack of cards"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ""
        for card in self.cards:
            rep += str(card) + "\n"
        return rep
    
    def add(self, card):
        self.cards.append(card)

    def give(self, card, person):
        self.cards.remove(card)
        person.add(card)

class Player(Stack):
    """Player in the game, human"""
    def attribute_choice(self, card):
        print(self.cards[0])
        choices = ("1", "2", "3", "4")
        choice = None
        while choice not in choices:
            choice = input("Choose and attribute (1-4): ")       
        return choice

    def call(self, card, choice):
        if choice == "1":
            attribute = card.toughness
        elif choice == "2":
            attribute = card.shooting
        elif choice == "3":
            attribute = card.melee
        elif choice == "4":
            attribute = card.leadership
        return attribute

    def move_front_card(self):
        n = self.cards[0]
        self.cards = self.cards[1:]
        self.add(n)

    @property
    def no_cards(self):
        return self.cards == []

    def lose(self):
        n = None
        if self.no_cards == True:
            n = True
        return n

    def ask_yn(self):
        choice = ""
        while choice.lower() not in ("y", "n"):
            choice = input("Input answer(y/n): ")
        return choice.lower()

    def cards_left(self):
        n = 0
        for card in self.cards:
            n += 1
        return n

    def display_cards_left(self):
        n = self.cards_left()
        print("You have", str(n), "cards left.")
        
        

class AI(Player):
    """Redo pick attribute to AI control"""
    def attribute_choice(self, card):
        choices = [card.toughness, card.shooting, card.melee, card.leadership]            
        choices.sort(reverse=True)
        attribute = choices[0]
        if attribute == card.toughness:
            choice = "1"
        elif attribute == card.shooting:
            choice = "2"
        elif attribute == card.melee:
            choice = "3"
        elif attribute == card.leadership:
            choice = "4"
        return choice

    def display_cards_left(self):
        n = self.cards_left()
        print("Your oppenent has", str(n), "cards left.")
    
            
        


            
            
        
    

    








    
