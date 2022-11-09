from fractions import Fraction

print((2.5).as_integer_ratio())             #метод об'єкта з плаваючою крапкою

f = 2.5
z = Fraction(*f.as_integer_ratio())         #перетворює об'єкт з плаваючою крапкою в дроб
x = Fraction(1, 3)

print(z)
print(x)
print(x + z)

print(float(x))                             #перетворює дроб в об'єкт з плаваючою крапкою
print(float(z))
print(float(x + z))
print(17 / 6)

print(Fraction.from_float(1.75))            #перетворює об'єкт з плаваючою крапкою в дроб
print(Fraction(*(1.75).as_integer_ratio()))

print(x)
print(x + 2)                                #об'єкт дробу + об'єкт цілого числа = об'єкт дробу
print(x + 2.0)                              #об'єкт дробу + об'єкт с плаваючою крапкою = об'єкт з плаваючою крапкою
print(x + (1./3))                           #об'єкт дробу + об'єкт с плаваючою крапкою = об'єкт з плаваючою крапкою
print(x + (4./3))
print(x + Fraction(4, 3))                   #об'єкт дробу + об'єкт дробу = об'єкт дробу

print(4.0 / 3)
print((4.0 / 3).as_integer_ratio())         #точність втрачається через числа з плаваючою крапкою

print(x)
a = x + Fraction(*(4.0 / 3).as_integer_ratio())
print(a)
print(22517998136852479/13510798882111488)  #5/3(або близько)
print(a.limit_denominator(10))                     #спрощення до найближчого дробу