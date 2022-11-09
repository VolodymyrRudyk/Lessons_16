a = 1 / 3.0                         #результат точний настільки, наскільки дозволяють апаратні засоби
b = 4 / 6.0

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)

print(0.1 + 0.1 + 0.1 - 0.3)        #повинен бути 0(близько, но не точно)

from fractions import Fraction
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

print(1/3)
print(Fraction(1,3))

import decimal
decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))

print((1 / 3) + (6 / 12))
print(Fraction(6, 12))              #результат автоматично спрощується
print(Fraction(1, 3) + Fraction(6, 12))

print(decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12)))
print(1000.0 / 1234567890)
print(Fraction(1000, 123456789))