#Data Analysis covid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DataPreProcessingML.py/covid_data.csv")
#print(df.head())

#print(df.isnull().sum()) ##checking how many missing values there are
df = df[["Province_State","Country_Region","Confirmed","Recovered","Deaths","Active"]]
print(df.head())
print(df.isnull().sum())
df["Province_State"].fillna(value=" ",inplace = True) #replaces all the null values with spaces. Inplace - true means make the changes in the data set permanent 
#whenever there is a string column you can remnove missing values using fillna and usually give a space 
print(df.isnull().sum())


top_ten_countries = df.sort_values(by="Confirmed",ascending=False).head(10) # sorting data by confirmed cases in descending order
print(top_ten_countries[["Country_Region","Confirmed"]])
print()
top_five_countries = df.sort_values(by="Confirmed",ascending=False).head(5)
print(top_five_countries[["Country_Region","Confirmed"]])

print()
#least  5 
top_one_countries = df.sort_values(by="Confirmed",ascending=True).head(5) # sorting data by confirmed cases in descending order
print(top_one_countries[["Country_Region","Confirmed"]])
#erronous row in data set <---

plt.figure(figsize=(5,5))
x = top_ten_countries["Country_Region"]
y = top_ten_countries["Confirmed"]
plt.scatter(x,y,color="Red")
plt.xlabel("Top 10 Countries")
plt.ylabel("Number of confirmed cases")
plt.title("Top 10 Affected countries of covid")
plt.show()

plt.figure(figsize=(5,5))
x = top_ten_countries["Country_Region"]
y = top_ten_countries["Confirmed"]
plt.bar(x,y,color="Red")
plt.xlabel("Top 10 Countries")
plt.ylabel("Number of confirmed cases")
plt.title("Top 10 Affected countries of covid")
plt.show()



#HW: ANALYSE ALL CATEGORIES WITH VISUALISATION 
# EG TOP 10 DEATHS, TOP 10 ACTIVE, LEAST DEATH, TOP 10 RECOVERED 