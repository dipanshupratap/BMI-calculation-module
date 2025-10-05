# BMI-calculation-module
#(Python)

This is a simple Python module to calculate Body Mass Index (BMI)and determine the weight category.

# How to Use

```python
from bmi_module import calculate_bmi, bmi_category, bmi_user_input

# Option 1: Direct user input
bmi_user_input()

# Option 2: Manual calculation
bmi = calculate_bmi(70, 1.75)
category = bmi_category(bmi)
print(f"BMI: {bmi}, Category: {category}")
