import numpy as np
import matplotlib.pyplot as plt

# Define layer spacing d and tilt angle θ for SmC
d = 50  # Layer spacing in Å
theta_deg = 20  # Tilt angle in degrees
theta = np.radians(theta_deg)  # Convert to radians

# Define SAXS q values
q_values = np.linspace(0.05, 0.3, 500)  # q range in Å⁻¹
n_values = np.arange(1, 6)  # First 5 Bragg peaks

# Compute Bragg peaks for Smectic A
q_sma = (2 * np.pi * n_values) / d

# Compute Bragg peaks for Smectic C (tilted molecules)
q_smc = (2 * np.pi * n_values * np.cos(theta)) / d

# Define Lorentzian peak function for broadening
def lorentzian(q, q_center, gamma=0.005):
    return 1 / ((q - q_center)**2 + gamma**2)

# Generate SAXS intensity for SmA and SmC
I_sma = np.zeros_like(q_values)
I_smc = np.zeros_like(q_values)

for q in q_sma:
    I_sma += lorentzian(q_values, q)

for q in q_smc:
    I_smc += lorentzian(q_values, q)

# 📊 Plot SAXS Comparison
plt.figure(figsize=(8,5))
plt.plot(q_values, I_sma, label="Smectic A", color='b')
plt.plot(q_values, I_smc, label=f"Smectic C (Tilt = {theta_deg}°)", color='r')
plt.axvline(q_sma[0], color='b', linestyle="--", alpha=0.5, label="SmA First Peak")
plt.axvline(q_smc[0], color='r', linestyle="--", alpha=0.5, label="SmC First Peak")
plt.xlabel("q (Å⁻¹)")
plt.ylabel("Intensity (a.u.)")
plt.title("Simulated SAXS for Smectic A vs. Smectic C")
plt.legend()
plt.show()