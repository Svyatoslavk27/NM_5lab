#5 лаба: природний кубічний інтерполяційний сплайн. 
# Записати в звіт все, що рахується (матриці, СЛАР, коефіцієнти, функції).
#  вивести графіки самого сплайна, його першої та другої похідної та оригінальної функції. 
# Провести аналіз наближення.
# Для тих, у кого в 4 лабі був сплайн: сплайн з четвертої лаби винести в окремий звіт і назвати це пʼятою лабою.
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(x):
    return 1 / x

x = np.linspace(1, 5, 15)
y = f(x)

f_spline = CubicSpline(x, y, bc_type='natural')

x_new = np.linspace(1, 5, 100)
y_spline = f_spline(x_new)

error_spline = np.abs(f(x_new) - y_spline)

f_spline_der1 = f_spline.derivative(1)
f_spline_der2 = f_spline.derivative(2)

fig, axs = plt.subplots(3, 1, figsize=(10, 15))

axs[0].plot(x, y, 'o', label='Дані')
axs[0].plot(x_new, f(x_new), '--', label='Точна функція', color='gray')
axs[0].plot(x_new, y_spline, label='Кубічний сплайн', color='green')
axs[0].set_title('Кубічний сплайн')
axs[0].legend()
axs[0].grid()

axs[1].plot(x_new, error_spline, label='Похибка кубічного сплайну', color='purple')
axs[1].set_title('Похибка кубічного сплайну')
axs[1].legend()
axs[1].grid()

axs[2].plot(x_new, f_spline_der1(x_new), label='Перша похідна', color='blue')
axs[2].plot(x_new, f_spline_der2(x_new), label='Друга похідна', color='brown')
axs[2].set_title('Похідні кубічного сплайну')
axs[2].legend()
axs[2].grid()

plt.tight_layout()
plt.show()
