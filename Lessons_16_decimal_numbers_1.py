print(0.1 + 0.1 + 0.1 - 0.3)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))                              #за замовчанням 28  цифр

decimal.getcontext().prec = 4                                               #фіксована точність
print(decimal.Decimal(1) / decimal.Decimal(7))

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))            #ближче до 0