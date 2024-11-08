# -*- coding: utf-8 -*-
"""project1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UxVHckaDJRRH0dysT7pFOGLo2Y6n3pE9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
data=pd.read_csv("dailyActivity_merged.csv")
print(data.head())

print(data.info())

data["ActivityDate"] = pd.to_datetime(data["ActivityDate"],format="%m/%d/%Y")
print(data.info())

data["TotalMinutes"] = data["VeryActiveMinutes"] + data ["FairlyActiveMinutes"] + data["LightlyActiveMinutes"] + data["SedentaryMinutes"]
print(data["TotalMinutes"].sample(5))

print(data.describe())

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,6))
sns.barplot(x=data['ActivityDate'], y=data['TotalSteps'], color='blue')


plt.title('Total Steps per Day', fontsize=14)
plt.show()

import matplotlib.pyplot as plt
activity_minutes = {
    'Very Active Minutes': data['VeryActiveMinutes'].sum(),
    'Fairly Active Minutes': data['FairlyActiveMinutes'].sum(),
    'Lightly Active Minutes': data['LightlyActiveMinutes'].sum(),
    'Sedentary Minutes': data['SedentaryMinutes'].sum()
}
activity_distances = {
    'Very Active Distance': data['VeryActiveDistance'].sum(),
    'Moderately Active Distance': data['ModeratelyActiveDistance'].sum(),
    'Light Active Distance': data['LightActiveDistance'].sum(),
    'Sedentary Active Distance': data['SedentaryActiveDistance'].sum()
}
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
ax1.pie(activity_minutes.values(), labels=activity_minutes.keys(), autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
ax1.set_title('Activity Minutes Distribution')
ax2.pie(activity_distances.values(), labels=activity_distances.keys(), autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
ax2.set_title('Activity Distances Distribution')
plt.tight_layout()
plt.show()

labels = list(activity_minutes.keys())
minutes = list(activity_minutes.values())
distances = list(activity_distances.values())

x = np.arange(len(labels))  # label locations
width = 0.35  # width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, minutes, width, label='Minutes', color='#66b3ff')
rects2 = ax.bar(x + width/2, distances, width, label='Distances', color='#ff9999')

ax.set_xlabel('Activity Type')
ax.set_title('Activity Minutes and Distances')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(activity_minutes.values(), activity_distances.values(), color='#66b3ff')
plt.title('Activity Minutes vs Distances')
plt.xlabel('Total Activity Minutes')
plt.ylabel('Total Activity Distances')
plt.grid(True)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
data = pd.read_csv('dailyActivity_merged.csv')

# Select relevant columns for the heatmap
heatmap_data = data[['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes',
                     'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance', 'SedentaryActiveDistance',
                     'TotalSteps', 'Calories']]

# Generate the correlation matrix
corr_matrix = heatmap_data.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Activity Metrics')
plt.show()

import matplotlib.pyplot as plt

# Creating a bar plot for TotalSteps vs. Calories
plt.figure(figsize=(10, 6))
plt.bar(data['TotalSteps'], data['Calories'], color='blue', alpha=0.7)
plt.xlabel('Total Steps')
plt.ylabel('Calories Burned')
plt.title('Bar Plot between Total Steps and Calories Burned')
plt.show()

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('dailyActivity_merged.csv')

# Define the target variable
# For this example, we'll create a new column 'HighlyActive'
# If 'VeryActiveMinutes' > 30, label as 1 (Highly Active), else 0 (Not Highly Active)
data['HighlyActive'] = data['VeryActiveMinutes'].apply(lambda x: 1 if x > 30 else 0)

# Select features for the model
features = ['TotalSteps', 'TotalDistance', 'Calories', 'FairlyActiveMinutes', 'LightlyActiveMinutes']

X = data[features]    # Feature variables
y = data['HighlyActive']  # Target variable

# Split the dataset into training and testing sets using the split method
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Convert accuracy to percentage
accuracy_percentage = accuracy * 100

# Print the accuracy in percentage
print(f"Accuracy: {accuracy_percentage:.2f}%")

# Split the dataset into two parts based on Calories burned
# One part with Calories <= 2000, and another with Calories > 2000

low_calories_data = data[data['Calories'] <= 2000]
high_calories_data = data[data['Calories'] > 2000]

# Display formatted output
print("### 1. Low Calories Data (Calories <= 2000):")
print(low_calories_data.head())  # Display the first few entries of low calorie data

print("\n### 2. High Calories Data (Calories > 2000):")
print(high_calories_data.head())  # Display the first few entries of high calorie data

# Sort the dataset by 'TotalSteps' in ascending order

sorted_data = data.sort_values(by='TotalSteps', ascending=True)

# Display formatted output
print("\n### 3. Dataset sorted by TotalSteps:")
print(sorted_data.head())  # Display the first few sorted entries by total steps

import pandas as pd
data = pd.read_csv("dailyActivity_merged.csv")
print(data.head(10))

print(data.isnull().sum())

figure=px.scatter(data_frame=data,x="Calories",y="TotalSteps",size="VeryActiveMinutes",trendline="ols",title="Relationship between Calories and Total Steps")
figure.show()

label = ["Very Active Minutes", "Fairly Active Minutes",
         "Lightly Active Minutes", "Inactive Minutes"]
counts = data[["VeryActiveMinutes", "FairlyActiveMinutes",
               "LightlyActiveMinutes", "SedentaryMinutes"]].mean()
colors = ['gold','lightgreen', "pink", "blue"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Total Active Minutes')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

data["Day"] = data["ActivityDate"].dt.day_name()
print(data["Day"].head())

# Append new rows to the dataset
# Creating a new DataFrame for demonstration purposes (representing new daily activity data)

new_data = pd.DataFrame({
    'VeryActiveMinutes': [50, 45],
    'FairlyActiveMinutes': [20, 30],
    'LightlyActiveMinutes': [200, 180],
    'SedentaryMinutes': [600, 550],
    'Calories': [2500, 2200],
    'TotalSteps': [15000, 13000],
    'VeryActiveDistance': [5.0, 4.5],
    'ModeratelyActiveDistance': [3.0, 2.8],
    'LightActiveDistance': [8.0, 7.5],
    'SedentaryActiveDistance': [0.5, 0.4],
    'ActivityDate': ['2023-09-26', '2023-09-27']
})

# Append new data to the existing dataset
updated_dataset = pd.concat([dataset, new_data], ignore_index=True)

# Display formatted output
print("\n### 4. Dataset after appending new rows:")
print(updated_dataset.tail())  # Display the last few entries after appending the new data

fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["VeryActiveMinutes"],
    name='Very Active',
    marker_color='purple'
))
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["FairlyActiveMinutes"],
    name='Fairly Active',
    marker_color='green'
))
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["LightlyActiveMinutes"],
    name='Lightly Active',
    marker_color='pink'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()

day = data["Day"].value_counts()
label = day.index
counts = data["SedentaryMinutes"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Inactive Minutes Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

calories = data["Day"].value_counts()
label = calories.index
counts = data["Calories"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Calories Burned Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

# Importing necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file
data = pd.read_csv("dailyActivity_merged.csv")

# Extracting the features (TotalSteps) and target (Calories)
X = data["TotalSteps"].values.reshape(-1, 1)  # TotalSteps as feature
y = data["Calories"].values                   # Calories as target

# Creating the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predicting calories based on total steps
y_pred = model.predict(X)

# Displaying a few predicted values alongside the actual values
predicted_vs_actual = pd.DataFrame({'TotalSteps': X.flatten(), 'Actual Calories': y, 'Predicted Calories': y_pred})
print(predicted_vs_actual)

# Importing necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("dailyActivity_merged.csv")

# Extracting the features (TotalSteps) and target (Calories)
X = data["TotalSteps"].values.reshape(-1, 1)  # TotalSteps as feature
y = data["Calories"].values                   # Calories as target

# Creating the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predicting calories based on total steps
y_pred = model.predict(X)

# Plotting the scatter plot and regression line using matplotlib
plt.scatter(X, y, color="blue", label="Observed data")
plt.plot(X, y_pred, color="red", label="Regression line")
plt.title("Linear Regression: Calories vs. Total Steps")
plt.xlabel("Total Steps")
plt.ylabel("Calories")
plt.legend()
plt.show()