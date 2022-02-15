from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12

solve((expr1, expr2), dict=True)

soln = solve((expr1, expr2), dict=True)
soln = soln[0]
expr1.subs({x: soln[x], y: soln[y]})
expr2.subs({x: soln[x], y: soln[y]})
