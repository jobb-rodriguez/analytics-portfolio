# Housing Price Prediction using Linear Regression with One Feature
# Conclusion
```Number of Convenience Stores vs Price``` had the lowest optimized cost with a relatively fair learning rate (in consideration of the other features). Moreover, the pair’s optimized regression line is the nearest to the scatterplot.

As a result, Number of Convenience Stores is the best feature to predict the House Price.

[Read the full report](/projects/housing-price-prediction/Report%20-%20Housing%20Price%20Prediction.pdf).

# Dataset
The Real Estate Price Prediction dataset came from [Kaggle](https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction). [Access the file](/projects/housing-price-prediction/realestate.csv).

# Analysis
Per feature available, I conducted Linear Regression for comparison with ```numpy``` and plotted the results with ```matplotlib``` as seen in [```lin_reg.py```](/projects/housing-price-prediction/lin_reg.py).
| Feature vs Price | File |
| --- | --- |
| Transaction Date | [```lin_reg_date.py```](/projects/housing-price-prediction/lin_reg_date.py) |
| House Age | [```lin_reg_age.py```](/projects/housing-price-prediction/lin_reg_age.py) |
| MRT Station | [```lin_reg_mrt.py```](/projects/housing-price-prediction/lin_reg_mrt.py) |
| Number of Convenience Stores | [```lin_reg_conv.py```](/projects/housing-price-prediction/lin_reg_conv.py) |
| Latitude | [```lin_reg_lat.py```](/projects/housing-price-prediction/lin_reg_lat.py) |
| Longitude | [```lin_reg_long.py```](/projects/housing-price-prediction/lin_reg_long.py) |