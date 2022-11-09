from fractions import Fraction
x = Fraction(1, 3)                          #чисельник і знаменник
y = Fraction(4, 6)                          #скорочуе до 2 і 3 по найбільшому спільному знаменнику

print(x)
print(y)

print(x + y)
print(x - y)
print(x * y)

print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction(.25) + Fraction('1.25'))