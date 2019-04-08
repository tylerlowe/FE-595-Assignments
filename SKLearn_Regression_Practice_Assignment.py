import pandas as pd
from sklearn import datasets
from sklearn import linear_model


# Load Boston data
boston_dataset = datasets.load_boston()
df = pd.DataFrame(boston_dataset.data, columns = boston_dataset.feature_names)
target = pd.DataFrame(boston_dataset.target)

# Fit Linear Model
regress = linear_model.LinearRegression()
regress.fit(df[:], target[0])


# Get Regression Co-effients
weights = pd.Series(regress.coef_, index = boston_dataset.feature_names)
weights_abs = abs(weights)
weights.sort_values()


# Print the sorted ('Coefficients,Greatest and Least influential variable
print('Coefficients: ', weights_abs.sort_values(ascending=False))
print('Greatest Influential   : ', weights_abs.idxmax())
print('Least Influential      : ', weights_abs.idxmin())