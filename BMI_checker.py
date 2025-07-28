# Ask the user for height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Function to calculate BMI
def calculate_BMI(height, weight): 
    return weight / (height ** 2)

# Calculate BMI
BMI = calculate_BMI(height, weight)

# Function to display BMI
def display_BMI(BMI):
    print("Your Body Mass Index is:", round(BMI, 2))

# Display BMI
display_BMI(BMI)

# Display BMI category
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 24.9:
    print("Normal Weight")
elif 25.0 <= BMI < 29.9: 
    print("Overweight")
else:
    print("Obese")
