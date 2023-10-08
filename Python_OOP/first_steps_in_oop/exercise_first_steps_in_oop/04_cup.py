class Cup:
    def __init__(self, size, quantity):
        self.quantity = quantity
        self.size = size

    def fill(self, amount):
        if self.status() >= amount:
            self.quantity += amount

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
