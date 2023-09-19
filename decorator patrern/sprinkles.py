from Icecream import icecreame


class sprinkles(icecreame):
    def __init__(self, icecream: icecreame):
        self.icecream=icecream

    def cost(self):
        return self.icecream.cost()+2

    def description(self):
        return self.icecream.description()+" sprinkles"


