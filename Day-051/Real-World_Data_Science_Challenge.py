import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    accuracy_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# 1. Dataset Construction (36 Support Tickets across 4 Priority Levels)
descriptions_36 = [
    # Critical
    "Production checkout is unavailable for all customers",
    "Cannot log in to any company account",
    "Payment processing has stopped completely",
    "Customer records are disappearing after saving",
    "Our entire website returns server errors",
    "Security alert reports unauthorised account access",
    "Payroll export is failing before today's deadline",
    "All users receive an error when opening the dashboard",
    "Database connection timeout affecting all API requests",
    "Critical vulnerability discovered in authentication module",
    # High
    "Order confirmations are not being generated",
    "Monthly sales report contains incorrect totals",
    "Invoice export fails for one department",
    "Inventory numbers are delayed by several hours",
    "Search results are missing recently added products",
    "A scheduled report did not run this morning",
    "User authentication token expires prematurely",
    "Webhooks failing to deliver event payloads",
    "Payment gateway returning intermittent 500 errors",
    # Medium
    "Customer profile updates are not appearing immediately",
    "Several invoices show incorrect tax calculations",
    "The dashboard loads slowly during busy periods",
    "Some orders are missing tracking information",
    "Email notifications are delayed for certain users",
    "Product images fail to load on some pages",
    "A data import completed with several rejected rows",
    "The weekly summary contains duplicate entries",
    "Export button unclickable in Firefox browser",
    # Low
    "How can I change my profile picture",
    "Where can I find the user manual",
    "Please explain how to reset my password",
    "How do I update my notification preferences",
    "I need instructions for downloading a report",
    "Can you explain the subscription renewal process",
    "What are the supported image formats for uploads",
    "How do I invite a team member to workspace",
]

priorities = (
    ["Critical"] * 10
    + ["High"] * 9
    + ["Medium"] * 9
    + ["Low"] * 8
)

tickets = pd.DataFrame({
    "ticket_id": range(9001, 9001 + len(descriptions_36)),
    "description": descriptions_36,
    "priority": priorities,
})

print("--- 1. Priority Label Distribution ---")
print(tickets["priority"].value_counts(), "\n")

# 2. Scikit-Learn Pipeline with Stratified Train/Test Split
X = tickets["description"]
y = tickets["priority"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1, 2))),
    ("clf", LogisticRegression(random_state=42, max_iter=1000)),
])

model_pipeline.fit(X_train, y_train)
y_pred = model_pipeline.predict(X_test)

# 3. Model Evaluation
print("--- 3. Evaluation Metrics ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Macro-F1 Score: {f1_score(y_test, y_pred, average='macro'):.2f}\n")

print("Per-Class Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

labels_order = ["Critical", "High", "Medium", "Low"]
conf_matrix = confusion_matrix(y_test, y_pred, labels=labels_order)
print("Confusion Matrix (Rows: True, Columns: Predicted):")
print(pd.DataFrame(conf_matrix, index=labels_order, columns=labels_order))
print()

# 4. Error Inspection
test_results = pd.DataFrame({
    "description": X_test,
    "true_priority": y_test,
    "predicted_priority": y_pred,
})
misclassified = test_results[
    test_results["true_priority"] != test_results["predicted_priority"]
]
print(f"--- 4. Misclassified Tickets ({len(misclassified)}) ---")
print(misclassified.to_string(), "\n")

# 5. Deployment Recommendation Summary
print("--- 5. Deployment Strategy Recommendation ---")
print(
    "Implement a human-in-the-loop triage system where predictions serve as automated suggestions, "
    "with hard keyword-based safety overrides for critical security or outage alerts."
)