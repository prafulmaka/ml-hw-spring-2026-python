# Read N
N = int(input("Enter N: "))

# Read N numbers one by one
numbers = []

for i in range(N):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Read X
X = int(input("Enter X: "))

# Find X in the list
found_index = -1

for i in range(N):
    if numbers[i] == X:
        found_index = i + 1   # index from 1 to N
        break

# Output result
print(found_index)