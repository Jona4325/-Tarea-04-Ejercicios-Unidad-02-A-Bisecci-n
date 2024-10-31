def bisection(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        print("El método de bisección no se puede aplicar.")
        return None
    c = a
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Definir la función
f = lambda x: x**3 - 7*x**2 + 14*x - 6

# Calcular la raíz en cada intervalo
root_1 = bisection(f, 0, 1)
root_2 = bisection(f, 1, 3.2)
root_3 = bisection(f, 3.2, 4)

print(f"Raíz en [0, 1]: {root_1}")
print(f"Raíz en [1, 3.2]: {root_2}")
print(f"Raíz en [3.2, 4]: {root_3}")
