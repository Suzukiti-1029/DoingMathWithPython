from sympy import Symbol, solve
x = Symbol('x')
expr = x**2 + 5*x + 4
solve(expr, dict=True)

x = Symbol('x')
expr = x**2 + x + 1
solve(expr)
