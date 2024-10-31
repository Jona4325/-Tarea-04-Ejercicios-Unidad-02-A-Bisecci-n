import cmath

def calcular_raices_mejoradas(a, b, c):
    D = b**2 - 4 * a * c 
    
    if D >= 0:
        if b > 0:
            x1 = (-b - math.sqrt(D)) / (2 * a)
            x2 = c / (a * x1)
        else:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = c / (a * x1)
    else:
        x1 = (-b / (2 * a)) + cmath.sqrt(D) / (2 * a)
        x2 = (-b / (2 * a)) - cmath.sqrt(D) / (2 * a)
    
    return x1, x2

a = 1
b = -3
c = 2
x1, x2 = calcular_raices_mejoradas(a, b, c)

print("Raíz x1:", x1)
print("Raíz x2:", x2)

