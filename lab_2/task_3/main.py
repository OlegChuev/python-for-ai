def swap_first_last_elements(lst):
    # Check if the list has at least two elements
    if len(lst) >= 2:
        # Swap the first and last elements
        lst[0], lst[-1] = lst[-1], lst[0]

    return lst


def main():
    # Prompt the user to input the numbers
    input_numbers = input("Enter at least 12 numbers separated by spaces: ")

    # Convert the input string into a list of numbers
    numbers = list(map(int, input_numbers.split()))

    # Check if the list has at least 12 elements
    if len(numbers) < 12:
        print("Please enter at least 12 numbers.")
        return

    # Swap the first and last elements
    swapped_list = swap_first_last_elements(numbers)

    # Print the modified list
    print("List after swapping first and last elements:", swapped_list)


if __name__ == "__main__":
    main()
