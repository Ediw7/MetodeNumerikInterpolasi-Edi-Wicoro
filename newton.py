import numpy as np
import matplotlib.pyplot as plt

# Data
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi polinom Newton
def newton_interpolation(x_data, y_data, x):
    n = len(x_data)
    coef = np.zeros([n, n])
    coef[:,0] = y_data
    
    for j in range(1, n):
        for i in range(n-j):
            coef[i, j] = (coef[i+1, j-1] - coef[i, j-1]) / (x_data[i+j] - x_data[i])
    
    def P(x):
        result = coef[0, 0]
        term = 1.0
        for j in range(1, n):
            term *= (x - x_data[j-1])
            result += coef[0, j] * term
        return result
    
    return P(x)

# Rentang x untuk plotting
x_range = np.linspace(5, 40, 400)

# Hitung nilai interpolasi Newton untuk setiap titik dalam x_range
y_newton = [newton_interpolation(x_data, y_data, xi) for xi in x_range]

# Plot hasil interpolasi Newton
plt.plot(x_data, y_data, 'o', label='Data')
plt.plot(x_range, y_newton, label='Newton Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()
