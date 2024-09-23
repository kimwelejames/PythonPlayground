import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
num_years = 5
num_days_per_year = 252
num_days = num_years * num_days_per_year
dt = 1 / num_days_per_year
mu = 0.1
sigma = 0.2
S0 = 100


shocks = np.random.normal(0, 1, num_days)


t = np.linspace(0, num_years, num_days)
S = S0 * np.exp(np.cumsum((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * shocks))

# Plotting the simulated stock price
plt.figure(figsize=(10, 6))
plt.plot(t, S, lw=2)
plt.title('Simulated Stock Price Movement')
plt.xlabel('Time (years)')
plt.ylabel('Stock Price ($)')
plt.grid(True)
plt.show()
