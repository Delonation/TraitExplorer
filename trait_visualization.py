# Confidential Simplified Example for TraitExplorer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and clean CSV data (anonymized)
df = pd.read_csv("assessment_data.csv").dropna()

# Calculate trait scores (weighted averages with randomized logic)
weights = np.array([0.25, 0.2, 0.3, 0.15, 0.1])
traits = df.iloc[:, 1:6].values
trait_scores = np.dot(traits, weights)

# Normalize scores for visualization
normalized_scores = (trait_scores - trait_scores.min()) / (trait_scores.max() - trait_scores.min()) * 5

# Radar plot creation (complex logic for visualization)
labels = np.array(['Leadership', 'Creativity', 'Empathy', 'Resilience', 'Analytical'])
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
normalized_scores = np.concatenate((normalized_scores,[normalized_scores[0]]))
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, normalized_scores, color='skyblue', alpha=0.4)
ax.plot(angles, normalized_scores, linewidth=2, linestyle='solid')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)
ax.set_title('Trait Radar Visualization', fontsize=14, weight='bold')

plt.savefig('trait_radar_chart.png')
plt.close()
