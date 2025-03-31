#data needs to be clean to be able to be understood and used for prediction models
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("DataPreProcessingML.py/Data.csv")
print(df.head())
print(df.info()) #--> function that gives database informatin 
#non-null data without missing values 

#checking how many missing values there are
print(df.isnull().sum())
X = df.iloc[:,0:3] #takes data in two parts 1) index of rows, : means everything  2) index of number of columns takes only first 3 columns. (0,1,2) as we dont wamt the 4th column
y = df.iloc[:,3] #takes all rows but only 3rd column 

print(X)
print(y) #target variable --> the amswer that the machine would predicts 
#feature columns are represented by capital X --> based on the data / features /factors, will the machine predict the target
#must import a module that helps us remove missing values 


from sklearn.impute import SimpleImputer # helps remove missing 
#by 1) deleting data where missing values are. 2) by replacing mising value with the average of the column 


imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
result = imputer.fit_transform(X.iloc[:,1:3])
X.iloc[:,1:3] = result #first and second index // second and third column. emilinating country factor as it is unuseful
print(X)

#data set should onlt be either integer or boolean values
#ENCODING 
#HOTENCODING
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder #modules

col_trans=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough") 
result2 = col_trans.fit_transform(X)
newdf = pd.DataFrame(result2)
print(newdf)



















