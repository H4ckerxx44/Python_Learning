currentYear = int(input("current year "))
currentPop = int(input("current population "))
birthsPerYear = int(input("births/year "))
targetYear = int(input("targetYear "))
difference = abs(int(targetYear) - int(currentYear))

newPop = currentPop + difference * birthsPerYear

print(difference, "Jahre Später leben", newPop, "Menschen auf der Welt")
print("Das sind", difference * birthsPerYear, "mehr als im Jahr", currentYear)