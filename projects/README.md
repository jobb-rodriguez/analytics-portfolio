# Excel
## Bike Purchased Bikes Dashboard (Excel, Docs, Canva, and Video)
Big Idea: Most of our buying customers were from North America commuting 2-5 miles and Europe commuting 0-1 miles. Splitting the ad budget into 60-40 can generate the most ROI. Utilize 60% targeting Middle Aged North Americans with our 2-5 miles bike. Utilize the remaining 40% targeting Middle Aged Europeans with our 0-1 miles bike.

*Situation:* Clement runs an E-commerce Bike Shop. He wants to know which type of customers he should target for 2023 Q3.
1. Clement never saw the dataset for his customers. So he wants to have a general idea about them.
2. He also wants to know if income, gender, marital status, and commute distance plays a role in their purchasing decision.
3. He's also considering on which region to allocate his budget.

*Outputs:*
- Access the [Dashboard](mini-projects/clements-bicycle-shop/dashboard.xlsx).
- Read the [Written Report](https://docs.google.com/document/d/1Jt_MA0C9CYMIhHo5qRfUhrTnlRa0J7IlkEQw_tAt73Y/edit?usp=sharing).
- View the [Proposed Target Customer Presentation](https://www.canva.com/design/DAFtJLKNhn4/6ZCH_dvPXDsbjx50yhDPKA/view?utm_content=DAFtJLKNhn4&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink). [Watch me explain it](https://youtu.be/QlKbsO8kktE).

# Tableau
## Airbnb Dashboard (Tableau Public, Docs, Canva, and Video)
Big Idea: Zipcode 98134 is the best place to start an Airbnb in Seattle. Airbnb with 2 bedrooms can sell for $175.4 per night and has a lower competition compared to single bedrooms. The best time to list list an Airbnb are during May to July and October to December.

*Situation:* Andrew wants to identify the best place to start an Airbnb in Seattle.
1. He wants to know the factors he should consider.
2. He's also curious on how much he can charge.
3. He wants to know the best time to rent his Airbnb.

*Outputs:*
- Access the [Dashboard](https://public.tableau.com/app/profile/jobb.rodriguez/viz/AirbnbDashboard2016_16935822119980/Dashboard1?publish=yes).
- Read the [Written Report](https://docs.google.com/document/d/1m2f0-wNG9LJoY_nMCcYIRhvQF6bFrSBs9kWn5xxRwaE/edit?usp=sharing).

# SQL
## Covid Data (PostgreSQL)
I conducted Data Exploration to help people have a general idea about the state of the world during Covid.

[Read more here](/projects/covid/).

**Skills Used:**
1. Importing Data into PostgreSQL
2. Descriptive Statistics
3. Window Functions and Aggregate Functions
4. Type Conversion
5. Joins
6. CTE's and Temp Tables
7. Export CSV ([Access the exported CSV](/projects/covid/covid_percentpopulationvaccinated.csv))

## Nashville Housing (PostgreSQL)
I conducted Data Cleaning to ready the data for exploration and analysis in Excel, Python, and Tableau.

[Read more here](/projects/nashville-housing/).

**Skills Used:**
1. Importing Data into PostgreSQL
2. Populating Missing Data
3. Splitting Data
4. Removing Duplicates
5. Dropping Columns
6. Export CSV ([Access the exported CSV](/projects/nashville-housing/nashville_housing_cleaned.csv))

# Python
## Housing Price Prediction using Linear Regression with One Feature (Numpy, Matplotlib)
**Abstract**

In this analysis, I used ```Linear Regression``` with One Feature to identify the best feature to predict the house price. From the available features (Transaction Date, House Age, Distance to the nearest MRT station, Number of Convenience Stores, Latitude, and Longitude), 

```Number of Convenience Stores``` is the best feature to use in predicting house price. The optimized cost was ```62.236```, (0, 0) as values of the initial thetas and 0 as value of the learning rate. The scatterplot is close to the feature’s optimized regression line.

- [Read the Report](/projects/housing-price-prediction/Report%20-%20Housing%20Price%20Prediction.pdf) 
- [Access the Dataset](https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction)
- [Access the Folder](/projects/housing-price-prediction/) 

## Automobile Price Prediction using Multivariate Linear Regression (Pandas, Numpy, Matplotlib, Seaborn)
**Abstract**

In this analysis, I used ```Multivariate Linear Regression``` to identify which experiment performs best in predicting the price
given the dataset, [Automobile Dataset](https://archive.ics.uci.edu/dataset/10/automobile). All sets of features. However, in terms of the optimized cost, the thetas, and the learning rate, ```Car Performance with Curb Weight vs Price``` performed best.

- [Read the Report](/projects/automobile-price-prediction/Report%20-%20Automobile%20Price%20Prediction.pdf) 
- [Access the Folder](/projects/automobile-price-prediction/) 

## Cardiovascular Disease using Multi-layer Perceptron Classifier and Logistic Regression (Pandas, Numpy, Scikit-learn)
**Abstract**

In this analysis, I used ```Multi-layer Perceptron classifier (MPC)``` and ```Logistic Regression (LR)``` to identify which configuration of MPC performs best and identify if LR outperforms MPC in predicting the cardiovascular disease given the dataset, [Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset). Moreover, I aimed to identify if the ```Body Mass Index (BMI)``` can improve the performance of the models. 

The MPC model, without BMI, with the default configuration performed the best with an average test accuracy score of 73.39%. The MPC model, with BMI, with the default configuration performed the best with an average test accuracy score of 73.36%. Without BMI, the MPC’s
average test accuracy score was 1.36% higher than LR. With BMI, the MPC’s average test accuracy score was 1.33% higher than LR. The BMI does not improve the models’ performances.

- [Read the Report](/projects/cardiovascular-disease-prediction/Report%20-%20Cardiovascular%20Disease%20Prediction.pdf) 
- [Access the Folder](/projects/cardiovascular-disease-prediction/) 