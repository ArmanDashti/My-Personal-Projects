import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_column = 'Adj. Close'

# print(df)
# print('-------------------' + '\n')

# df.fillna(-9999, inplace = True)

# print(df)
# print('-------------------' + '\n')
# df.dropna(inplace = True)
# print(df)
# print('-------------------' + '\n')

forecast_out = int(math.ceil(0.01 * len(df)))
# print(forecast_out)

df['label'] = df[forecast_column].shift(-forecast_out)

# print(df['label'])
# print('-------------------' + '\n')

df.dropna(inplace = True)

# print(df['label'])
# print('-------------------' + '\n')
# df['label'] = df['label'].fillna(df['label'].mean())
# print(df['label'])
# print('-------------------' + '\n')
# y = np.array(df['label'])

# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(missing_values = 'NaN', strategy = 'mean')
# y = y.reshape(1, -1)

# imputer = imputer.fit(y)
# y = imputer.transform(y)

X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])
X = preprocessing.scale(X)

# X = X[:forecast_out+1]
# df.dropna(inplace = True)

# y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
accuracy = regressor.score(X_test, y_test)
print(accuracy)