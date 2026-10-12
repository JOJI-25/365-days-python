import numpy as np

# GPS coordinates: latitude and longitude in decimal degrees
gps = np.array([
    [9.5000, 76.3000],
    [9.5050, 76.3050],
    [9.5100, 76.3100],
    [9.5150, 76.3150],
    [9.7000, 76.5000],
    [9.5200, 76.3200],
    [9.5250, 76.3250],
    [9.5300, 76.3300],
])

# Time elapsed between consecutive observations, in minutes
time_gap = np.array([10, 10, 10, 10, 10, 10, 10])


def haversine_np(coord1, coord2, radius_km=6371.0):
  """Calculate the great-circle distance between two points

  on the Earth surface using the Haversine formula with NumPy.
  """
  lat1, lon1 = np.radians(coord1[:, 0]), np.radians(coord1[:, 1])
  lat2, lon2 = np.radians(coord2[:, 0]), np.radians(coord2[:, 1])

  dlat = lat2 - lat1
  dlon = lon2 - lon1

  a = (
      np.sin(dlat / 2.0) ** 2
      + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
  )
  c = 2 * np.arcsin(np.sqrt(a))
  return radius_km * c


# 1. Calculate distances between consecutive pairs (in km)
point1 = gps[:-1]
point2 = gps[1:]
distances = haversine_np(point1, point2)

# 2. Calculate movement speed in km/h
# Speed = (distance / time_in_hours) -> time_in_hours = time_gap / 60
time_hours = time_gap / 60.0
speeds = distances / time_hours

# 3. Identify intervals exceeding the 15 km/h threshold
threshold = 15.0
outliers = np.where(speeds > threshold)[0]

# 4. Calculate median speeds
median_all = np.median(speeds)
valid_speeds = speeds[speeds <= threshold]
median_filtered = np.median(valid_speeds)

# Print Results
print("--- Sea Turtle Movement Analysis ---")
for i in range(len(distances)):
  print(
      f"Interval {i+1} (Obs {i} -> {i+1}): Distance = {distances[i]:.3f} km,"
      f" Speed = {speeds[i]:.2f} km/h"
  )

print(f"\nSuspicious Intervals (Speed > 15 km/h): Index {outliers.tolist()}")
print(f"Median Speed (All intervals): {median_all:.2f} km/h")
print(f"Median Speed (Filtered intervals): {median_filtered:.2f} km/h")