# qb_pass_distribution.py

# 1. Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nfl_data_py as nfl

# 2. Load data
print("Downloading 2024 play-by-play data... (may take a minute)")
pbp = nfl.import_pbp_data(years=[2024])
print("Data loaded!")

# 3. Filter for QB passing plays
qb_passes = pbp[pbp['pass_attempt'] == 1]

# 4. Aggregate passing yards by QB (use 'yards_gained' instead of 'pass_yds')
qb_summary = qb_passes.groupby('passer_player_name', as_index=False).agg({
    'yards_gained': 'sum',
    'pass_attempt': 'count'
})
qb_summary = qb_summary.rename(columns={
    'yards_gained': 'total_passing_yards',
    'pass_attempt': 'total_attempts'
})

# 5. Filter for QBs with a minimum number of attempts
min_attempts = 300
qb_summary = qb_summary[qb_summary['total_attempts'] >= min_attempts]

# 6. Histogram of passing yards
plt.figure(figsize=(12,6))
sns.histplot(qb_summary['total_passing_yards'], bins=20, kde=True, color='blue', edgecolor='black')
plt.title('Distribution of Total Passing Yards by QBs — 2024 Season (300+ Attempts)')
plt.xlabel('Total Passing Yards')
plt.ylabel('Number of QBs')
plt.grid(True)
plt.show()

# 7. Summary statistics
mean_yards = qb_summary['total_passing_yards'].mean()
median_yards = qb_summary['total_passing_yards'].median()
max_yards = qb_summary['total_passing_yards'].max()

print(f"Mean passing yards: {mean_yards:.0f}")
print(f"Median passing yards: {median_yards:.0f}")
print(f"Highest passing yards by a QB: {max_yards:.0f}")

# 8. Box plot
plt.figure(figsize=(8,4))
sns.boxplot(x=qb_summary['total_passing_yards'], color='lightgreen')
plt.title('Box Plot: Total Passing Yards by QBs — 2024 Season (300+ Attempts)')
plt.xlabel('Total Passing Yards')
plt.show()

# 9. Top 10 QBs by Total Passing Yards
top_qbs = qb_summary.sort_values(by='total_passing_yards', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(
    data=top_qbs,
    x='total_passing_yards',
    y='passer_player_name',
    hue='passer_player_name',
    dodge=False,
    palette='Blues_r',
    legend=False
)
plt.title('Top 10 Quarterbacks by Total Passing Yards — 2024 Season')
plt.xlabel('Total Passing Yards')
plt.ylabel('Quarterback')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()