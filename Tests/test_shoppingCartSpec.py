import pytest


@pytest.mark.parametrize("items, cost", [
    (["A"], 50),
    (["B"], 30),
    (["A", "B", "C", "D"], 105),
    (["A", "A", "A"], 130),
    (["B", "B"], 45),
    (["B", "B", "B", "B"], 90),
    (["A", "A", "A", "B", "B"], 175),
    (["A", "A", "A", "A", "A"], 230)
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
        self._total -= Discounter().GetDiscountTotal(self._basket)

        return self._total


class Discounter():
    def __init__(self):
        self._rules = [DiscountRule("A", 3, 20), DiscountRule("B", 2, 15)]

    def GetDiscountTotal(self, basket):
        totalDiscount = 0

        for amount in [rule.DiscountToApply(basket) for rule in self._rules if rule.ShouldApplyDiscount(basket)]:
            totalDiscount += amount

        return totalDiscount


class DiscountRule():
    def __init__(self, sku, quantity, discountAmount):
        self._sku = sku
        self._quantity = quantity
        self._discountAmount = discountAmount

    def ShouldApplyDiscount(self, basket):
        return self.GetCount(basket) > 0

    def DiscountToApply(self, basket):
        return self._discountAmount * (self.GetCount(basket) // self._quantity)

    def GetCount(self, basket):
        return basket.count(self._sku)
