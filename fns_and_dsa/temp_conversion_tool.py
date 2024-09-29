# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get user input for temperature and validate it
        temp_input = input("Enter the temperature to convert: ")
        
        # Attempt to convert the input to a float, or raise ValueError if invalid
        temperature = float(temp_input)
        
        # Get the unit from the user and validate it
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform conversion based on the unit
        if unit == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temp:.1f}°F")
        elif unit == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temp:.1f}°C")
        else:
            # Invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Catch any non-numeric input and raise a ValueError with the required message
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
