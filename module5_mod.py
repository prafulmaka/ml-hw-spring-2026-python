class NumberCollection:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def search_number(self, target):
        for index, number in enumerate(self.numbers):
            if number == target:
                return index + 1
        return -1
