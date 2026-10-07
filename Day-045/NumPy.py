import numpy as np

temperature = np.array([
    [62.5, 64.1, 63.8, 65.2, 66.0, 64.7],
    [68.2, 69.5, 70.1, 71.3, 72.0, 73.2],
    [59.8, 60.5, 61.2, 60.9, 62.1, 61.7],
    [75.1, 76.8, 78.2, 77.5, 80.1, 82.4]
])

processors = np.array(["P1", "P2", "P3", "P4"])

# Calculate the mean and maximum temperature for each processor and identify the processor with the highest thermal load.
processor_mean = temperature.mean(axis=1)
processor_max = temperature.max(axis=1)
high_processor = np.argmax(processor_max)
print("Processor Mean Temperature:", processor_mean)
print("Processor Max Temperature:", processor_max)
print("Processor with Highest Thermal Load:", processors[high_processor])