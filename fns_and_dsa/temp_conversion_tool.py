# Define global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get user input for temperature
        temp = float(input("Enter the temperature to convert: "))
        
        # Get user input for unit (C/F)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on unit
        if unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Catch non-numeric input
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
