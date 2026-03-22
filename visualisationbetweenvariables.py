import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("penguins")

# Drop missing values
df = df.dropna()

# Scatter plot: Culmen Length vs Body Mass
plt.figure()
sns.scatterplot(x="bill_length_mm", y="body_mass_g", data=df)
plt.title("Culmen Length vs Body Mass")
plt.show()

# Scatter plot: Culmen Depth vs Body Mass
plt.figure()
sns.scatterplot(x="bill_depth_mm", y="body_mass_g", data=df)
plt.title("Culmen Depth vs Body Mass")
plt.show()

# Pair plot for all features
sns.pairplot(df)
plt.show()

# Sort values for area plot
df_sorted = df.sort_values(by="bill_length_mm")

# Area plot: Culmen Length vs Body Mass
plt.figure()
plt.fill_between(df_sorted["bill_length_mm"], df_sorted["body_mass_g"])
plt.xlabel("Culmen Length")
plt.ylabel("Body Mass")
plt.title("Area Graph: Culmen Length vs Body Mass")
plt.show()