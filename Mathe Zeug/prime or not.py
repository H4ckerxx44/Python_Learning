num = int(input("Nummer: "))

if num > 1:
    # check for factors
    for var in range(2, num):
        if (num % var) == 0:
            print(num, "ist keine Primzahl")
            print(var, "*", num // var, "=", num)
            break
    else:
        print(num, "ist eine Primzahl.")
else:
    print(num, "ist keine Primzahl.")
