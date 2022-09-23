employees = ["Bruce", "Oswald", "Flo", "Bif"]

for employee in employees:
    print(employee)
    employees.sort()

employees.append("Layne") #adding a new employee
employees.remove("Flo") #removing an employee

print() #space

for employee in employees:
    print(employee)
    employees.sort()

Layne = "Baller"

print()

if Layne == "Baller":
    print("We ball")
else: 
    print("Gabe isn't real")

Layne = "Not Baller"

print() #space

if Layne == "Baller":
    print("We ball")
else: 
    print("Gabe isn't real")

    betterPerson = input("Who is a better person? Gabe or Layne?")
    userGuess = 1

    while betterPerson != "Layne":
        userGuess = userGuess + 1
        betterPerson = input("Guess again silly.")

        print("You are so smart")