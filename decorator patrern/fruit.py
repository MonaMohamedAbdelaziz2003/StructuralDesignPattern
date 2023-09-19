from Icecream import icecreame


class fruit(icecreame):
    def __init__(self, icecream: icecreame):
        self.icecream=icecream

    def cost(self):
        return self.icecream.cost()+2.5

    def description(self):
        return self.icecream.description()+" fruit"

