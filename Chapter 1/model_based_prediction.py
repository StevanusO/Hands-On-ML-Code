import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor


# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
x = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# Viz the data
lifesat.plot(kind = 'scatter', grid = True,
            x = "GDP per capita (USD)", y = "Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select linear model, activate line 21 and unactivate line 24
# model = LinearRegression()

# Select k-nearest neighbors regression, activaate line 24 and unactivate line 21
model = KNeighborsRegressor() 

# Train the model
model.fit(x,y)

# Make a prediction for Cyprus
x_new = [[37_655.2]] # Cyprus' GDP per capita in 2020
print(model.predict(x_new)) # Output: [[6.30165767]]