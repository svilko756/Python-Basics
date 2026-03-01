exercices = []
calories = [] 
total_burn_calories = 0

while True:
    exercice = input("What exercice you want to do (press q to quit): ")

    if exercice.lower() == "q":
        break 

    else:
        cal = float(input("How much calories this exercice burns: "))
        exercices.append(exercice)
        calories.append(cal)

for x in exercices:
    print(x)

total_burn_calories = sum(calories)

print(f"You will burn {total_burn_calories} calories")

  
