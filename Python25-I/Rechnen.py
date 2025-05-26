#Variablen
xint = 10
yint = 10
xfloat = 13.2
yfloat = 6.8

#Addition
print("Addition:")
erg_add_int = xint + yint # int + int
print(erg_add_int)
erg_add_float = xfloat + yfloat # float + float
print(erg_add_float)
erg_add_int_float = xint + yfloat # int + float
print(erg_add_int_float)
erg_add_float_int = yfloat + xint # float + int
print(erg_add_float_int)


#Subtraktion
print("\nSubtraktion")
erg_sub_int = xint - yint # int - int
print(erg_sub_int)
erg_sub_float = xfloat - yfloat # float - float
print(erg_sub_float)
erg_sub_int_float = xint - yfloat # int - float
print(erg_sub_int_float)
erg_sub_float_int = yfloat - xint # float - int
print(erg_sub_float_int)

#Multiplikation
print("\nMultiplikation")
erg_mult_int = xint * yint # int * int
print(erg_mult_int)
erg_mult_float = xfloat * yfloat # float * float
print(erg_mult_float)
erg_mult_int_float = xint * yfloat # int * float
print(erg_mult_int_float)
erg_mult_float_int = yfloat * xint # float * int
print(erg_mult_float_int)

#Division
print("\nDivision")
erg_div_int = xint / yint # int / int
print(erg_div_int)
erg_div_int_ganz = xint // yint # int // int
print(erg_div_int_ganz)
erg_div_int_rest = xint % yint # int % int
print(erg_div_int_rest)
erg_div_float = xfloat / yfloat # float / float
print(erg_div_float)
erg_div_int_float = xint / yfloat # int / float
print(erg_div_int_float)
erg_div_float_int = yfloat / xint # float / int
print(erg_div_float_int)

#Potenz
print("\nPotenz")
erg_pot_int = xint ** yint # int ** int
print(erg_pot_int)
erg_pot_int_negativ = xint ** (-yint) # int ** int
print(erg_pot_int_negativ)
erg_pot_float = xfloat ** yfloat # float ** float
print(erg_pot_float)
erg_pot_int_float = xint ** yfloat # int ** float
print(erg_pot_int_float)
erg_pot_float_int = yfloat ** xint # float ** int
print(erg_pot_float_int)

#Kurzschreibweise
x = 12
x += 12 # Entspricht x = x + 12
x *= 12 # Entspricht x = x * 12
x -= 12 # Entspricht x = x - 12
x /= 12 # Entspricht x = x / 12
x %= 12 # Entspricht x = x % 12
x //= 12 # Entspricht x = x // 12
x **= 12 # Entspricht x = x ** 12

#Vergleichsoperatoren
print("\nVergleichsoperatoren")
erg_gleich = xint == yint
print(erg_gleich)
erg_ungleich = xint != yint
print(erg_ungleich)
erg_kleiner = xint < yint
print(erg_kleiner)
erg_groesser = xint > yint
print(erg_groesser)
erg_kleiner_gleich = xint <= yint
print(erg_kleiner_gleich)
erg_groesser_gleich = xint >= yint
print(erg_groesser_gleich)

# logische Operatoren
print("\nlogische Operatoren")
xbool = True
ybool = False
erg_not = not xbool
print(erg_not)
erg_and = xbool and ybool
print(erg_and)
erg_or = xbool or ybool
print(erg_or)
erg_and = xbool and 3>5
print(erg_and)