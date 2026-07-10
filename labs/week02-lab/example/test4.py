print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

weight = int(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))
bmi = weight / (height ** 2)

print(f"Your BMI = {bmi}")
