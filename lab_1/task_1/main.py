import math


def calculate_area_of_triangle(side1, side2, side3):
    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    return area


def main():
    try:
        # Get user input for the sides of the triangle
        side1 = float(input("Enter the length of the first side: "))
        side2 = float(input("Enter the length of the second side: "))
        side3 = float(input("Enter the length of the third side: "))

        # Check if the sides form a valid triangle
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            area = calculate_area_of_triangle(side1, side2, side3)
            print(f"The area of the triangle is: {area:.2f}")
        else:
            print("The lengths provided do not form a valid triangle.")

    except ValueError:
        print("Invalid input. Please enter numerical values for the sides.")


if __name__ == "__main__":
    main()
