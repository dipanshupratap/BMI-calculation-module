# bmi_module.py
# Body Mass Index (BMI) calculation module

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
    print("=== Body Mass Index (BMI) Calculator ===\n")

    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

        return bmi, category
    except ValueError:
        print("\nInvalid input! Please enter valid numeric values.")
        return None, None


if __name__ == "__main__":
    bmi_user_input()
   

