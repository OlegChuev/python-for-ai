import math


def calculate_Y(x, a):
    numerator = (
        math.exp(-x)
        + math.log(abs(math.acos(x)))
        + math.atan(x)
        - (1.2 * math.cos(x) ** 2)
    )
    denominator = (math.sqrt(a * x) * (a * math.exp(a * x) + 3.5 * 10**-5)) - (
        x + a**2 - 0.3
    ) ** (1 / 3)

    if denominator == 0:
        raise ValueError("Denominator evaluates to zero, leading to division by zero.")

    Y = numerator / denominator
    return Y


def main():
    a = 0.5
    print(f"A: {a:.2f}")

    x = 3.4 * 10**-4
    print(f"X: {x:.10f}")

    y = calculate_Y(a, x)
    print(f"Y: {y:.10f}")


if __name__ == "__main__":
    main()
