import numpy as np

metrics = np.array([
    [0.82, 0.76, 0.79],
    [0.91, 0.88, 0.89],
    [0.74, 0.81, 0.77],
    [0.86, 0.83, 0.84],
    [0.79, 0.72, 0.75],
    [0.93, 0.90, 0.91]
])

def evaluate_metrics(metrics):
    # 1. Mean of each metric (Precision, Recall, F1) across all datasets
    means = np.mean(metrics, axis=0)
    
    # 2. Dataset index with the highest F1 score (Column index 2)
    best_f1_idx = np.argmax(metrics[:, 2])
    
    # 3. Dataset index with the largest absolute difference between Precision and Recall
    max_diff_idx = np.argmax(np.abs(metrics[:, 0] - metrics[:, 1]))
    
    # 4. Average of precision and recall for every dataset
    avg_prec_rec = np.mean(metrics[:, :2], axis=1)
    
    # 5. Datasets where Precision > 0.85 and Recall > 0.80
    high_perf_datasets = np.where((metrics[:, 0] > 0.85) & (metrics[:, 1] > 0.80))[0]
    
    # 6. Standard deviation of each metric across all datasets
    std_devs = np.std(metrics, axis=0)
    
    # 7. Metric that is most stable across datasets (lowest standard deviation)
    metric_names = ["Precision", "Recall", "F1 Score"]
    most_stable_idx = np.argmin(std_devs)
    most_stable_metric = metric_names[most_stable_idx]
    
    # 8. Improvement in F1 score between lowest and highest performing datasets
    f1_improvement = np.max(metrics[:, 2]) - np.min(metrics[:, 2])
    
    # 9. Determine whether the ranking by precision is the same as the ranking by F1 score
    precision_rank = np.argsort(metrics[:, 0])
    f1_rank = np.argsort(metrics[:, 2])
    same_ranking = np.array_equal(precision_rank, f1_rank)

    return {
        "means": means,
        "best_f1_dataset": best_f1_idx,
        "max_diff_dataset": max_diff_idx,
        "avg_prec_rec": avg_prec_rec,
        "high_perf_datasets": high_perf_datasets,
        "std_devs": std_devs,
        "most_stable_metric": most_stable_metric,
        "f1_improvement": f1_improvement,
        "same_ranking": same_ranking
    }

# Execute and print results
results = evaluate_metrics(metrics)

print("1. Mean of each metric (Precision, Recall, F1):", np.round(results["means"], 4))
print(f"2. Dataset with highest F1 score: Dataset {results['best_f1_dataset']}")
print(f"3. Dataset with largest Precision-Recall difference: Dataset {results['max_diff_dataset']}")
print("4. Average of Precision and Recall per dataset:", np.round(results["avg_prec_rec"], 4))
print(f"5. Datasets with Precision > 0.85 and Recall > 0.80: {list(results['high_perf_datasets'])}")
print("6. Standard deviation of each metric:", np.round(results["std_devs"], 4))
print(f"7. Most stable metric: {results['most_stable_metric']}")
print(f"8. F1 score improvement (max - min): {results['f1_improvement']:.2f}")
print(f"9. Is Precision ranking the same as F1 ranking? {results['same_ranking']}")