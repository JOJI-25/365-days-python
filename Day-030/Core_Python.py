def traffic_summary(page_visits):
    # 1. Calculate total visits for each page
    totals = {}
    for page, visits in page_visits:
        totals[page] = totals.get(page, 0) + visits

    # Calculate overall total website traffic
    grand_total = sum(totals.values())

    # 2 & 5. Calculate percentage and rank pages from highest to lowest traffic
    ranked_pages = []
    for page, total_visits in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        percentage = (total_visits / grand_total) * 100
        ranked_pages.append({
            "page": page,
            "total_visits": total_visits,
            "percentage": round(percentage, 2)
        })

    # 3. Find the page with the highest total traffic
    highest_page = ranked_pages[0]["page"] if ranked_pages else None

    # 4. Create a list of pages responsible for more than 20% of total traffic
    major_pages = [item["page"] for item in ranked_pages if item["percentage"] > 20]

    return {
        "ranked_summary": ranked_pages,
        "highest_traffic_page": highest_page,
        "pages_over_20_percent": major_pages,
        "total_traffic": grand_total
    }

# --- Execution Example ---
page_visits = [
    ("Home", 4200),
    ("Products", 3100),
    ("Home", 1800),
    ("Pricing", 2200),
    ("Products", 2700),
    ("Blog", 1400),
    ("Pricing", 1900),
    ("Home", 2500),
    ("Blog", 900),
    ("Products", 1600),
]

summary = traffic_summary(page_visits)
print(summary)