#!/usr/bin/env python3


class CashRegister:
    """Model a simple cash register that tracks items, totals, and discounts."""

    def __init__(self, discount=0):
        # Keep private backing fields for validation and state tracking.
        self._discount = 0
        self._total = 0.0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    @property
    def total(self):
        """Return the current total on the register."""
        return self._total

    @total.setter
    def total(self, value):
        """Store the total and clear the register when it is reset to zero."""
        self._total = float(value)

        if self._total == 0:
            self.items = []
            self.previous_transactions = []

    @property
    def discount(self):
        """Return the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Validate the discount before storing it on the register."""
        if not isinstance(value, int) or isinstance(value, bool):
            print("Not valid discount")
            return

        if value < 0 or value > 100:
            print("Not valid discount")
            return

        self._discount = value

    def add_item(self, item, price, quantity=1):
        """Add an item to the register and update totals and history."""
        quantity = int(quantity)
        line_total = price * quantity

        self.total += line_total
        self.items.extend([item] * quantity)
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        """Apply the configured percentage discount to the current total."""
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        """Remove the most recent item entry and update totals."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        quantity = last_transaction["quantity"]
        price = last_transaction["price"]

        self.total -= price * quantity

        for _ in range(quantity):
            if self.items:
                self.items.pop()
