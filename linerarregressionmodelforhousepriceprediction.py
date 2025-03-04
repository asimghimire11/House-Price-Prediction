# -*- coding: utf-8 -*-
"""LinerarRegressionModelForHousePricePrediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J9ptBv1cSvio6OUCIkolMs_46Potte7n
"""

#import required modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset from CSV
df = pd.read_csv('housedata.csv')

# Exploratory Data Analysis (EDA)
print(df.head())

# Summary statistics of the dataset
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Exclude non-numeric columns before calculating the correlation matrix
numeric_df = df.select_dtypes(include=[float, int])
correlation_matrix: DataFrame = numeric_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Preprocessing: Selecting features and target variable
X = df[['GrLivArea', 'FullBath', 'Bedroom']]
y = df['SalePrice']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building the Linear Regression Model
model = LinearRegression()

# Fitting the model on the training data
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)

# Mean Squared Error and R-squared for model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Predictions and Visualization
# To visualize the predictions against actual prices, we'll use a scatter plot
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.show()

# We can also create a residual plot to check the model's performance
residuals = y_test - y_pred
plt.scatter(y_test, residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("Actual Prices")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

# Lastly, let's use the trained model to make predictions on new data and visualize the results
new_data = [[3100, 2, 3]]
predicted_price = model.predict(new_data)

print("Predicted Price:", predicted_price[0])