# Import
import pandas as pd

# Functions: Categorical to Numerical Conversion


def convertCarBody(data):
    if data == 'convertible':
        return 0
    elif data == 'hardtop':
        return 1
    elif data == 'hatchback':
        return 2
    elif data == 'sedan':
        return 3
    else:
        return 4


def convertDriveWheel(data):
    if data == 'fwd':
        return 0
    elif data == 'rwd':
        return 1
    else:
        return 2


def convertCylinderNumber(data):
    if data == 'two':
        return 0
    elif data == 'three':
        return 1
    elif data == 'four':
        return 2
    elif data == 'five':
        return 3
    elif data == 'six':
        return 4
    elif data == 'eight':
        return 5
    else:
        return 6


def convertDoorNumber(data):
    if data == 'two':
        return 0
    else:
        return 1


# Import data
cars = pd.read_csv('car.csv')

# Drop columns not used for analysis
cars.drop(['fueltype', 'aspiration', 'enginelocation', 'fuelsystem', 'boreratio',
          'enginetype', 'stroke', 'compressionratio', 'peakrpm', 'highwaympg'], axis=1, inplace=True)

# Add a column, Volume
carvolume = cars["carlength"] * cars["carwidth"] * cars["carheight"]
cars.insert(7, 'carvolume', carvolume)
# Add a column, width^2
cardwith_sq = cars["carlength"] ** 2
cars.insert(8, 'cardwith_sq', cardwith_sq)
# Add a column, length^2
carlength_sq = cars["carwidth"] ** 2
cars.insert(8, 'carlength_sq', carlength_sq)

# Converting the categorical columns
cars["doornumber"] = cars["doornumber"].apply(convertDoorNumber)
cars["carbody"] = cars["carbody"].apply(convertCarBody)
cars["drivewheel"] = cars["drivewheel"].apply(convertDriveWheel)
cars["cylindernumber"] = cars["cylindernumber"].apply(convertCylinderNumber)

# store dataFrame for normalization
cars_norm = cars

# Normalized data: (x - mean)/range
for i in range(0, len(cars_norm.columns)):
    cars_norm.iloc[:, i] = (cars_norm.iloc[:, i] - cars_norm.iloc[:, i].mean()) / \
        (cars_norm.iloc[:, i].max() - cars_norm.iloc[:, i].min())

# Adding a column with the values 1
fill = pd.Series([1 for x in range(0, cars_norm.shape[0])])
cars_norm.insert(0, "Filler", fill)

# Export
cars_norm.to_csv('rodriguez_cars_preprocessed.csv', index=False)
