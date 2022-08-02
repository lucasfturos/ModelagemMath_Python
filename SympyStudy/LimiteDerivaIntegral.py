from sympy import Limit, Symbol, S, Derivative, Integral

# Limites
x = Symbol("x")
print("Limite de 1 / x, x -> infinito")
print(Limit(1 / x, x, S.Infinity, dir="-").doit())

# Derivada
t = Symbol("t")
St = 5 * t**2 + 2 * t + 8
print("\nDerivada da função f = (x**3 + x**2 + x) * (x**2 + x)")
print(Derivative(St, t).doit())
f = (x**3 + x**2 + x) * (x**2 + x)
print(Derivative(f, x).doit())

# Integral
k = Symbol("k")
print("\nIntegral Indefinida e Definida da função f = k * x")
print(Integral(k * x, x).doit())  # Indefinida
print(Integral(k * x, (x, 0, 2)).doit())  # Definida
