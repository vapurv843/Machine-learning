#Importing the dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data =pd.read_csv('Salary_Data.csv')
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values
#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size = 0.2,random_state=0)

#Implementing the linear regression class 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#Predicting the model 
y_pred=regressor.predict(x_test)
plt.scatter(x_train,y_train,color = 'pink')
plt.plot(x_train,regressor.predict(x_train))
plt.title("Experience vs salary {Training set}")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

#predicting the model on the test set

plt.scatter(x_test,y_test,color = 'red')
plt.plot(x_train,regressor.predict(x_train))
plt.title("Experience vs salary {Test set}")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
print(regressor.predict([[12]]))
print(regressor.coef_)
print(regressor.intercept_)
