import numpy as np
from sklearn.metrics import precision_score, recall_score


class TrainingData:
    def __init__(self, n):
        self.points = np.zeros((n, 2), dtype=int)
        self.count = 0

    def insert_point(self, x, y):
        self.points[self.count, 0] = x
        self.points[self.count, 1] = y
        self.count += 1

    def get_labels_and_predictions(self):
        y_true = self.points[: self.count, 0]
        y_pred = self.points[: self.count, 1]
        return y_true, y_pred


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_binary_label(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            print("Value must be 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")


def main():
    n = read_positive_integer("Enter N, a positive integer: ")

    data = TrainingData(n)

    for i in range(n):
        x = read_binary_label(f"Enter x for point {i + 1}: ")
        y = read_binary_label(f"Enter y for point {i + 1}: ")
        data.insert_point(x, y)

    y_true, y_pred = data.get_labels_and_predictions()

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    print(precision)
    print(recall)


if __name__ == "__main__":
    main()
