employees = ["Alice", "Vera", "Flo", "Mel"]

for employee in employees:
    print(employee)
    employees.sort()

employees.append("Layne")
employees.remove("Flo")

print()

for employee in employees:
    print(employee)
    employees.sort()