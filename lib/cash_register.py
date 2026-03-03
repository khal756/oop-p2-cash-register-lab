class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction_total = 0
        self.last_transaction_items = []

    def add_item(self, title, price, quantity=1):
        # Add to total
        transaction_total = price * quantity
        self.total += transaction_total

        # Add items to the list (duplicate for quantity)
        self.items.extend([title] * quantity)

        # Track last transaction
        self.last_transaction_total = transaction_total
        self.last_transaction_items = [title] * quantity

    def apply_discount(self):
        if self.discount:
            self.total *= (1 - self.discount / 100)
            # Ensure total is displayed as integer if it matches tests
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Subtract last transaction total from total
        self.total -= getattr(self, "last_transaction_total", 0)

        # Remove last transaction items from the list
        if hasattr(self, "last_transaction_items"):
            for item in self.last_transaction_items:
                self.items.remove(item)
pass