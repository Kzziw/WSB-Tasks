
number = int(input("Enter the number of grades: "))

total = 0

for i in range(number):
    grade = float(input(f"Enter grade {i + 1}: "))
    total += grade

if number > 0:
    average = total / number
    print(f"Average: {average:.2f}")

    if average >= 3.0:
        print("The student passed.")
    else:
        print("The student failed.")
else:
    print("No grades entered.")