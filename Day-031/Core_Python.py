def analyse_reviews(reviews):
    # Dictionaries to track total score and review counts per product
    totals = {}
    counts = {}

    for product_id, score in reviews:
        totals[product_id] = totals.get(product_id, 0) + score
        counts[product_id] = counts.get(product_id, 0) + 1

    # 1. Dictionary containing the number of reviews for each product
    review_counts = counts.copy()

    # 2. Calculate average review score for each product
    averages = {}
    for product_id in totals:
        averages[product_id] = totals[product_id] / review_counts[product_id]

    # 3. Classify each product based on its average score
    classifications = {}
    for product_id, avg in averages.items():
        if avg >= 4:
            classifications[product_id] = "Positive"
        elif 3 <= avg < 4:
            classifications[product_id] = "Neutral"
        else:
            classifications[product_id] = "Negative"

    # 4. Find the product with the highest average rating
    highest_rated_product = max(averages, key=averages.get)

    # 5. Find the product with the largest number of reviews
    most_reviewed_product = max(review_counts, key=review_counts.get)

    # 6. Create a ranking of products based on average rating (highest to lowest)
    ranked_products = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    return {
        "review_counts": review_counts,
        "average_scores": averages,
        "classifications": classifications,
        "highest_rated": highest_rated_product,
        "most_reviewed": most_reviewed_product,
        "rating_ranking": ranked_products,
    }


# --- Execution Example ---
reviews = [
    ("P101", 5),
    ("P102", 4),
    ("P101", 2),
    ("P103", 3),
    ("P102", 5),
    ("P101", 4),
    ("P104", 1),
    ("P103", 4),
    ("P104", 2),
    ("P102", 3),
    ("P105", 5),
    ("P105", 4),
]

results = analyse_reviews(reviews)

print("Review Counts:", results["review_counts"])
print("Average Scores:", results["average_scores"])
print("Classifications:", results["classifications"])
print("Highest Rated Product:", results["highest_rated"])
print("Most Reviewed Product:", results["most_reviewed"])
print("Rating Ranking:", results["rating_ranking"])