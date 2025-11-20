def display_menu():
    print("\nWelcome to Data Analyzer and Transformer Program")
    print("\nMain Menu")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")


def input_data():
    data = list(map(int, input("\nEnter data for a 1D array (separated by space): ").split()))
    print("Data has been stored successfully!")
    return data


def data_summary(data):
    print("\nData Summary:")
    print("Total elements:", len(data))
    print("Minimum Value:", min(data))
    print("Maximum Value:", max(data))
    print("Sum of all values:", sum(data))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def filter_data(data):
    threshold = int(input("Enter threshold value: "))
    filtered = list(filter(lambda x: x > threshold, data))
    print(f"Filtered data (values > {threshold}):", filtered)


def sort_data(data):
    print("\n1. Sort in Ascending Order")
    print("2. Sort in Descending Order")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        sorted_data = sorted(data)
        print("Data sorted in Ascending Order:", sorted_data)

    elif choice == '2':
        sorted_data = sorted(data, reverse=True)
        print("Data sorted in Descending Order:", sorted_data)

    else:
        print("Invalid choice!")


def dataset_statistics(data):
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)
    return minimum, maximum, total, average


def show_statistics(data):
    stats = dataset_statistics(data)
    print("\nDataset Statistics")
    print("Minimum Value:", stats[0])
    print("Maximum Value:", stats[1])
    print("Total Sum:", stats[2])
    print("Average:", round(stats[3], 2))


def exit_program():
    print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
    exit()


data = []

while True:
    display_menu()
    choice = input("\nPlease enter your choice (1-7): ")

    match choice:

        case '1':
            data = input_data()
            print("Your data:", data)

        case '2':
            if data:
                data_summary(data)
            else:
                print("No data found! Please input data first.")

        case '3':
            n = int(input("Enter number to calculate factorial: "))
            if n < 0:
                print("Factorial does not exist for negative numbers.")
            else:
                print(f"Factorial of {n} is: {factorial(n)}")

        case '4':
            if data:
                filter_data(data)
            else:
                print("No data found!")

        case '5':
            if data:
                sort_data(data)
            else:
                print("No data found!")

        case '6':
            if data:
                show_statistics(data)
            else:
                print("No data found! Please input data first.")

        case '7':
            exit_program()

        case _:
            print("Invalid choice! Please enter a number between 1 and 7.")
