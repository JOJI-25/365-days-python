listening = {
    "U201": {"Rock": 42, "Pop": 35, "Jazz": 8, "Classical": 5},
    "U202": {"Rock": 10, "Pop": 52, "Jazz": 18, "Classical": 12},
    "U203": {"Rock": 65, "Pop": 8, "Jazz": 4, "Classical": 3},
    "U204": {"Rock": 24, "Pop": 28, "Jazz": 22, "Classical": 19},
    "U205": {"Rock": 15, "Pop": 31, "Jazz": 27, "Classical": 21}
}

# Calculate the total number of songs played by each user and identify the most active user.

total_per_user = {user: sum(genere.values()) for user, genere in listening.items()}
most_active_user = max(total_per_user, key=total_per_user.get)

print("--- 1. Total Songs per User ---")
for user, total in total_per_user.items():
    print(f"User {user}: {total} songs")
print(f"Most Active User: {most_active_user} ({total_per_user[most_active_user]} songs)\n")

# Calculate the total number of plays for each genre across all users and identify the most popular genre.

genres_list = ["Rock", "Pop", "Jazz", "Classical"]
total_per_genre = {genre: sum(listening[user][genre] for user in listening) for genre in genres_list}
most_popular_genre = max(total_per_genre, key=total_per_genre.get)

print("--- 2. Total Plays per Genre ---")
for genre, total in total_per_genre.items():
    print(f"{genre}: {total} plays")
print(f"Most Popular Genre: {most_popular_genre} ({total_per_genre[most_popular_genre]} plays)\n")

# For each user, determine their most-played genre and calculate what percentage of their total listening activity belongs to that genre.

user_top_genre = {}
print("--- 3. Top Genre & Percentage per User ---")
for user, genres in listening.items():
    top_genre = max(genres, key=genres.get)
    percentage = (genres[top_genre] / total_per_user[user]) * 100
    user_top_genre[user] = (top_genre, percentage)
    print(f"User {user}: {top_genre} ({percentage:.2f}%)")
print()

# Create a function that classifies users as "Focused", "Balanced", or "Highly Diverse" based on the percentage contribution of their most-played genre, using thresholds you define.

def classify_user(percentage):
    if percentage > 60:
        return "Focused"
    elif percentage >= 40:
        return "Balanced"
    else:
        return "Highly Diverse"

print("--- 4. User Classifications ---")
classifications = {user: classify_user(data[1]) for user, data in user_top_genre.items()}
for user, category in classifications.items():
    print(f"User {user}: {category} ({user_top_genre[user][1]:.2f}% in {user_top_genre[user][0]})")
print()

# Determine whether the most active user is also the most diverse listener, and explain why total activity alone may not be sufficient to understand user behaviour.

most_diverse_user = min(user_top_genre, key=lambda u: user_top_genre[u][1])
print("--- 5. Diversity Analysis ---")
print(f"Most Active User: {most_active_user} (Total plays: {total_per_user[most_active_user]})")
print(f"Most Diverse User: {most_diverse_user} (Top genre percentage: {user_top_genre[most_diverse_user][1]:.2f}%)")
