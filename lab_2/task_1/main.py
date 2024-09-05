import math


def is_point_within_lower_semicircle(x, y, cx=0, cy=0, r=2):
    # Check the distance condition
    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)

    # Check if the point is within the radius and in the lower part of the circle
    return distance <= r and y <= 0


def is_point_within_square(x, y, min_bound=-1, max_bound=1):
    return min_bound <= x <= max_bound and min_bound <= y <= max_bound


def main():
    # Point coordinates
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))

    in_circle = is_point_within_lower_semicircle(x, y)
    outside_square = not is_point_within_square(x, y)

    if in_circle and outside_square:
        print(f"The point ({x}, {y}) is within shadow area.")
    else:
        print(f"The point ({x}, {y}) is outside.")


if __name__ == "__main__":
    main()
