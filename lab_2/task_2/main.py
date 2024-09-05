import math


def calculate_y(x, a):
    if x <= -1:
        return a * math.cos(x + 1) + a
    else:
        return a * (x + 2) ** (3 / 2)


def main():
    x = float(input("Input X: "))
    a = float(input("Input A: "))

    y = calculate_y(x, a)
    print(f"Y is: {y}")


if __name__ == "__main__":
    main()
