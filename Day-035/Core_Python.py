def analyse_employee_skills(employees):
    # 1. Normalise skill names helper
    def normalise(skill):
        s = skill.strip().lower()
        if s == "python":
            return "Python"
        elif s in ("power bi", "powerbi"):
            return "Power BI"
        elif s == "machine learning":
            return "Machine Learning"
        return skill.title()

    total_employees = len(employees)
    norm_employees = {}
    skill_counts = {}
    
    # Process and normalise data
    for emp, skills in employees.items():
        norm_skills = set(normalise(s) for s in skills)
        norm_employees[emp] = norm_skills
        for s in norm_skills:
            skill_counts[s] = skill_counts.get(s, 0) + 1

    # Calculate percentage
    skill_percentages = {s: (count / total_employees) * 100 for s, count in skill_counts.items()}

    # Top 3 most common skills
    sorted_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)
    top_three = sorted_skills[:3]

    # Employees with both Python and SQL
    python_and_sql = [emp for emp, skills in norm_employees.items() if "Python" in skills and "SQL" in skills]

    # Employees with Power BI and DAX
    powerbi_and_dax = [emp for emp, skills in norm_employees.items() if "Power BI" in skills and "DAX" in skills]

    # Most frequent skill combination
    combination_counts = {}
    for skills in norm_employees.values():
        comb = tuple(sorted(skills))
        combination_counts[comb] = combination_counts.get(comb, 0) + 1
    most_common_comb = max(combination_counts.items(), key=lambda x: x[1])

    # Skills possessed by only one employee
    single_owner_skills = [s for s, count in skill_counts.items() if count == 1]

    return {
        "skill_counts": skill_counts,
        "skill_percentages": skill_percentages,
        "top_three_skills": top_three,
        "python_and_sql": python_and_sql,
        "powerbi_and_dax": powerbi_and_dax,
        "most_common_combination": most_common_comb,
        "single_owner_skills": single_owner_skills
    }

# --- Execution Example ---
employees = {
    "E101": ["Python", "SQL", "Excel", "Power BI"],
    "E102": ["python", "SQL", "Tableau"],
    "E103": ["Excel", "SQL", "Python"],
    "E104": ["Power BI", "DAX", "SQL"],
    "E105": ["Python", "Machine Learning", "SQL"],
    "E106": ["Excel", "PowerBI", "SQL"],
    "E107": ["Python", "DAX", "Power BI"],
    "E108": ["machine learning", "Python", "SQL"]
}

results = analyse_employee_skills(employees)