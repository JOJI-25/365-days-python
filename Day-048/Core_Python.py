from collections import Counter
import string

# Given Data
reviews = [
    "App crashes during payment",
    "Payment failed twice",
    "Very slow loading speed",
    "App crashes after login",
    "Payment process is too slow",
    "Excellent user experience",
    "Slow loading and frequent crashes",
    "Payment failed during checkout",
    "Login is fast and easy",
    "Frequent payment failures",
    "Slow response from the app",
    "Excellent payment experience",
    "App crashes during checkout",
    "Loading speed is very slow"
]

stopwords = {
    "the", "is", "and", "a", "during", "after",
    "from", "too", "very", "twice"
}

# -------------------------------------------------------------
# Task 1: Normalise reviews (lowercase, remove punctuation, split)
# -------------------------------------------------------------
normalized_reviews = []
all_words = []

for review in reviews:
    # Convert to lowercase
    lower_review = review.lower()
    # Remove punctuation using string.punctuation
    clean_review = lower_review.translate(str.maketrans('', '', string.punctuation))
    # Split into individual words
    words = clean_review.split()
    normalized_reviews.append(words)
    all_words.extend(words)

print("--- Task 1: Sample Normalized Words ---")
print(normalized_reviews[:3])
print()

# -------------------------------------------------------------
# Task 2: Count word frequency (excluding stopwords) and top 5 words
# -------------------------------------------------------------
filtered_words = [word for word in all_words if word not in stopwords]
word_counts = Counter(filtered_words)
top_5_words = word_counts.most_common(5)

print("--- Task 2: Top 5 Frequent Words ---")
for word, freq in top_5_words:
    print(f"'{word}': {freq} times")
print()

# -------------------------------------------------------------
# Task 3: Find reviews with both "payment" and "failed" & percentage
# -------------------------------------------------------------
matching_reviews = []
for review in reviews:
    lower_words = review.lower().translate(str.maketrans('', '', string.punctuation)).split()
    if "payment" in lower_words and "failed" in lower_words:
        matching_reviews.append(review)

percentage = (len(matching_reviews) / len(reviews)) * 100

print("--- Task 3: Reviews with 'payment' and 'failed' ---")
print(f"Matching reviews: {matching_reviews}")
print(f"Percentage of total reviews: {percentage:.2f}%")
print()

# -------------------------------------------------------------
# Task 4: Reusable categorisation function using keyword rules
# -------------------------------------------------------------
def categorise_review(review_text):
    text = review_text.lower()
    
    # Keyword-based rules
    if any(keyword in text for keyword in ["payment", "checkout", "failures", "failed"]):
        return "Payment"
    elif any(keyword in text for keyword in ["slow", "speed", "crashes", "response", "loading"]):
        return "Performance"
    elif any(keyword in text for keyword in ["login"]):
        return "Login"
    else:
        return "Other"

# Apply function to all reviews
categorized_results = [(review, categorise_review(review)) for review in reviews]

print("--- Task 4: Categorised Reviews (Sample) ---")
for rev, cat in categorized_results[:5]:
    print(f"[{cat}] {rev}")
print()

# -------------------------------------------------------------
# Task 5: Summarise counts and provide a recommendation
# -------------------------------------------------------------
category_counts = Counter([cat for _, cat in categorized_results])

print("--- Task 5: Category Summary ---")
for cat, count in category_counts.items():
    print(f"{cat}: {count} reviews")