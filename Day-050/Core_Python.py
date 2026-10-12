downtime_logs = {
    "Machine_A": [(10, 25), (20, 35), (45, 60), (55, 70), (90, 100)],
    "Machine_B": [(5, 15), (18, 30), (28, 40), (50, 65)],
    "Machine_C": [(12, 22), (25, 38), (40, 55), (53, 68)],
}


def merge_intervals(intervals, handle_adjacent=False):
  if not intervals:
    return []

  # Sort intervals by start time
  sorted_intervals = sorted(intervals, key=lambda x: x[0])
  merged = [sorted_intervals[0]]

  for current in sorted_intervals[1:]:
    last_start, last_end = merged[-1]
    current_start, current_end = current

    # Check for overlap or adjacency based on flag
    # Adjacent rule: current_start <= last_end (e.g., (10, 20) and (20, 30))
    # Strict overlap rule: current_start < last_end
    condition = (
        (current_start <= last_end)
        if handle_adjacent
        else (current_start < last_end)
    )

    if condition:
      # Merge by updating the end time of the last interval
      merged[-1] = (last_start, max(last_end, current_end))
    else:
      merged.append(current)

  return merged


def calculate_downtime(intervals):
  return sum(end - start for start, end in intervals)


# 1 & 2. Process each machine (handling overlapping and adjacent intervals)
results = {}
total_combined_downtime = 0

for machine, intervals in downtime_logs.items():
  # Set handle_adjacent=True to also merge touching intervals like (10, 20) and (20, 30)
  merged = merge_intervals(intervals, handle_adjacent=True)
  downtime = calculate_downtime(merged)
  results[machine] = {"merged": merged, "downtime": downtime}
  total_combined_downtime += downtime

# 3. Identify machine with highest downtime and its percentage
highest_machine = max(results, key=lambda k: results[k]["downtime"])
highest_downtime = results[highest_machine]["downtime"]
percentage = (highest_downtime / total_combined_downtime) * 100

# Print results
print("--- Downtime Analysis Results ---")
for machine, data in results.items():
  print(
      f"{machine}: Merged Intervals = {data['merged']}, Total Downtime ="
      f" {data['downtime']} minutes"
  )

print(f"\nTotal Combined Downtime: {total_combined_downtime} minutes")
print(
    f"Machine with Highest Downtime: {highest_machine} ({highest_downtime}"
    f" minutes, {percentage:.2f}% of total)"
)