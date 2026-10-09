import numpy as np

yield_data = np.array([
    [4.8, 5.1, 4.9, 5.3],
    [3.9, 4.4, 4.1, 4.6],
    [5.7, 5.9, 6.2, 6.0],
    [4.2, 3.8, 4.5, 4.0],
    [5.0, 5.2, 4.7, 5.5]
])
plots = np.array(["Plot_A", "Plot_B", "Plot_C", "Plot_D", "Plot_E"])

# ---------------------------------------------------------
# Task 1: Mean yield for each plot and rank from highest to lowest
# ---------------------------------------------------------
mean_yields = np.mean(yield_data, axis=1)
rank_indices = np.argsort(mean_yields)[::-1]
ranked_plots = plots[rank_indices]
ranked_means = mean_yields[rank_indices]

print("=== TASK 1: Mean Yields & Ranking (Highest to Lowest) ===")
for plot, mean in zip(ranked_plots, ranked_means):
    print(f"{plot}: {mean:.2f} tonnes/hectare")


# ---------------------------------------------------------
# Task 2: Total yield across all plots for each season & highest season
# ---------------------------------------------------------
season_totals = np.sum(yield_data, axis=0)
best_season_idx = np.argmax(season_totals)

print("\n=== TASK 2: Total Yield per Season ===")
for i, total in enumerate(season_totals, 1):
    print(f"Season {i}: {total:.2f} tonnes")
print(f"-> Season with Highest Overall Production: Season {best_season_idx + 1} ({season_totals[best_season_idx]:.2f} tonnes)")


# ---------------------------------------------------------
# Task 3: Percentage contribution of each plot to total production
# ---------------------------------------------------------
total_production = np.sum(yield_data)
plot_totals = np.sum(yield_data, axis=1)
plot_percentages = (plot_totals / total_production) * 100

print("\n=== TASK 3: Percentage Contribution of Each Plot ===")
for plot, pct in zip(plots, plot_percentages):
    print(f"{plot}: {pct:.2f}%")


# ---------------------------------------------------------
# Task 4: Coefficient of Variation (CV) & most variable plot
# ---------------------------------------------------------
plot_stds = np.std(yield_data, axis=1)
cvs = (plot_stds / mean_yields) * 100
most_variable_idx = np.argmax(cvs)
most_variable_plot = plots[most_variable_idx]

print("\n=== TASK 4: Coefficient of Variation (CV) ===")
for plot, cv in zip(plots, cvs):
    print(f"{plot}: {cv:.2f}%")
print(f"-> Most Variable Plot: {most_variable_plot}")


# ---------------------------------------------------------
# Task 5: NumPy broadcasting for deviations & largest positive deviation
# ---------------------------------------------------------
# Reshape mean_yields from (5,) to (5, 1) for broadcasting across seasons (5, 4)
deviations = yield_data - mean_yields[:, np.newaxis]
max_positive_deviation = np.max(deviations)
max_dev_pos = np.unravel_index(np.argmax(deviations), deviations.shape)
max_dev_plot = plots[max_dev_pos[0]]
max_dev_season = max_dev_pos[1] + 1

print("\n=== TASK 5: Deviations from Plot Mean (Broadcasting) ===")
print(deviations)
print(f"\n-> Largest Positive Deviation: {max_positive_deviation:.2f} (Found in {max_dev_plot}, Season {max_dev_season})")