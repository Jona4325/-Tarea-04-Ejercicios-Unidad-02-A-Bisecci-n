def f(x):
    return x**3 - x - 1

def bisection(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        print("El método de bisección no se puede aplicar.")
        return None
    c = a
    iteration = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1
    print(f"Iteraciones realizadas: {iteration}")
    return c

# Encontrar la raíz en el intervalo [1, 2] con precisión de 10^-5
root = bisection(f, 1, 2, tol=1e-5)
print(f"Aproximación de la raíz: {root}")
