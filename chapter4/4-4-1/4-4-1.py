from sympy import Symbol, solve, sympify
# ここから
expr = input('Enter an expression: ')
2*x + 3*y - 6
expr = sympify(expr)
y = Symbol('y')
solve(expr, y)

solutions = solve(expr, 'y')
expr_y = solutions[0]
expr_y
