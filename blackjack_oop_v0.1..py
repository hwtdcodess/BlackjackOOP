import random
import time

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.value = value
        self.suit = suit
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        return sum(card.value for card in self.cards)

class Game:
    def __init__(self):
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['♠️', '♥️', '♦️', '♣️']

        self.player_hand = Hand()

    def draw_card(self):
        suit = random.choice(self.suits)
        name = random.choice(self.values)

        if name in ['J','Q','K']:
            value = 10
        elif name == 'A':
            value = 11
        else:
            value = int(name)

        return Card(name, suit, value)

    def got_card(self):
        print('Карты:')
        for card in self.player_hand.cards:
            print(card.name + card.suit)
        print('Очки:', self.player_hand.get_value())

    def repeat(self):
        repeat = str(input("Хотите повторить?\ny/n: "))
        return repeat
    def start(self):
        while True:
            self.player_hand = Hand()

            self.player_hand.add_card(self.draw_card())
            self.player_hand.add_card(self.draw_card())
            self.got_card()

            while True:
                try:
                    choice = int(input('Выбор:\n1. Взять.\n2. Хватит\nВвод: '))
                    if choice == 1:
                        self.player_hand.add_card(self.draw_card())
                        self.got_card()
                    else:
                        print('---')
                        break
                except ValueError:
                    print("Ошибка! Повторите.")

                if self.player_hand.get_value() > 21:
                    print('Перебор.')
                    print("Вы проиграли.")
                    break
                elif self.player_hand.get_value() == 21:
                    print("Вы победили!")
                    break
            if self.repeat() == "y":
                continue
            else:
                return print("Удачи!")
game = Game()
game.start()