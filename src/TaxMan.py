class TaxMan:
    total = 0.00

    def __init__(self, items, rate):
        self.items = items
        self.rate = rate

    def calc_total(self):
        for x in self.items:
            self.total += x['price']
        self.total += self.total * 1/(float(self.rate[0:len(self.rate)-1]))

    def get_total(self):
        return self.total
