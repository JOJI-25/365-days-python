import pandas as pd
import numpy as np

# Initial DataFrame
customers = pd.DataFrame({
    "customer_id": [
        "C001", "C002", "C003", "C004", "C005",
        "C003", "C006", "C007", "C008", "C009"
    ],
    "name": [
        " Rahul Kumar ", "ANITA JOSEPH", "john mathew",
        " Meera Nair", "ARUN P",
        "john mathew", "SNEHA MENON", "Vivek Rao ",
        "PRIYA DAS", "  Rohan Singh"
    ],
    "city": [
        "kochi", "BENGALURU", "Kochi ", "Kochi",
        "Bengaluru", "kochi ", None, "CHENNAI",
        "chennai", "Bengaluru "
    ],
    "age": [
        24, 31, None, 28, 42,
        None, 26, 35, 29, 31
    ],
    "gender": [
        "M", "Female", "male", "F", "Male",
        "M", "female", "M", "Female", None
    ],
    "annual_spend": [
        45000, 72000, 38000, None, 91000,
        38000, 52000, 68000, 59000, 81000
    ]
})

# 1. Count missing values before cleaning
missing_before = customers.isnull().sum().sum()

# 2. Handle Duplicates
# C003 appears twice with identical values. We drop exact duplicates based on customer_id and all attributes.
duplicates_before = customers.duplicated().sum()
cleaned_df = customers.drop_duplicates().copy()
duplicates_removed = duplicates_before

# 3. Standardise Text Columns
cleaned_df["name"] = cleaned_df["name"].str.strip().str.title()
cleaned_df["city"] = cleaned_df["city"].str.strip().str.title()

# 4. Standardise Gender Column
gender_mapping = {
    "M": "Male", "m": "Male", "male": "Male", "Male": "Male",
    "F": "Female", "f": "Female", "female": "Female", "Female": "Female"
}
cleaned_df["gender"] = cleaned_df["gender"].map(gender_mapping)

# 5. Handle Missing Values (Data-Driven Strategies)
# --- Age: Impute with the median age ---
# Justification: Median is robust against outliers compared to the mean.
median_age = cleaned_df["age"].median()
cleaned_df["age"] = cleaned_df["age"].fillna(median_age)

# --- City: Impute with the mode (most frequent city) ---
# Justification: Since city has categorical text, filling with the most common value ("Kochi" or "Bengaluru") maintains distribution balance without introducing arbitrary text.
mode_city = cleaned_df["city"].mode()[0]
cleaned_df["city"] = cleaned_df["city"].fillna(mode_city)

# --- Annual Spend: Impute with the median annual spend ---
# Justification: Spending data can be skewed by high-value customers; median provides a realistic central benchmark.
median_spend = cleaned_df["annual_spend"].median()
cleaned_df["annual_spend"] = cleaned_df["annual_spend"].fillna(median_spend)

# 6. Create New Features
# --- Age Group ---
# Thresholds: Young Adult (18-30), Middle-Aged (31-45), Senior (46+)
def categorize_age(age):
    if age <= 30:
        return "Young Adult"
    elif age <= 45:
        return "Middle-Aged"
    else:
        return "Senior"

cleaned_df["age_group"] = cleaned_df["age"].apply(categorize_age)

# --- Customer Value ---
# Thresholds: Low (< 50,000), Medium (50,000 - 75,000), High (> 75,000)
# Justification: Based on standard spending distribution tiers in retail analytics.
def categorize_spend(spend):
    if spend < 50000:
        return "Low"
    elif spend <= 75000:
        return "Medium"
    else:
        return "High"

cleaned_df["customer_value"] = cleaned_df["annual_spend"].apply(categorize_spend)

# Count missing values after cleaning
missing_after = cleaned_df.isnull().sum().sum()

# --- PRINT REPORTS ---
print("=" * 50)
print("DATA CLEANING REPORT")
print("=" * 50)
print(f"Missing values before cleaning: {missing_before}")
print(f"Missing values after cleaning: {missing_after}")
print(f"Duplicate records removed: {duplicates_removed}")
print("\nFinal Cleaned DataFrame:")
print(cleaned_df.to_string(index=False))
print("=" * 50)