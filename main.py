import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
sns.set_style("whitegrid")

#reading the data set
df=pd.read_csv('delli.csv')
print(df.head())
print(df.describe())

#printing the shape of the data
print("The shape of the is ",df.shape)

#printing area
#df.cut is used as Use cut when you need to segment and sort data values into bins. This function is also useful for going
df['Area'] = pd.cut(df['Area'], bins=[0, 500,1000, 1500, 2000, 2500, 3000, np.inf],
labels=['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000', '3000+'])
fig, ax = plt.subplots(figsize=(5,5))#matplotlib function draws mutiple plots in a figure
ax.set_title('Area Distribution', fontsize=20)
sns.countplot(x='Area', data=df)
ax.set_ylabel('Count of Properties', fontsize=15)
ax.set_xlabel('Area Range(sq.ft)', fontsize=15)
plt.xticks(rotation=45)#for the equal spacing of the x axis 
plt.show()

#np.inf represnts positive and negative infinite
df['Price'] = pd.cut(df['Price'],
bins=[0,10000000,20000000,30000000,40000000,50000000,60000000,70000000,np.inf],
labels=['0-100', '100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700+'])
fig, ax = plt.subplots(figsize=(5,5))#matplotlib function draws mutiple plots in a figure
ax.set_title('Price Distribution', fontsize=20)
sns.countplot(x='Price', data=df)#seaborn module -uses bars
ax.set_ylabel('Count of Properties', fontsize=15)
ax.set_xlabel('Price Range(lakhs)', fontsize=15)
plt.xticks(rotation=45)#for the equal spacing of the x axis 
plt.show()


fig, ax = plt.subplots(figsize=(15, 10))
ax.set_title('No. of Bedrooms', fontsize=20)
sns.countplot(x='No. of Bedrooms', data=df)
ax.set_ylabel('Count of Properties', fontsize=15)
ax.set_xlabel('No. of Bedrooms', fontsize=15)
plt.xticks(rotation=45)
plt.show()



fig, ax = plt.subplots(figsize=(15, 10))
ax.set_title('Top 25 Properties by Location', fontsize=20)
sns.countplot(y='Location', data=df, order=df.Location.value_counts().index[:25])
ax.set_xlabel('Count of Properties', fontsize=15)
ax.set_ylabel('Location', fontsize=15)
plt.yticks(rotation=45)
plt.show()


plt.hist(df['SwimmingPool'],bins = 25, alpha = 0.5, 
         color = 'red')
plt.hist(df['Area'],bins = 25, alpha = 0.5,
         color = 'blue')

plt.legend(['SwimmingPool','Area'])
  
plt.show()

df['SwimmingPool'].plot(kind='hist')
plt.show()


