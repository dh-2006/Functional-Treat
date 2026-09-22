print("=================== Functional Treat====================")
print()

data = []
dataset_summary = {}


def Input_data():
    global data

    print("1. 1D array")
    print("2. 2D array")

    option = int(input("Enter a number for array: "))

    if option == 1:

        num = list(map(int, input(
            "Enter data for a 1D array(separated by space): "
        ).split()))

        data = num

        print("Data has been stored successfully!")

    elif option == 2:

        data = []

        for i in range(3):

            row = list(map(int, input(
                f"Enter Row {i + 1} : "
            ).split()))

            data.append(row)

        print("Data has been stored successfully!")

    else:

        print("Invalid choice")


def display_values(*args):
    """Display multiple values using *args."""

    print(*args, sep=", ")


def display_data_summary():
    """Display basic statistics using built-in functions."""

    if len(data) == 0:
        print("Please enter data first.")
        return

    if type(data[0]) == list:

        values = []

        for row in data:
            for value in row:
                values.append(value)

    else:

        values = data

    total = len(values)
    minimum = min(values)
    maximum = max(values)
    total_sum = sum(values)
    average = total_sum / total

    print("\nData Summary:")
    print("- Total elements:", total)
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total_sum)
    print("- Average value:", round(average, 2))


def calculate_factorial(number):
    """Calculate factorial using recursion."""

    if number == 0 or number == 1:
        return 1

    return number * calculate_factorial(number - 1)


def filter_data():
    """Filter data using lambda and filter function."""

    if len(data) == 0:
        print("Please enter data first.")
        return

    threshold = int(input(
        "Enter a threshold value to filter out data above this value: "
    ))

    if type(data[0]) == list:

        values = []

        for row in data:
            for value in row:
                values.append(value)

    else:

        values = data

    filtered_data = list(
        filter(lambda x: x >= threshold, values)
    )

    print("\nFiltered Data (values >=", threshold, "):")

    if len(filtered_data) == 0:
        print("No values found.")
    else:
        display_values(*filtered_data)


def sort_data():
    """Sort the data using sort and sorted functions."""

    if len(data) == 0:
        print("Please enter data first.")
        return

    if type(data[0]) == list:

        print("Sorting is available for 1D data only.")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        data.sort()

        print("\nSorted Data in Ascending Order:")
        display_values(*data)

    elif choice == 2:

        sorted_data = sorted(data, reverse=True)

        print("\nSorted Data in Descending Order:")
        display_values(*sorted_data)

    else:

        print("Please enter 1 or 2.")


def get_statistics():
    """Return minimum, maximum, sum and average values."""

    if type(data[0]) == list:

        values = []

        for row in data:
            for value in row:
                values.append(value)

    else:

        values = data

    minimum = min(values)
    maximum = max(values)
    total_sum = sum(values)
    average = total_sum / len(values)

    return minimum, maximum, total_sum, average


def display_dataset_summary(**kwargs):
    """Display dataset information using **kwargs."""

    for key, value in kwargs.items():
        print("-", key, ":", value)


print("Welcome to the Data Analyzer and Transformer Program")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 1:

        Input_data()

    elif choice == 2:

        display_data_summary()

    elif choice == 3:

        number = int(input(
            "\nEnter a number to calculate its factorial: "
        ))

        result = calculate_factorial(number)

        print("Factorial of", number, "is:", result)

    elif choice == 4:

        filter_data()

    elif choice == 5:

        sort_data()

    elif choice == 6:

        if len(data) == 0:
            print("Please enter data first.")
            continue

        minimum, maximum, total_sum, average = get_statistics()

        dataset_summary = {
            "Minimum value": minimum,
            "Maximum value": maximum,
            "Sum of all values": total_sum,
            "Average value": round(average, 2)
        }

        print("\nDataset Statistics:")

        display_dataset_summary(**dataset_summary)

    elif choice == 7:

        print(
            "\nThank you for using the Data Analyzer "
            "and Transformer Program. Goodbye!"
        )

        break

    else:

        print("Please enter a valid choice.")
