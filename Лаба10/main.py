import numpy as np


def divided_differences(x, y):
    n = len(x)
    coefficients = np.zeros((n, n))
    coefficients[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coefficients[i][j] = (coefficients[i + 1][j - 1] - coefficients[i][j - 1]) / (x[i + j] - x[i])

    return coefficients[0]


def newton_interpolation(x, y, xi):
    n = len(x)
    coefficients = divided_differences(x, y)
    result = coefficients[0]
    product_term = 1

    for i in range(1, n):
        product_term *= (xi - x[i - 1])
        result += coefficients[i] * product_term

    return result


def newton_interpolation_extrapolation(x, y, xi_min, xi_max, num_points):
    xi = np.linspace(xi_min, xi_max, num_points)
    interpolation_result_1 = np.zeros(num_points)
    interpolation_result_2 = np.zeros(num_points)

    for i in range(num_points):
        if xi_min <= xi[i] <= xi_max:
            interpolation_result_1[i] = newton_interpolation(x, y, xi[i])
        else:
            coefficients = divided_differences(x, y)
            result_1 = coefficients[0]
            result_2 = coefficients[0]
            product_term_1 = 1
            product_term_2 = 1

            for j in range(1, len(x)):
                product_term_1 *= (xi[i] - x[j - 1])
                result_1 += coefficients[j] * product_term_1

                product_term_2 *= (xi[i] - x[-j])
                result_2 += coefficients[-j] * product_term_2

            interpolation_result_1[i] = result_1
            interpolation_result_2[i] = result_2

    return xi, interpolation_result_1, interpolation_result_2

x = np.array([2.97, 9.57])
y = 1 / (6 * x*x*x*x + 5)


xi_min = 3
xi_max = 9
num_points = 6

xi, extrapolation_result_1, extrapolation_result_2 = newton_interpolation_extrapolation(x, y, xi_min, xi_max,
                                                                                        num_points)

print("Extrapolation Results 1:")
print("    xi   |")
print("---------------------------------")
for i in range(len(xi)):
    print(f"{xi[i]:8.2f} | {extrapolation_result_1[i]:12.9f}")

print("\nExtrapolation Results 2:")
print("    xi   |")
print("---------------------------------")
for i in range(len(xi)):
    print(f"{xi[i]:8.2f} | {extrapolation_result_2[i]:12.9f}")
