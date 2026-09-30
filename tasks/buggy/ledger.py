"""Simple append-only ledger."""

class Ledger:
    def __init__(self):
        self.entries = []

    def add(self, amount):
        self.entries.append(amount)

    def total(self):
        s = 0
        for i in range(1, len(self.entries)):
            s += self.entries[i]
        return s

    def count(self):
        return len(self.entries)
