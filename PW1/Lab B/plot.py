import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3

# Read data, skipping the header
t, observed = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1, unpack=True)

# Analytical law calculation
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# Create 1x2 subplot with shared axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

ax1.scatter(t, observed, color="blue", s=10)
ax1.set_title("Observed Data")
ax1.set_xlabel("Time")
ax1.set_ylabel("Count")

ax2.plot(t, analytical, color="red")
ax2.set_title("Analytical Law")
ax2.set_xlabel("Time")
# Save the figure
plt.savefig("figure.png")
