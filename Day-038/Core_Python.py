deliveries = [
    {"driver": "Asha", "distance": 42, "fuel": 5.2, "late": False},
    {"driver": "Rahul", "distance": 35, "fuel": 4.8, "late": True},
    {"driver": "Neha", "distance": 58, "fuel": 7.1, "late": False},
    {"driver": "Vijay", "distance": 29, "fuel": 4.5, "late": True},
    {"driver": "Arun", "distance": 64, "fuel": 7.5, "late": False},
    {"driver": "Meera", "distance": 47, "fuel": 5.9, "late": True},
    {"driver": "Kiran", "distance": 51, "fuel": 6.0, "late": False},
    {"driver": "Diya", "distance": 38, "fuel": 4.9, "late": False}
]

total_distance = sum(d["distance"] for d in deliveries)
total_fuel = sum(d["fuel"] for d in deliveries)

efficiencies = {}
for d in deliveries:
    eff = d["distance"] / d["fuel"]
    efficiencies[d["driver"]] = eff

most_efficient_driver = max(efficiencies, key=efficiencies.get)

status_dict = {d["driver"]: ("Late" if d["late"] else "On Time") for d in deliveries}

def classify_efficiency(eff):
    if eff < 7:
        return "Poor"
    elif 7 <= eff <= 9:
        return "Average"
    else:
        return "Efficient"

print(f"Total Distance: {total_distance}")
print(f"Total Fuel: {total_fuel}")
for name, eff in efficiencies.items():
    print(f"{name}: {eff:.2f} km/l ({classify_efficiency(eff)})")

print(f"Most Efficient: {most_efficient_driver} with {efficiencies[most_efficient_driver]:.2f} km/l")

late_effs = [d["distance"]/d["fuel"] for d in deliveries if d["late"]]
ontime_effs = [d["distance"]/d["fuel"] for d in deliveries if not d["late"]]

print(f"Late Avg Eff: {sum(late_effs)/len(late_effs):.2f}")
print(f"On-time Avg Eff: {sum(ontime_effs)/len(ontime_effs):.2f}")