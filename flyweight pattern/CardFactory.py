from card import Card
class CardFactory:
    card_pool = {}
    @staticmethod
    def get_card(rank, suit):
        key = (rank, suit)
        if key not in CardFactory.card_pool:
            CardFactory.card_pool[key] = Card(rank, suit)
        return CardFactory.card_pool[key]

