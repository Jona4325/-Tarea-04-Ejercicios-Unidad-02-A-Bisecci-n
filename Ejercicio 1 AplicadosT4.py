import numpy as np

def volume_difference(h, L=10, r=1, V=12.4):
    return L * (0.5 * np.pi * r**2 - r**2 * np.arcsin(h / r) - h * np.sqrt(r**2 - h**2)) - V

def bisection(f, a, b, tol=0.01):
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

# Calcular h usando el método de bisección en el intervalo [0, r]
h_solution = bisection(volume_difference, 0, 1)
print(f"La profundidad del agua h es aproximadamente: {h_solution} cm")
