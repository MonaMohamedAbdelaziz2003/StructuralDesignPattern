from CardFactory import CardFactory


class CardGame:
    def __init__(self):
        self.cards = []

    def deal_card(self, rank, suit):
        card = CardFactory.get_card(rank, suit)
        card.display()
        self.cards.append(card)

