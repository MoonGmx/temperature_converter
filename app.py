# Temperature Conversion Program

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    unit = input("Enter the unit of temperature (Celsius, Fahrenheit, Kelvin): ").strip().lower()
    value = float(input("Enter the temperature value: "))
    
    if unit == "celsius":
        print(f"Fahrenheit: {celsius_to_fahrenheit(value)}")
        print(f"Kelvin: {celsius_to_kelvin(value)}")
    elif unit == "fahrenheit":
        print(f"Celsius: {fahrenheit_to_celsius(value)}")
        print(f"Kelvin: {fahrenheit_to_kelvin(value)}")
    elif unit == "kelvin":
        print(f"Celsius: {kelvin_to_celsius(value)}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(value)}")
    else:
        print("Invalid unit of measurement")

if _name_ == "_main_":
    main()
