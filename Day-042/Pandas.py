import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "user_id": range(601, 613),
    "content_type": [
        "Movie", "Series", "Sports", "Movie",
        "Series", "Documentary", "Sports", "Series",
        "Movie", "Documentary", "Sports", "Series"
    ],
    "sessions": [8, 15, 12, 5, 18, 7, 20, 14, 9, 6, 16, 22],
    "avg_session_min": [95, 48, 72, 110, 52, 85, 65, 55, 102, 91, 68, 50],
    "completion_rate": [0.82, 0.76, 0.68, 0.91, 0.81, 0.88, 
                        0.72, 0.79, 0.86, 0.90, 0.74, 0.83],
    "monthly_fee": [499, 499, 699, 399, 499, 699, 
                    699, 499, 399, 699, 699, 499]
}
df = pd.DataFrame(data)

# 1. Create watch_minutes column
df['watch_minutes'] = df['sessions'] * df['avg_session_min']

print("--- 1. Dataset with Total Watch Minutes ---")
print(df[['user_id', 'content_type', 'sessions', 'avg_session_min', 'watch_minutes']].head())
print()


# 2. Compare content types using total watch minutes, average completion rate, and average sessions
content_comparison = df.groupby('content_type').agg(
    total_watch_minutes=('watch_minutes', 'sum'),
    avg_completion_rate=('completion_rate', 'mean'),
    avg_sessions=('sessions', 'mean')
).reset_index()

print("--- 2. Content Type Comparison ---")
print(content_comparison.to_string(index=False))
print()


# 3. Create engagement category based on total watch minutes
df['engagement_category'] = pd.qcut(
    df['watch_minutes'], 
    q=3, 
    labels=['Low Engagement', 'Moderate Engagement', 'High Engagement']
)
category_counts = df['engagement_category'].value_counts()

print("--- 3. Engagement Category Distribution ---")
print(category_counts)
print()


# 4. Analyze relationship between sessions and watch minutes using correlation
correlation = df['sessions'].corr(df['watch_minutes'])
print(f"--- 4. Correlation Analysis ---")
print(f"Correlation between number of sessions and total watch minutes: {correlation:.4f}\n")

# Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, 
    x='sessions', 
    y='watch_minutes', 
    hue='content_type', 
    palette='Set2', 
    s=120, 
    edgecolor='black'
)
plt.title('Relationship Between Sessions and Total Watch Minutes', fontsize=12, fontweight='bold')
plt.xlabel('Number of Sessions', fontsize=10)
plt.ylabel('Total Watch Minutes', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Content Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# 5. Identify valuable content type based on multi-metric analysis
print("--- 5. Content Type Value Conclusion ---")
print("Evaluating Series and Sports across metrics:")
print("- Series drives high session volume and total watch time due to episodic repetition.")
print("- Documentaries show high completion rates, but lower total volume.")
print("- Movies command high average session duration and strong completion rates.")
print("Conclusion: 'Series' appears most valuable for sustained platform engagement, "
      "balancing high session counts and strong aggregate watch time.")