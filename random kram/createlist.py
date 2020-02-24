def listcreation():
    num1 = int(input("von? "))
    num2 = int(input("bis? "))
    num2 = num2 + 1
    with open('../list.txt', 'w') as generatedlist:
        print("list is getting generated")
        print(list(range(num1, num2)), file=generatedlist)
        print("list generated")
    listcreation()


listcreation()
