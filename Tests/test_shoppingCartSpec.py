import pytest


@pytest.mark.parametrize("items, cost", [
    (["A"], 50),
    (["B"], 30),
    (["A", "B", "C", "D"], 105),
    (["A", "A", "A"], 130),
    (["B", "B"], 45)
])
def test_checkout_total(items, cost):
    checkout = Checkout()

    for item in items:
        checkout.Scan(item)

    assert checkout.Total() == cost


class Checkout():
    def __init__(self):
        self._prices = {"A": 50, "B": 30, "C": 15, "D": 10}
        self._total = 0
        self._basket = []

    def Scan(self, sku):
        self._total += self._prices[sku]
        self._basket.append(sku)

    def Total(self):
        if(self._basket.count("A") == 3):
            self._total -= 20

        if(self._basket.count("B") == 2):
            self._total -= 15

        return self._total


class Discounter():
    def __init__(self):
        self._rules = [DiscountRule("A", 3, 20), DiscountRule("B", 2, 15)]

    def GetDiscountTotal(self, basket):
        totalDiscount = 0

        for rule in self._rules:
            checkout.Scan(item)


class DiscountRule():
    def __init__(self, sku, numberOfItems, discountAmount):
        self._sku = sku
        self._numberOfItems = numberOfItems
        self._discountAmount = discountAmount

    def GetDiscount(self, basket):
        countOfSkus = basket.count(self._sku)

        if(countOfSkus == self._numberOfItems):
            return self._discountAmount

        return 0
