"""Simple append-only ledger."""

class Ledger:
    def __init__(self):
        self.entries = []

    def add(self, amount):
        self.entries.append(amount)

    def total(self):
        return sum(self.entries)

    def count(self):
        return len(self.entries)
