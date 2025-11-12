# bmi_module.py
# Simple BMI Calculator + Progress Comparison (Beginner Version)

def calculate_bmi(weight, height):
    """Returns the BMI value."""
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be greater than zero.")
    return round(weight / (height ** 2), 2)


def bmi_category(bmi):
    """Returns the BMI category based on value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def bmi_user_input():
    """Takes user input and prints BMI and category."""
    print("\n=== Body Mass Index (BMI) Calculator ===")

    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

    except ValueError:
        print("\nInvalid input! Please enter valid numbers.")


# -------------------------------
# New: Progress Comparison Feature
# -------------------------------
def progress_comparison():
    """Compares daily, weekly, or monthly progress in calories or steps."""
    print("\n=== Progress Comparison ===")

    data_type = input("Enter what you want to track (Calories / Steps): ").capitalize()
    period = input("Enter period type (Daily / Weekly / Monthly): ").capitalize()

    try:
        count = int(input(f"How many {period.lower()} entries do you want to compare? "))

        data = []
        for i in range(count):
            value = float(input(f"Enter {data_type} for {period} {i+1}: "))
            data.append(value)

        print("\n--- Progress Summary ---")
        for i in range(count):
            print(f"{period} {i+1}: {data[i]} {data_type}")

        average = sum(data) / len(data)
        print(f"\nAverage {data_type}: {average:.2f}")

        if data[-1] > data[0]:
            print(f"Good job! Your {data_type.lower()} have improved from {data[0]} to {data[-1]}!")
        elif data[-1] < data[0]:
            print(f"You did less {data_type.lower()} than before. Try to improve!")
        else:
            print("Your performance stayed the same this time.")

    except ValueError:
        print("\nInvalid input! Please enter numeric values.")


# -------------------------------
# Main Menu
# -------------------------------
def main():
    print("=== Welcome to the Fitness Tracker ===")
    print("1. Calculate BMI")
    print("2. Compare Progress")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            bmi_user_input()
        elif choice == "2":
            progress_comparison()
        elif choice == "3":
            print("Thank you for using the Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

