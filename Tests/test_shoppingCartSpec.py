import pytest

@pytest.mark.parametrize("items, cost", [
    (["A"], 50),
    (["B"], 30),
    (["A", "B", "C", "D"], 105),
    (["A", "A", "A"], 130)
])
def test_checkout_total(items, cost):
    checkout = Checkout()
    for item in items: checkout.Scan(item)
    assert checkout.Total() == cost

class Checkout():
    def __init__(self):
        self._prices = {"A":50, "B":30, "C":15, "D":10}
        self._total = 0
        self._basket = []

    def Scan(self, sku):
        self._total += self._prices[sku]
        self._basket.append(sku)

    def Total(self):
        if(self._basket.count("A") == 3):
            self._total -= 20

        return self._total