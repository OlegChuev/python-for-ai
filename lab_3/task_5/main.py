# Define sorting order dictionary as a constant
ORDER_DICT = {0: "ascending", 1: "descending"}


def check_sort_order(arr, order_key):
    order = ORDER_DICT.get(order_key)

    if order == "ascending":
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    elif order == "descending":
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    else:
        # Invalid order key or order not found in dictionary
        return False


def replace_with_sum_of_value_and_index(arr, order_key):
    # Replace each element with the sum of its value and index
    for i in range(len(arr)):
        arr[i] = arr[i] + i


def main():
    # Prompt the user to input the numbers
    input_numbers = input("Enter at least 5 numbers separated by spaces: ")

    # Convert the input string into a list of numbers
    try:
        numbers = list(map(int, input_numbers.split()))
    except ValueError:
        print("Please enter valid integers.")
        return

    # Ensure array length is at least N+5 (i.e., 5 numbers)
    if len(numbers) < 5:
        print("Invalid array length. Please enter at least 5 numbers.")
        return

    # Prompt the user to input the order key (0 for ascending, 1 for descending)
    try:
        order_key = int(input("Enter 0 for ascending or 1 for descending: "))
        if order_key not in ORDER_DICT:
            print("Invalid sort order. Please enter 0 or 1.")
            return
    except ValueError:
        print("Invalid input. Please enter 0 or 1.")
        return

    # Check the sorting order
    result = check_sort_order(numbers, order_key)

    # Display the result
    if result:
        print(f"The array is sorted in {ORDER_DICT[order_key]} order.")
        replace_with_sum_of_value_and_index(numbers, order_key)
        print(numbers)
    else:
        print(f"The array is not sorted in {ORDER_DICT[order_key]} order.")


if __name__ == "__main__":
    main()
