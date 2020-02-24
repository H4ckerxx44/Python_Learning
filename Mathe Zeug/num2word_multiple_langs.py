from num2words import num2words

num = int(input("Zahl? "))
print("Deutsch:", num2words(num, lang='de'))
print("Norwegisch:", num2words(num, lang='no'))
print("Englisch_US:", num2words(num, lang='en'))
print("Englisch_GB:", num2words(num, lang='en_GB'))
print("Französisch:", num2words(num, lang='fr'))
