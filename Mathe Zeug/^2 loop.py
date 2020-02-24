# x ^ 2 = y ^ 2 = z usw.


# a ^ 2 = b
# b ^ 2 = c


num1 = int(input("beginning? "))
num2 = int(input("ending? "))
num2 = num2 + 1

for n in range(num1, num2):
    square = n ** 2
    print(n, 'squared is', square)
    with open('dirty_file.txt', 'w') as outputfile:
        def loop():
            print(n, 'squared is', square, file=outputfile)
            loop()
    loop()
