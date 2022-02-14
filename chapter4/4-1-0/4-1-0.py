x = 1
x + x + 1

from sympy import Symbol
x = Symbol('x')
x + x + 1

a = Symbol('x')
a + a + 1

# Symbolオブジェクトが表す記号を見つける
x = Symbol('x')
x.name
a = Symbol('x')
a.name

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

from sympy import symbols
x,y,z = symbols('x,y,z')

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + x*y
s

p = x*(x + x)
p

p = (x + 2) * (x + 3)
p
