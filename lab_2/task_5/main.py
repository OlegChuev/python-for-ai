import math


def factorial_of_n_plus_5(N):
    n = N + 5
    return math.factorial(n)


def main():
    N = int(input("Enter the number N: "))
    result = factorial_of_n_plus_5(N)
    print(f"The factorial of {N + 5} is {result}")


if __name__ == "__main__":
    main()
