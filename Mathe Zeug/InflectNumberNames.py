import inflect

number = int(input("Enter Number "))
p = inflect.engine()
print(number, "name is actually", p.number_to_words(number))
