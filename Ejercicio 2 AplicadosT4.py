def height_difference(t, s0=300, m=0.25, g=9.81, k=0.1):
    return s0 - (m * g / k) * t + (m / k) * (1 - np.exp(-k * t / m))
t_solution = bisection(height_difference, 0, 100, tol=0.01)
print(f"El tiempo que tarda en golpear el suelo es aproximadamente: {t_solution} segundos")
