import random, time
import sys
class Card:
    cards_value = {'2C' : 2, '2D' : 2, '2H' : 2, '2S' : 2, '3C' : 3, '3D' : 3, '3H' : 3, '3S' : 3, '4C' : 4, '4D' : 4, '4H' : 4, '4S' : 4, '5C' : 5, '5D' : 5, '5H' : 5, '5S' : 5, '6C' : 6, '6D' : 6, '6H' : 6, '6S' : 6, '7C' : 7, '7D' : 7, '7H' : 7, '7S' : 7, '8C' : 8, '8D' : 8, '8H' : 8, '8S' : 8, '9C' : 9, '9D' : 9, '9H' : 9, '9S' : 9, '10C' : 10, '10D' : 10, '10H' : 10, '10S' : 10, 'JC' : 10, 'JD' : 10, 'JH' : 10, 'JS' : 10, 'QC' : 10, 'QD' : 10, 'QH' : 10, 'QS' : 10, 'KC' : 10, 'KD' : 10, 'KH' : 10, 'KS' : 10, 'AC' : 11, 'AD' : 11, 'AH' : 11, 'AS' : 11}
    is_busted = False
    cards_available = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', '10C', '10D', '10H', '10S', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH', 'QS', 'KC', 'KD', 'KH', 'KS', 'AC', 'AD', 'AH', 'AS']

    # The cards list will be filled with cards and the card_amount map won't be used
    # The map is just shows how many of that card
    cards_picked = list()
    cards_sum = 0

    def pick_card(self):
        picked_card = random.choice(self.cards_available)
        self.cards_available.remove(picked_card)

        self.cards_picked.append(picked_card)
        self.cards_sum += self.cards_value[picked_card]
        print(f"The Card {picked_card} was picked\nThe Sum of The Cards is {self.cards_sum}")
        return picked_card

    def check_bust(self):
        if self.cards_sum > 21:
            self.is_busted = True

class Player(Card):
    money = 100

    def _continue(self):
        self.check_bust()
        if self.is_busted:
            return False
        while True:
            decision = input("Hit or Stand:\n")
            if (decision == "Hit"):
                return True
            elif (decision == "Stand"):
                return False

    def bid(self):
        while True:
            bid_money = int(input("Bidding Money:\n"))
            if (bid_money <= self.money):
                self.money -= bid_money
                return bid_money

    def play(self):
        self.pick_card()

        return self._continue()

class Dealer(Player):
    # Dealer will be a bot
    money = 10**10

    # Override
    def _continue(self):
        if self.cards_sum > 15:
            return False
        else:
            return True


    def play(self):
        # won't be the same as the play method in player class
        self.pick_card()
        time.sleep(3)
        return self._continue()

class Game:
    running = True
    players_turn = True
    player = Player()
    dealer = Dealer()

    def startup(self):
        # Initiate or Reset
        self.players_turn = True
        self.player = Player()
        self.dealer = Dealer()

    def main(self):
        self.startup()
        bidden_money = self.player.bid()

        # TODO CLEAN THIS CODE

        self.dealer.money -= bidden_money
        bidden_money *= 2

        while self.running:
            if self.players_turn:
                if not self.player.play():
                    # The player is standing
                    print("\n\n" + "-" * 40 + "\n\n")
                    self.players_turn = False
            else:
                if not self.dealer.play():
                    self.ending(bidden_money)
                    print("\n\n" + "-" * 40 + "\n\n")

    def ending(self, bidden_money):
        if (self.player.is_busted or self.dealer.cards_sum > self.player.cards_sum):
            print("Dealer Wins")
            self.dealer.money += bidden_money
        elif (self.dealer.is_busted or self.dealer.cards_sum < self.player.cards_sum):
            print("Player Wins")
            self.player.money += bidden_money
        else:
            print("Neither Wins")
            self.dealer.money += bidden_money // 2
            self.player.money += bidden_money // 2

        while True:
            play_again = input("Play Again? (y/n)\n")
            if (play_again == 'y'):
                self.startup()
                return
            elif (play_again == 'n'):
                self.running = False
                return

if (__name__ == "__main__"):
    Game().main()




