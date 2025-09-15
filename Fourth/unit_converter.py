def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(celsius):
    return (celsius * 9 / 5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Exit")

while True:
    try:
        choice = int(input("Choose conversion (1 - 5): "))
        if choice == 1:
            km = float(input("Enter Kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles\n")
        elif choice == 2:
            miles = float(input("Enter Miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} km\n")
        elif choice == 3:
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}° Celsius = {c_to_f(celsius):.2f} Fahrenheit\n")
        elif choice == 4:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit} Fahrenheit = {f_to_c(fahrenheit):.2f}° Celsius\n")
        elif choice == 5:
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid input\n")
    except ValueError:
        print("Please enter a valid number")
