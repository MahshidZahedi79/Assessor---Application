import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Scientific Setup for Reproducibility
np.random.seed(42) # Ensures the same random numbers are generated every time
num_users = 30     # Sample size of 30 users

# 2. Generating Apps' version1 Data
# Pain points: Nested folders, slow information access, no internal chat
old_data = pd.DataFrame({
    'Version': 'version1',
    'Time_on_Task': np.random.normal(30, 5, num_users),      # Mean: 30 minutes, Std Dev: 5
    'Nav_Steps': np.random.poisson(9, num_users),           # Mean: 9 clicks due to nested architecture
    'Comm_Attempts': np.random.poisson(5, num_users),       # Mean: 5 phone calls needed for support
    'SUS_Score': np.random.normal(52, 8, num_users)         # Mean Satisfaction: 52 (Marginal/Poor)
})

# 3. Generating Redesign Data (New Version)
# Solutions: Optimized information architecture, integrated internal chat
new_data = pd.DataFrame({
    'Version': 'version2',
    'Time_on_Task': np.random.normal(15, 2, num_users),      # Mean: 15 minutes (50% faster)
    'Nav_Steps': np.random.poisson(3, num_users),           # Mean: 3 clicks (Simplified IA)
    'Comm_Attempts': np.random.poisson(1, num_users),       # Mean: 1 quick chat message for support
    'SUS_Score': np.random.normal(82, 5, num_users)         # Mean Satisfaction: 82 (Excellent)
})

# 4. Merge datasets into a single DataFrame for comparison
df = pd.concat([old_data, new_data])

# 5. Visualization: Creating the Performance Dashboard
plt.style.use('ggplot') # Using a clean, professional graphical style
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Chart 1: Efficiency - Time on Task
sns.barplot(ax=axes[0,0], x='Version', y='Time_on_Task', data=df, palette='Reds_r')
axes[0,0].set_title('Efficiency: Time on Task (Minutes)')
axes[0,0].set_ylabel('Avg. Minutes')

# Chart 2: Navigation Depth - Validating the fix for "Nested Folders"
sns.barplot(ax=axes[0,1], x='Version', y='Nav_Steps', data=df, palette='Blues_r')
axes[0,1].set_title('Navigation Depth: Number of Clicks')
axes[0,1].set_ylabel('Avg. Clicks')

# Chart 3: Communication Friction - Impact of the Internal Chat feature
sns.barplot(ax=axes[1,0], x='Version', y='Comm_Attempts', data=df, palette='Oranges_r')
axes[1,0].set_title('Comm. Friction: Phone Calls vs. Chat Messages')
axes[1,0].set_ylabel('Avg. Attempts')

# Chart 4: User Satisfaction - System Usability Scale (SUS)
sns.barplot(ax=axes[1,1], x='Version', y='SUS_Score', data=df, palette='Greens_r')
axes[1,1].axhline(68, color='red', linestyle='--', label='Industry Avg (68)') # SUS Benchmark
axes[1,1].set_title('User Satisfaction: SUS Score (0-100)')
axes[1,1].set_ylabel('Mean Score')
axes[1,1].legend()

# Final Polish and Layout adjustment
plt.tight_layout()
plt.show()

