from sympy import Symbol
x = Symbol('x')
y = Symbol('y')

from sympy import factor, expand
expr = x**2 - y**2
factor(expr)

from sympy import expand
factors = factor(expr)
expand(factors)

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
factors
expand(factors)

expr = x + y + x*y
factor(expr)
