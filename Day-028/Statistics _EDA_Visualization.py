import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

delivery_time = np.array([
    28,
    31,
    29,
    35,
    30,
    32,
    27,
    29,
    34,
    31,
    30,
    28,
    33,
    29,
    31,
    75,
    30,
    32,
    28,
    34,
])

plt.figure(figsize=(8, 4))
sns.boxplot(x=delivery_time, color="skyblue")
plt.title("Delivery Time Distribution (Box Plot)")
plt.xlabel("Delivery Time (minutes)")
plt.show()