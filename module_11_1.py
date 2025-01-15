import numpy as np
import matplotlib.pyplot as plt


def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + np.sqrt(d)) / (2 * a)
        x2 = (-b - np.sqrt(d)) / (2 * a)
        return [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return None


a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if a == 0:
    print("Коэффициент 'a' не должен быть равен нулю.")
else:
    roots = solve_quadratic(a, b, c)

    x = np.linspace(-10, 10, 400)
    y = a * x ** 2 + b * x + c

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}', color='blue')
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)

    if roots is None:
        print("Корней нет.")
    else:
        for root in roots:
            plt.plot(root, 0, 'ro')
            plt.annotate(f'Корень: {root:.2f}', xy=(root, 0), xytext=(root, 5))

plt.title('График квадратного уравнения')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.ylim(-10, 10)
plt.xlim(-10, 10)

plt.show()
