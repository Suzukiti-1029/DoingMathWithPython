from sympy import sympify
expr = input('Enter a mathematical expression: ')
x**2 + 3*x + x**3 + 2*x
expr = sympify(expr)

2 * expr

expr = input('Enter a mathematic expression: ')
x**2 + 3*x + x**3 + 2x
expr = sympify(expr) # SympifyError

from sympy import sympify
from sympy.core.sympify import SympifyError
expr = input('Enter a mathematical expression: ')
x**2 + 3*x + x**3 + 2x
try:
  expr = sympify(expr)
except SympifyError:
  print('Invalid input')
