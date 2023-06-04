import numpy as np


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
    print(f"|{elem:5.1f}  |")

zero = np.zeros_like(terms)
iteration_count = 1000
e = 0.001
iterations=[]
for first in range(iteration_count):
    zero_new = np.zeros_like(zero)
    for second in range(len(terms)):
        s = np.dot(matrix[second, :second], zero[:second]) + np.dot(matrix[second, second + 1:], zero[second + 1:])
        zero_new[second] = (terms[second] - s) / matrix[second, second]
    iterations.append(np.round(zero_new, 5))
    if np.allclose(zero, zero_new, rtol=e):
        break
    zero = zero_new
result = np.round(zero, 5)
print(f"Solution after the first iteration:\n\t|{iterations[0][0]}|{iterations[0][1]}|{iterations[0][2]}|{iterations[0][3]}|")
print(f"Solution after the second iteration:\n\t|{iterations[1][0]}|{iterations[1][1]}|{iterations[1][2]}|{iterations[1][3]}|")
print(f"Solution after the third iteration:\n\t|{iterations[2][0]}|{iterations[2][1]}|{iterations[2][2]}|{iterations[2][3]}|")
print(f"Iterations count: {len(iterations)}")
print(f"Result {result}")