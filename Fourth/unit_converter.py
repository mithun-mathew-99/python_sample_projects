def km_to_miles(km):
  retrun km * 0.621371

def miles_to_km(miles):
  retrun miles/0.621371

def c_to_f(celsius):
  return (celsius*9/5) + 32

def f_to_c(fahrenheit):
  return (fahrenheit -32)*5/9

print(" Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
choice = int(input("Choose conversion (1 - 4)"))

try:
  if choise == 1:
    km = float(input("Enter Kilometers : ")
    print(f" {km} km = {km_to_miles(km) : .2f} miles")

  if choise == 2:
    miles = float(input("Enter Miles : ")
    print(f" {miles} miles = {miles_to_km(miles) : .2f} km")

  if choise == 3:
    celsius = float(input("Enter temperature in Celsius : ")
    print(f" {km} \u00bo Celcius = {km_to_miles(celsius) : .2f} Fahrenheit")

  if choise == 4:
    fahrenheit = float(input("Enter temperature in Fahrenheit : ")
    print(f" {fahrenheit} Fahrenheit = {f_to_c(fahrenheit) : .2f} \u00bo Celcius")

  else:
    print("Invalid input")
except ValueError:
  print(" please enter a valid number")
