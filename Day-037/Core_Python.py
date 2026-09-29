tickets = [
    {"id": 101, "category": "Login", "priority": "High", "hours": 3.5},
    {"id": 102, "category": "Payment", "priority": "Medium", "hours": 8.0},
    {"id": 103, "category": "Login", "priority": "Low", "hours": 12.5},
    {"id": 104, "category": "Bug", "priority": "High", "hours": 5.0},
    {"id": 105, "category": "Payment", "priority": "High", "hours": 2.5},
    {"id": 106, "category": "Bug", "priority": "Medium", "hours": 10.0},
    {"id": 107, "category": "Login", "priority": "Medium", "hours": 6.5},
    {"id": 108, "category": "Bug", "priority": "Low", "hours": 18.0}
]

each_category = {}


for t in tickets:
    cat  = t['category']
    each_category[cat] = each_category.get(cat, 0) + 1

longest = max(tickets, key=lambda t:t['hours'])
shortest = min(tickets, key=lambda t:t['hours'])

priority_hours = {"High": [], "Medium": [], "Low": []}
for t in tickets:
  priority_hours[t["priority"]].append(t["hours"])

avg_by_priority = {
    p: sum(hrs) // len(hrs) if hrs else 0 for p, hrs in priority_hours.items()
}

def classify_resolution(hours):
  if hours < 4:
    return "Urgent"
  elif 4 <= hours <= 10:
    return "Normal"
  else:
    return "Slow"

category_stats = {}
for t in tickets:
  cat = t["category"]
  status = classify_resolution(t["hours"])
  if cat not in category_stats:
    category_stats[cat] = {"total": 0, "slow": 0}
  category_stats[cat]["total"] += 1
  if status == "Slow":
    category_stats[cat]["slow"] += 1

proportions = {
    cat: stats["slow"] / stats["total"] for cat, stats in category_stats.items()
}
highest_slow_category = max(proportions, key=proportions.get)
print(f"Category with highest slow resolution: {highest_slow_category}")
 


