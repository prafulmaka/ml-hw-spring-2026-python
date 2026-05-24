import numpy as np
from sklearn.neighbors import KNeighborsRegressor


class TrainingData:
    def __init__(self, n):
        self.points = np.zeros((n, 2), dtype=float)
        self.count = 0

    def insert_point(self, x, y):
        self.points[self.count, 0] = x
        self.points[self.count, 1] = y
        self.count += 1

    def get_features_and_labels(self):
        x_train = self.points[: self.count, 0].reshape(-1, 1)
        y_train = self.points[: self.count, 1]
        return x_train, y_train


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

    data = TrainingData(n)

    for i in range(n):
        x = read_real_number(f"Enter x for point {i + 1}: ")
        y = read_real_number(f"Enter y for point {i + 1}: ")
        data.insert_point(x, y)

    x_train, y_train = data.get_features_and_labels()
    label_variance = np.var(y_train)

    x_query = read_real_number("Enter X: ")

    if k > n:
        print("Error: k must be less than or equal to N.")
    else:
        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(x_train, y_train)
        result = model.predict(np.array([[x_query]]))[0]
        print(result)

    print(label_variance)


if __name__ == "__main__":
    main()
