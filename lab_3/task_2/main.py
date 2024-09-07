def arithmetic_progression_product(a_n1, t, q):
    # Starts with 1 because multiplying by 1 doesn't change the result
    product = 1

    for k in range(q):
        # Calculate the k-th element of the arithmetic progression
        a_k = a_n1 + k * t
        product *= a_k

    return product


def main():
    a_n1 = int(input("Enter the a(1): "))
    t = int(input("Enter the t: "))
    q = int(input("Enter the q: "))

    result = arithmetic_progression_product(a_n1, t, q)
    print(f"The product of the first {q} elements is: {result}")


if __name__ == "__main__":
    main()
