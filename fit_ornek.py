import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x_data = np.linspace(0,1,500)
y_data = 7 * np.exp(3*x_data**2) * x_data**2 + np.random.rand(500) * 10

def model_function(x,A,B):
	return A * np.exp(B*x**2) * x**2

popt, pcov = curve_fit(model_function, x_data, y_data)

y_fit = model_function(x_data, popt[0], popt[1])

plt.plot(x_data,y_data,'o', alpha=0.3, label='data')
plt.plot(x_data, y_fit, 'k-', label='fit')
plt.legend(loc='best')
plt.show()