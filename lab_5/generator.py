import random


def generate_traffic_data(filename="traffic_data.txt"):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    cities = [
        "London",
        "Manchester",
        "Birmingham",
        "Liverpool",
        "Glasgow",
        "Leeds",
        "Bristol",
    ]
    binary_values = ["no", "yes"]

    with open(filename, "w") as f:
        for city in cities:
            for day in days:
                for hour in range(24):
                    for minute in range(0, 60, 5):  # Steps of 5 minutes
                        time_of_day = f"{hour:02}:{minute:02}"
                        city = city
                        passing_vehicles = random.randint(
                            1, 50
                        )  # Simulated vehicle counts
                        binary_value = random.choice(binary_values)
                        f.write(
                            f"{day},{time_of_day},{city},{binary_value},{passing_vehicles}\n"
                        )


# Generate the traffic data
generate_traffic_data()
