import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load ratings dataset
ratings = pd.DataFrame(
    {
        "User_A": [5, 4, np.nan, 1, 2, np.nan],
        "User_B": [4, 5, 4, np.nan, 1, 2],
        "User_C": [np.nan, 4, 5, 1, np.nan, 2],
        "User_D": [1, np.nan, 2, 5, 4, 5],
        "User_E": [2, 1, np.nan, 4, 5, 4],
        "User_F": [np.nan, 2, 1, 5, 4, np.nan],
        "User_G": [5, 4, 5, np.nan, 1, 1],
        "User_H": [1, 2, np.nan, 5, 4, 5],
    },
    index=["Book_A", "Book_B", "Book_C", "Book_D", "Book_E", "Book_F"],
)
ratings.index.name = "book"

# 1. Sparsity and Sparsest Books
total_cells = ratings.size
missing_cells = ratings.isna().sum().sum()
sparsity_pct = (missing_cells / total_cells) * 100
ratings_per_book = ratings.notna().sum(axis=1)
sparsest_books = ratings_per_book[
    ratings_per_book == ratings_per_book.min()
].index.tolist()

print("--- 1. Sparsity Analysis ---")
print(f"Matrix Sparsity: {sparsity_pct:.2f}%")
print(f"Books with the fewest ratings: {sparsest_books}")

# 2. Item-to-Item Cosine Similarity (treating NaNs as zero)
ratings_filled = ratings.fillna(0)
similarity_matrix = pd.DataFrame(
    cosine_similarity(ratings_filled),
    index=ratings.index,
    columns=ratings.index,
)

print("\n--- 2. Item Similarity Matrix Shape ---")
print(similarity_matrix.shape)


# 3. Recommendation Function for User_C
def recommend_books(user_name, ratings_df, sim_matrix, top_n=3):
  user_ratings = ratings_df[user_name]
  unrated_books = user_ratings[user_ratings.isna()].index

  predicted_scores = {}
  for book in unrated_books:
    # Get similarities of this unrated book to all other books
    sims = sim_matrix.loc[book]
    # Get ratings given by the user for other books
    known_ratings = user_ratings.dropna()

    # Exclude the book itself and items with no similarity or rating
    sims = sims[known_ratings.index]

    if sims.sum() == 0:
      predicted_scores[book] = 0
    else:
      # Weighted average of ratings based on item similarity
      predicted_scores[book] = np.dot(sims, known_ratings) / sims.abs().sum()

  # Sort predictions descending
  sorted_preds = sorted(
      predicted_scores.items(), key=lambda x: x[1], reverse=True
  )
  return sorted_preds[:top_n]


top_recommendations = recommend_books("User_C", ratings, similarity_matrix, top_n=3)
print(f"\n--- 3. Top 3 Recommendations for User_C ---")
for book, score in top_recommendations:
  print(f"{book}: Estimated Score = {score:.2f}")


# 4. Held-out Rating Evaluation Experiment
def evaluate_model(ratings_df, test_user="User_A"):
  # Pick a known rating to hide
  known_items = ratings_df[test_user].dropna()
  test_book = known_items.index[0]
  true_value = known_items[test_book]

  # Create a train matrix with the value hidden
  train_ratings = ratings_df.copy()
  train_ratings.loc[test_book, test_user] = np.nan

  # Recompute similarity on filled train matrix
  train_filled = train_ratings.fillna(0)
  train_sim = pd.DataFrame(
      cosine_similarity(train_filled),
      index=train_ratings.index,
      columns=train_ratings.index,
  )

  # Predict the hidden rating
  user_ratings = train_ratings[test_user]
  sims = train_sim.loc[test_book][user_ratings.dropna().index]
  predicted_value = (
      np.dot(sims, user_ratings.dropna()) / sims.abs().sum()
      if sims.sum() != 0
      else 0
  )

  return test_book, true_value, predicted_value


test_book, true_val, pred_val = evaluate_model(ratings, "User_A")
print(f"\n--- 4. Held-Out Evaluation ---")
print(
    f"Target Book: {test_book} | True Rating: {true_val} | Predicted Rating:"
    f" {pred_val:.2f}"
)