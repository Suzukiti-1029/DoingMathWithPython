from sympy import Symbol
# ここから
x = Symbol('x')
y = Symbol('y')
x*x + x*y + x*y + y*y

expr = x*x + x*y + x*y + y*y
res = expr.subs({x: 1, y: 2})

res

expr.subs({x: 1-y})

# Python辞書
sampledict = {"key1": 5, "key2": 20}
sampledict["key1"]

expr_subs = expr.subs({x: 1-y})
from sympy import simplify
simplify(expr_subs)
