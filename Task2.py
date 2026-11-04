choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ").upper()
temperature = float(input("Enter the temperature: "))

if choice == "C":
    result = temperature * 1.8 + 32
    print(f"{temperature:g}°C = {result:g}°F")
elif choice == "F":
    result = (temperature - 32) / 1.8
    print(f"{temperature:g}°F = {result:g}°C")
else:
    print("Invalid choice")
