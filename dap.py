# -*- coding: utf-8 -*-
"""DAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m-RvgxcIEOyIkNmMWOxBeiAotAcWrq1R
"""

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
zeros_arr=np.zeros((3,3),dtype=int)
print(zeros_arr)
ones_arr=np.ones((2,2),dtype=int)
print(ones_arr)
arange_arr=np.arange(100)
print(arange_arr)
d=arr.reshape(5,1)
print(d)
e=arr[2:4]
print(e)
arr=np.array([1,2,3,4])
arr1=np.array([5,6,7,8])
c=np.vstack(arr+arr1)
d=np.vstack(arr+arr1)
print(c,d)
ar=np.array([1,2,3,4,5,6])
trans=ar.T
print(trans)
split=np.split(ar,3)
print(split)



a=np.array([[1,2,6],[3,4,5]])
b=np.sum(a)
print(b)
a1=np.array([[1,2,3],[4,5,6]])
b1=np.array([[1,2,3],[4,5,6]])
c=np.sum(a1+b1)
print(c)
a=np.array([[2,4,6],[1,3,5]])
c=np.sum(a,axis=0)
d=np.sum(a,axis=1)
print(c,d)
a=np.array([1,2,3,4,5])
b=np.mean(a)
print(b)
c=np.median(a)
print(c)
d=np.var(a)
print(d)
e=np.std(a)
print(e)

data=np.loadtxt("/data.txt",dtype=int)
data=np.savetxt("/date.txt",data)
print(data)

import matplotlib.pyplot as plt
a=np.array([1,2,3,4])
plt.plot(a)

import pandas as pd
a=["lalitha","priya","sunitha","dhana","mouni"]
r=pd.Series(a,index=[67,43,44,34,55])
print(r)

df=pd.read_csv("/content/books_data.csv")
print(df)

df=pd.read_csv("/content/save.txt", sep=" ")
print(df)

df=pd.read_excel("")
print(df)

import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.scatter(runs,w,color='orange')
plt.title("INDvsAUS score")
plt.show

import numpy as np
import matplotlib.pyplot as plt
tigar=np.linspace(-2*np.pi, 2*np.pi, 50)
print(tigar)
plt.plot(tigar,np.sin(tigar) ,color='black')
plt.title("sin(x)")

import numpy as np
import matplotlib.pyplot as plt
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
plt.subplot(2,1,2)
plt.plot(overs,runs_i,color='blue',label='India')
plt.legend(loc='best')
plt.subplot(2,1,1)
plt.plot(overs_a,runs_a,color='yellow',label='Aus')
plt.legend(loc='best')
plt.show()

import matplotlib.pyplot as plt
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
profit_a=[(a[i]-a[i-1])for i in range(1,len(a))]
profit_b=[(b[i]-b[i-1])for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth='3',label='companyA',marker='*',ms='15',mec='k')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='black',linestyle='dotted',label='companyb',marker='H')

a=np.array([25,60,5,10])
labe=["AIML","PYTHON","Pandas","Numpy"]
explo=[0.2,0,0,0]
colo=(["hotpink","darkblue","yellow","black"])
plt.pie(a,labels=labe,explode=explo,startangle=180,colors=colo)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
#Load the dataset containing daily temperatures
#Assuming the dataset is in a CSV file named "temperature_data.Csv' with a column named 'temperature'
df=pd.read_csv("/content/daily temperatures - Sheet1.csv")
print(df)
average_temperature=df['Temperature(celsius)'].mean()
highest_temperature=df['Temperature(celsius)'].max()
lowest_temperature=df['Temperature(celsius)'].min()
threshold=30
days_above_threshold=df[df['Temperature(celsius)']>threshold].shape[0]
print("Average temperature for the month:",average_temperature)
print("Highest temperature recorded:",highest_temperature)
print("Lowest temperature recorded:", lowest_temperature)
print("Number of days where temperature exceeded",threshold,"degrees celsius:",days_above_threshold)
plt.show()

pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
#load the anscombe dataset
anscombe=sns.load_dataset("anscombe")
print(anscombe)
#load example dataset
data=sns.load_dataset("anscombe")
#create a scatter plot
sns.violinplot(x="x",y="y",data=data)
plt.title("scatter plot of date vs. temperature")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
print(iris)
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of iris dataset")
plt.show()

import matplotlib.pyplot as plt
planets=sns.load_dataset("planets")
print(planets)
correlation_matrix=planets.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of planets dataset")
plt.show()

