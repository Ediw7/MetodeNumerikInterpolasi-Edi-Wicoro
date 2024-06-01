import numpy as np
import matplotlib.pyplot as plt

# Data
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi polinom Lagrange
def lagrange_interpolation(x_data, y_data, x):
    def L(k, x):
        term = [(x - x_data[j]) / (x_data[k] - x_data[j]) for j in range(len(x_data)) if j != k]
        return np.prod(term)
    
    return sum(y_data[k] * L(k, x) for k in range(len(x_data)))

# Plot hasil interpolasi Lagrange
x_range = np.linspace(5, 40, 400)
y_lagrange = [lagrange_interpolation(x_data, y_data, xi) for xi in x_range]

plt.plot(x_data, y_data, 'o', label='Data')
plt.plot(x_range, y_lagrange, label='Lagrange Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)
plt.show()
