from card import card
from random import randint

class set_stack:
    def __init__(self) -> None:
        self.unshown = []
        self.shown = []
        self.found = []
        self.score = 0
        for color in card.colors:
            for filling in card.fillings:
                for number in card.numbers:
                    for shape in card.shapes:
                        self.unshown.append(card(color, filling, number, shape))
        for _ in range(4):
            self.add_cards_to_shown()
        while not self.check_for_shown_set():
            self.add_cards_to_shown()

    def add_cards_to_shown(self):
        if len(self.unshown) != 0:
            for _ in range(min(3,len(self.unshown))):
                i = randint(1, len(self.unshown))
                self.shown.append(self.unshown.pop(i-1))

    def check_for_shown_set(self):
        for i in range(len(self.shown)-1):
            card_1 = self.shown[i]
            for j in range(i+1, len(self.shown)):
                card_2 = self.shown[j]
                card_3 = card_1.get_setting_card(card_2)
                if card_3 in self.shown:
                    return True
        return False
    
    def check_selected_cards(self, indices):
        card_1 = self.shown[indices[0]]
        card_2 = self.shown[indices[1]]
        card_3 = self.shown[indices[2]]
        if card_1.get_setting_card(card_2) == card_3:
            s = [card_1, card_2, card_3]
            self.shown = [c for c in self.shown if c not in s]
            self.found += s
            if len(self.shown)<12:
                self.add_cards_to_shown()
            while not self.check_for_shown_set():
                self.add_cards_to_shown()
            return True
        return False

            