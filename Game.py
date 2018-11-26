import base, card_list

CARD_LIST = card_list.cards


class Main_Deck(base.Stack):
    """Main deck of cards for dealing"""
    def __init__(self):
        self.cards = []
        for card in CARD_LIST:
            self.add(card)
        import random
        random.shuffle(self.cards)

    def deal(self, players):
        while self.cards != []:
            for pers in players:
                if self.cards != []:
                    self.give(self.cards[0], pers)
                else:
                    break

class Game(object):
    def player_lose(self, player1, player2):
        end_game = None
        if player1.cards == []:
            end_game = True
        elif player2.cards == []:
            end_game = True
        return end_game

    def turn(self, p1, p2):
        print("\n\n")
        choice = p1.attribute_choice(p1.cards[0])
        print("Attacker...")
        print(p1.cards[0])
        print("Defender...")
        print(p2.cards[0])
        print(choice, "was chosen")
        if p1.call(p1.cards[0], choice) > p2.call(p2.cards[0], choice):
            p2.give(p2.cards[0], p1)
            n = "0"
            p1.move_front_card()
        elif p1.call(p1.cards[0], choice) < p2.call(p2.cards[0], choice):
            p1.give(p1.cards[0], p2)
            n = "1"
            p2.move_front_card()
        return n

    def message(self, message, player_turn):
        if player_turn == True:
            if message == "0":
                print("You win and take the enemy card!")
            elif message == "1":
                print("You lose and your card is taken!")
            else:
                print("Draw!")
        else:
            if message == "0":
                print("You lose and your card is taken!")
            elif message == "1":
                print("You win and take the enemy card!")
            else:
                print("Draw!")
                                    
    def main(self):
        end = "y"
        while end != "n":
            user = base.Player()
            ai = base.AI()
            deck = Main_Deck()
            players = [user, ai]
            deck.deal(players)
            print("Do you want to go first?")
            choice = user.ask_yn()
            player_turn = None
            if choice == "y":
                player_turn = True
            while self.player_lose(user, ai) != True:
                if player_turn == True:
                    p1 = user
                    p2 = ai
                else:
                    p1 = ai
                    p2 = user
                message = self.turn(p1, p2)
                self.message(message, player_turn)
                player_turn = not player_turn
                user.display_cards_left()
                ai.display_cards_left()
                input("\nPress enter to continue")
            if user.cards == []:
                print("\n\nYou lost!")
            else:
                print("\n\nYou win!")
            print("Do you want to play again?")
            end = user.ask_yn()
            


game = Game()
game.main()
input("Press enter to close.")
                


                    
                
                

            
        
        
        
        
        
        








        
            
            


