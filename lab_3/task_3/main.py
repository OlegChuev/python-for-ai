def geometric_progression_sum(a_n1, t, alim):
    total_sum = 0

    # Start with the first element
    a_k = a_n1

    while a_k > alim:
        # Add the current element to the sum
        total_sum += a_k
        # Move to the next element in the progression (ak+1 = ak * t)
        a_k *= t

    return total_sum


def main():
    a_n1 = int(input("Enter the a(1): "))
    alim = int(input("Enter the alim: "))
    t = float(input("Enter the t: "))

    result = geometric_progression_sum(a_n1, t, alim)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
