import numpy as np
from scipy.linalg import solve

matrix = np.array([[25, 5.6, 4, 3],
              [4, 21, 6.5, 7],
              [5, 9.6, 14.1, 2],
              [3.9, 5.6, 2.4, 23]])

print("Input Matrix:")
for row in matrix:
    row_str = "  ".join([f"{elem:5.1f}" for elem in row])
    print("|" + row_str + "  |")

terms = np.array([3.4, 2.45, 6.9, 1.4])

print("Free terms (b):")
for elem in terms:
    print(f"| {elem:5.1f} |")

x = solve(matrix, terms)
x = np.round(x, 5)

print("\nResult x:")
for i, elem in enumerate(x):
    print(f"x{i+1}: {elem:.5f}")

