from sympy import symbols
x,y = symbols('x,y')

# ここから
expr = x*x + 2*x*y + y*y

expr

from sympy import pprint
pprint(expr) # linux,MacOSではuse_unicode=True不要

expr = 1 + 2*x + 2*x**2
pprint(expr) # linux,MacOSではuse_unicode=True不要

from sympy import init_printing
init_printing(order='rev-lex')
pprint(expr) # linux,MacOSではuse_unicode=True不要
