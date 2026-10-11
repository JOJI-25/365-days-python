from collections import Counter

# Given Data
patients = [
    {"id": "P101", "priority": "Normal", "arrival_min": 35, "service_min": 12},
    {"id": "P102", "priority": "Urgent", "arrival_min": 10, "service_min": 20},
    {"id": "P103", "priority": "Normal", "arrival_min": 25, "service_min": 15},
    {"id": "P104", "priority": "Critical", "arrival_min": 5, "service_min": 30},
    {"id": "P105", "priority": "Urgent", "arrival_min": 20, "service_min": 18},
    {"id": "P106", "priority": "Normal", "arrival_min": 15, "service_min": 10},
    {"id": "P107", "priority": "Critical", "arrival_min": 40, "service_min": 25},
    {"id": "P108", "priority": "Urgent", "arrival_min": 30, "service_min": 14}
]

priority_rank = {
    "Critical": 1,
    "Urgent": 2,
    "Normal": 3
}

# --- Task 1: Sort patients by priority and then by arrival time ---
sorted_patients = sorted(
    patients, 
    key=lambda x: (priority_rank[x["priority"]], x["arrival_min"])
)

print("--- Task 1: Sorted Patients ---")
for p in sorted_patients:
    print(f"ID: {p['id']}, Priority: {p['priority']}, Arrival: {p['arrival_min']}m, Service: {p['service_min']}m")
print()


# --- Task 2: Count patients in each category and determine urgent/critical percentage ---
priority_counts = Counter(p["priority"] for p in patients)
total_patients = len(patients)
urgent_critical_count = priority_counts["Critical"] + priority_counts["Urgent"]
urgent_critical_percentage = (urgent_critical_count / total_patients) * 100

print("--- Task 2: Queue Statistics ---")
for prio, count in priority_counts.items():
    print(f"{prio}: {count} patients")
print(f"Urgent or Critical Percentage: {urgent_critical_percentage:.2f}%\n")


# --- Task 3 & 4: Calculate waiting times and averages based on a service schedule ---
def calculate_queue_schedule(patient_list):
    """
    Simulates the queue processing sequentially. 
    Each patient starts service either when they arrive or when the previous patient finishes, 
    whichever is later.
    """
    current_time = 0
    schedule_results = []
    
    for p in patient_list:
        # Service can only start when the patient has arrived and the machine/staff is free
        start_time = max(current_time, p["arrival_min"])
        wait_time = start_time - p["arrival_min"]
        finish_time = start_time + p["service_min"]
        
        schedule_results.append({
            "id": p["id"],
            "priority": p["priority"],
            "arrival_min": p["arrival_min"],
            "service_min": p["service_min"],
            "start_min": start_time,
            "wait_min": wait_time,
            "finish_min": finish_time
        })
        current_time = finish_time
        
    return schedule_results

simulated_schedule = calculate_queue_schedule(sorted_patients)

print("--- Task 3: Service Schedule & Waiting Times ---")
for item in simulated_schedule:
    print(f"Patient {item['id']} ({item['priority']}): Arrived at {item['arrival_min']}m, "
          f"Started at {item['start_min']}m, Waited {item['wait_min']}m")
print()

# Calculate average waiting time per priority category
category_wait_times = {}
for item in simulated_schedule:
    prio = item["priority"]
    if prio not in category_wait_times:
    	category_wait_times[prio] = []
    category_wait_times[prio].append(item["wait_min"])

print("--- Task 4: Average Waiting Time by Category ---")
max_wait_group = None
max_avg_wait = -1

for prio, waits in category_wait_times.items():
    avg_wait = sum(waits) / len(waits)
    print(f"{prio} Average Wait: {avg_wait:.2f} minutes")
    if avg_wait > max_avg_wait:
        max_avg_wait = avg_wait
        max_wait_group = prio

print(f"\nGroup experiencing the longest average wait: {max_wait_group} ({max_avg_wait:.2f} mins)\n")


# --- Task 5: Recommendation ---
"""
--- Task 5: Queue-Management Strategy Recommendation ---
1. Why FCFS (First-Come, First-Served) is Unsuitable:
   A strict FCFS policy treats all patients equally based solely on arrival time. 
   In a medical environment, a critical patient who arrives slightly later than a normal 
   patient could experience life-threatening delays if forced to wait behind routine cases.

2. Recommended Strategy (Priority-based Queue with Aging/Preemption Safeguards):
   - Implement a Weighted Priority Queue (as demonstrated above): Critical cases are always 
     treated first, followed by Urgent, then Normal.
   - Introduce an 'Aging' Mechanism: To prevent Normal priority patients from experiencing 
     indefinite starvation (infinitely long waits) if a continuous stream of urgent/critical 
     patients arrives, bump their priority up after a specific threshold (e.g., waiting > 45 minutes).
"""
print("--- Task 5: Recommendation ---")
print("Recommended Strategy: Priority-based queue with an aging mechanism to balance clinical urgency and fairness.")