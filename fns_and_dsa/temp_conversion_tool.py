FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
temperature = float(input("Enter temperature: "))
unit = input("Is this temperature in Fahrenheit or Celsius? (F/C): ").strip().lower()
if unit == 'f':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp:.2f}°C")
elif unit == 'c':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp:.2f}°F")
else:
    print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")