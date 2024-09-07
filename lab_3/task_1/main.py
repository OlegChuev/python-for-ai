def count_ones_in_binary(N):
    return bin(N).count("1")


def main():
    N = int(input("Enter the N: "))
    result = count_ones_in_binary(N)
    print(f"The sum of '1's in the binary representation of {N} is {result}: {bin(N)}")


if __name__ == "__main__":
    main()
