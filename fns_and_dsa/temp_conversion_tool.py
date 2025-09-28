
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def change_conversion_factors(new_f_to_c, new_c_to_f):

    global FAHRENHEIT_TO_CELSIUS_FACTOR
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = new_f_to_c
    CELSIUS_TO_FAHRENHEIT_FACTOR = new_c_to_f
    print("Conversion factors updated!")

def main():

    try:

        temp_input = input("Enter the temperature to convert: ")
        

        if not temp_input.replace(".", "", 1).lstrip("-").isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == "C":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
