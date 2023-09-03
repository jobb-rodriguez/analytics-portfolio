# Automobile Price Prediction using Multivariate Linear Regression
# Conclusion
Based on the thetas, the learning rate, and the optimized cost, ```Car Perform with Curb Weight vs Price``` performs the best.

[Read the full report](/projects/automobile-price-prediction/Report%20-%Automobile%20Price%20Prediction.pdf).

# Dataset
The Automobile dataset came from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/10/automobile). [Access the file](/projects/automobile-price-prediction/car.csv).

# Data Preprocessing
In preparing the data for analysis, I perform the following preprocessing techniques with ```pandas``` (as seen [here](/projects/automobile-price-prediction/preprocessing.py)):
1. Categorical to Numerical Conversion
2. Drop Unused Columns
3. Add Columns: ```Volume```, ```Width ^ 2```, ```Length ^ 2```
4. Normalize the Data

[View the preprocessed data](/projects/automobile-price-prediction/cars_preprocessed.csv).

# Analysis
With the available features and engineered features, I conducted Multivariate Linear Regression for comparison with ```numpy``` and plotted the results with ```matplotlib``` and ```seaborn```.

You can see me exploring the data in [Jupyter Notebooks](/projects/automobile-price-prediction/cars.ipynb) and conductiny my analysis in this [Python file](/projects/automobile-price-prediction/analysis.py).