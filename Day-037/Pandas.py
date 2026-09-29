import pandas as pd

data = {    
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],    
    "course": [        "Python", "Python", "SQL", "SQL", "Power BI",        "Power BI", "Python", "SQL", "Power BI", "Python"    ],    
    "lessons_completed": [18, 7, 15, 4, 20, 9, 12, 17, 6, 21],    
    "total_lessons": [20, 20, 20, 20, 25, 25, 20, 20, 25, 20],    
    "quiz_score": [92, 58, 81, 45, 88, 62, 74, 90, 51, 95],    
    "hours_week": [7.5, 2.0, 5.5, 1.5, 8.0, 3.0, 4.5, 6.5, 2.5, 9.0]
}
df = pd.DataFrame(data)

# 1. New completion_rate column
df['completion_rate'] = (df['lessons_completed'] / df['total_lessons']) * 100

# 2. Average completion rate, quiz score, and weekly study hours for each course
course_summary = df.groupby('course')[['completion_rate', 'quiz_score', 'hours_week']].mean()

# 3. Identify students who have both a completion rate below 50% and a quiz score below 60
struggling_students = df[(df['completion_rate'] < 50) & (df['quiz_score'] < 60)]

# 4. engagement_level column
def get_engagement(hours):
    if hours < 3:
        return "Low"
    elif 3 <= hours <= 6:
        return "Medium"
    else:
        return "High"

df['engagement_level'] = df['hours_week'].apply(get_engagement)

# 5. Determine which course appears to have the greatest student engagement
# Let's check average hours_week and average completion_rate or high/medium engagement counts per course
course_engagement = df.groupby('course').agg({
    'hours_week': 'mean',
    'completion_rate': 'mean',
    'quiz_score': 'mean'
}).reset_index()

print("--- Course Summary ---")
print(course_summary)
print("\n--- Struggling Students ---")
print(struggling_students[['student_id', 'course', 'completion_rate', 'quiz_score']])
print("\n--- Full DF with Engagement ---")
print(df[['student_id', 'course', 'completion_rate', 'hours_week', 'engagement_level']])