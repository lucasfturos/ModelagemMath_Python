from sympy import *


print("\nA receita de uma empresa é dada por r(x)=419x e os custos por\nc(x)=271x+15000 em que x é a quantidade comercializada de um\ndeterminado produto. Determine o respectivo ponto de equilibrio\n")
x, r, c = symbols("x r c")
r = 419 * x
c = 271 * x + 15000.0
p = solve(Eq(r, c), x)
print(p)
print(r.subs(x, p[0]))
print("\n")
print("Solução de uma equação quadratica com variável x definida.\nA função sendo f = -7 * x**2 + 5200 * x - 80000\n")
x, f = symbols("x f")
f = -7 * x**2 + 5200 * x - 80000
print(f.subs(x, 350))
