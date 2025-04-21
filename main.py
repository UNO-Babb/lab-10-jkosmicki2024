#MapPlot.py
#Name: Jacob Kosmicki
#Date:
#Assignment:

import coffee
import pandas as pd
import matplotlib.pyplot as plt

# Retrieve coffee data
coffee_data = coffee.get_coffee()

years = []
scores = []

# Extract relevant data
for entry in coffee_data:
    year = entry["Year"]
    score = entry["Data"]["Scores"]["Total"]
    if score != 0:
        years.append(year)
        scores.append(score)

# Create DataFrame
df = pd.DataFrame({"Year": years, "Score": scores})

# Display DataFrame
print(df)

# Generate scatter plot
df.plot(kind='scatter', x='Year', y='Score')

# Save the plot
plt.savefig("output.png")
