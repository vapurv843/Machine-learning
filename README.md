# Machine-learning
Machine learning coding proposed by apurv verma.

**Data preprocessing** : *Day 1*  


Data preprocessing:First step to get started with machhine learning.

**Step1:** **Importing the required libraries**

1.Numpy

2.Pandas

3.Matplotlib

These three are essential library each time.

Pandas is the library used to import datasets and managing them.

Numpy is the library which contains all the Mathematical functions.

**Step 2:** **Importing the data set**

Data sets are generally availabe in .csv format.It contains data in tabular form.

We use read_csv.md method of pandas library to read the csv file as a dataframe.

Then we make seperate vectors and matrix of dependent variable and independent variables from the dataframe.

**Step3:** **Handling the missing data:**

Data is rarely clean and often you can have corrupt or missing values.

Missing data in the column is generally represented by NaN.

Data can be missing due to various reasons and it is very important to take care of that as it may affect the performance of the model.

We can replace the missing data by the median or mean of the entire column.

We use imputer class of sklearn.preprocessing module for this task.

**Step4:** **Encoding the categorical data**

Categorical data are variables that contain label values rather than numeric values.

Values such as yes or no can not be used in the mathematiccal equations of the model so we need to encode these variables into numbers.To achieve this we use  LabelEncoder class from sklearn.preprocessing library.

**Step4:** **Splitting the dataset into test set and training set**

We usually split dataset into two parts,One for the training the model called training set and other for testing the performance of the trained model called test set.
The ratio of split is generally 80% for the training and 20% for the testing.

For this purpose we import train_test_split() class from sklearn.model_selection module.

**Step5:** **Feature scaling**

Most of the machine learning algorithms use the Euclidean distance between two data points in their computation.

We have features in the dataset havinng  different range and it can pose problem ,so it is required to bring all the feature in some definite range so that the performance of the model can be improved.

For this StandardScaler class of sklearn.preprocessing module is used.


**Generally,Scaling is preferred after splitting the data set into test set and training set.**





