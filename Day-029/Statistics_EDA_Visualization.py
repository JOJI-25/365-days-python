import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

usage = np.array([
    12, 15, 18, 20, 22, 25, 27, 30, 31, 32,
    34, 35, 37, 40, 42, 45, 48, 50, 52, 95
])

# Create the visualization
plt.figure(figsize=(8, 5))
sns.boxplot(x=usage, color="skyblue", fliersize=6)
sns.stripplot(x=usage, color="darkblue", alpha=0.6, jitter=0.2, size=7)

plt.title("Daily User Engagement Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Minutes Spent in App", fontsize=12)
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()

# Display the plot
plt.show()