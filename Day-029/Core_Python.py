import pandas as pd

skills = [
    "Python", "SQL", "python", "Power BI", "Excel",
    "sql", "Machine Learning", "Python", "Excel",
    "Tableau", "machine learning", "SQL", "Pandas",
    "pandas", "Python"
]

# Helper function to standardise and format skill names
def format_skill(skill_name):
    clean_name = skill_name.strip().lower()
    if clean_name == "sql":
        return "SQL"
    elif clean_name == "power bi":
        return "Power BI"
    else:
        return clean_name.title()

# 1, 2 & 3. Normalise skill names, count frequencies, and produce a dictionary
skill_counts = {}
for skill in skills:
    formatted_skill = format_skill(skill)
    skill_counts[formatted_skill] = skill_counts.get(formatted_skill, 0) + 1

# 4. Find the most frequently mentioned skill
most_frequent_skill = max(skill_counts, key=skill_counts.get)

# 5. Create a list of skills that appear at least 2 times
frequent_skills = [skill for skill, count in skill_counts.items() if count >= 2]

# 6. Produce a ranking of skills from most to least frequently mentioned
ranked_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)

# --- Results Output ---
print("Skill Frequency Dictionary:", skill_counts)
print(f"Most Frequently Mentioned Skill: {most_frequent_skill} ({skill_counts[most_frequent_skill]} times)")
print("Skills Appearing at Least 2 Times:", frequent_skills)
print("Ranked Skills (High to Low):", ranked_skills)