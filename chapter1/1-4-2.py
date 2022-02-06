from fractions import Fraction
a = Fraction(input('Enter a fraction: '))
3/4
a

a = Fraction(input('Enter a fraction: '))
3/0

try:
  a = Fraction(input('Enter a fraction: '))
except ZeroDivisionError:
  print('Invalid fraction')
3/0

z = complex(input('Enter a complex number: '))
2+3j
z

z = complex(input('Enter a complex number: '))
2 + 3j
