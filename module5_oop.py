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


def read_positive_integer():
    while True:
        try:
            value = int(input("Enter N, a positive integer: "))
            if value > 0:
                return value
            print("N must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    collection = NumberCollection()

    n = read_positive_integer()

    for i in range(n):
        while True:
            try:
                number = int(input(f"Enter number {i + 1}: "))
                collection.insert_number(number)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    while True:
        try:
            x = int(input("Enter X, the number to search for: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    result = collection.search_number(x)
    print(result)


if __name__ == "__main__":
    main()
    
    
