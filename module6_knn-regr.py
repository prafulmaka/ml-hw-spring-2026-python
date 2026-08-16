import numpy as np


class KNNRegression:
    def __init__(self, n):
        self.points = np.zeros((n, 2), dtype=float)
        self.count = 0

    def insert_point(self, x, y):
        self.points[self.count, 0] = x
        self.points[self.count, 1] = y
        self.count += 1

    def predict(self, x_query, k):
        x_train = self.points[: self.count, 0]
        y_train = self.points[: self.count, 1]
        distances = np.abs(x_train - x_query)
        nearest_indices = np.argsort(distances)[:k]
        return np.mean(y_train[nearest_indices])


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a real number.")


def main():
    n = read_positive_integer("Enter N, a positive integer: ")
    k = read_positive_integer("Enter k, a positive integer: ")

    model = KNNRegression(n)

    for i in range(n):
        x = read_real_number(f"Enter x for point {i + 1}: ")
        y = read_real_number(f"Enter y for point {i + 1}: ")
        model.insert_point(x, y)

    x_query = read_real_number("Enter X: ")

    if k > n:
        print("Error: k must be less than or equal to N.")
        return

    result = model.predict(x_query, k)
    print(result)


if __name__ == "__main__":
    main()


