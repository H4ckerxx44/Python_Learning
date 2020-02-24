# ----------------------------------------------------------------------
# calculates area and volume of 2d/3d rectangles with variable size
#
# (c) 2020 Dennis Wortmann, Hamm, Germany
# Not Released to public
# email dennis.wortmann1999@gmail.com
# ----------------------------------------------------------------------


from num2words import num2words as n2w


class BasisRechnungen:
    def __init__(self, L, B, H):
        self.length = L
        self.width = B
        self.depth = H

    def volume(self):
        return self.length * self.width * self.depth

    def area(self):
        return self.length * self.width


# calc = BasisRechnungen(10, 15, 10)                                # just for testing purposes
calc = BasisRechnungen(int(input("Länge ")), int(input("Breite ")), int(input("Höhe ")))
print("Fläche: ", calc.area(), "cm²\n""In Worten: ", n2w(calc.area(), lang='de'))
print("")
print("Volumen: ", calc.volume(), "cm³\n""In Worten: ", n2w(calc.volume(), lang='de'))
