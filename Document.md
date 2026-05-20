1. Project Overview
This script simulates user performance data to validate the redesign of a vehicle assessor application. The goal was to solve efficiency issues caused by a nested information architecture and lack of internal communication tools.
2. Core Metrics (KPIs)
Time on Task (ToT): Measures efficiency (minutes).
Navigation Depth: Measures the number of clicks required to reach forms (addressing the "nested folder" issue).
Communication Friction: Measures the frequency of external support needed (addressing the new "Internal Chat" feature).
System Usability Scale (SUS): A 0-100 score measuring perceived satisfaction.
3. Code Breakdown
A. Foundations & Reproducibility
np.random.seed(42): Ensures that the generated "random" numbers remain consistent every time the script is run, meeting the scientific standard of reproducibility.
num_users = 30: Uses a sample size of 30, which is the academic threshold for statistical significance.
B. Statistical Modeling
Normal Distribution (np.random.normal): Used for Time and SUS Scores. It mimics human behavior where most users perform near the average, with a few outliers.
Poisson Distribution (np.random.poisson): Used for counting Clicks and Communication attempts. It is the scientific way to model discrete events.
C. Data Context (Legacy vs. Redesign)
Legacy App: Modeled with high Time (30m), high Navigation steps (9 clicks), and low Satisfaction (52 SUS).
Redesign: Modeled with optimized Time (15m), simplified Navigation (3 clicks), and high Satisfaction (82 SUS).
D. Data Visualization (The Dashboard)
plt.subplots(2, 2): Creates a 2x2 grid to show all four metrics simultaneously, allowing for a holistic comparison.
SUS Baseline (68): A red dashed line is drawn at 68. This is the industry-standard average; showing the redesign above this line proves a "Grade A" user experience.
