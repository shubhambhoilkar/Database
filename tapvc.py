import pandas as pd
from scipy.stats import f_oneway

# Assuming 'data' is your DataFrame containing relevant columns including 'BSA' and 'Type of TAPVC'
file_path = 'C:\\Users\\HP\\sam project files\\SAM\\Data Analysis\\tapvcbook.xlsx'
data = pd.read_excel(file_path)


# Clean the data
data['BSA'] = pd.to_numeric(data['BSA'], errors='coerce')
data = data.dropna()

# Separate the data into groups based on 'Type of TAPVC'
supra = data[data['Type of TAPVC'] == 'Supracardiac']['BSA']
infra = data[data['Type of TAPVC'] == 'Infracardiac']['BSA']
cardiac = data[data['Type of TAPVC'] == 'Cardiac']['BSA']
mix = data[data['Type of TAPVC'] == 'Mixed']['BSA']

# Perform one-way ANOVA
f_stat, p_val = f_oneway(supra, infra, cardiac, mix)

print(f"F-statistic: {f_stat:.2f}")
print(f"P-value: {p_val:.4f}")

if p_val < 0.05:
    print("There is a significant difference between at least one pair of groups.")
else:
    print("No significant difference found between the groups.")
