import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
df = pd.read_excel('file.xlsx', index_col=0)
df.set_index('ID number', inplace = True)
df.columns = [' ','First_name','Surname','I1','I2','Quiz','Project','Mid_term']
print(df.head())
df2 = df
df1 = df.describe()

#initial graph
print(df1.head())
df['I1'].plot(label = 'initial_I1')
df['I2'].plot(label = 'initial_I2')
df['Quiz'].plot(label = 'initial_Quiz')
df['Project'].plot(label = 'initial_Project')
df['Mid_term'].plot(label = 'initial_mid_term')
plt.legend(loc = 4)
plt.title('Initial')
plt.xlabel('ID')
plt.ylabel('Marks')
plt.show()

print('\ninitial null values:\n')
print(df.isnull().sum())

# returning 1D array from Dataframe df1
li1 = np.array(df['I1'])
li2 = np.array(df['I2'])
liq = np.array(df['Quiz'])
lip = np.array(df['Project'])
lim = np.array(df['Mid_term'])


# reshaping the data to get 2D array rather than a 1D array

r_li1=li1.reshape(-1,1)
r_li2=li2.reshape(-1,1)
r_liq=liq.reshape(-1,1)
r_lip=lip.reshape(-1,1)
r_lim=lim.reshape(-1,1)

# replacing NaN with mean values
imp = Imputer(missing_values='NaN', axis = 0, strategy= 'mean')
l_i1 = imp.fit_transform(r_li1)
l_i2 = imp.fit_transform(r_li2)
l_iq = imp.fit_transform(r_liq)
l_ip = imp.fit_transform(r_lip)
l_im = imp.fit_transform(r_lim)


# replacing with 1D list
df['I1'].fillna(value = df['I1'].mean(), inplace= True)
df['I2'].fillna(value = df['I1'].mean(), inplace= True)
df['Quiz'].fillna(value = df['Quiz'].mean(), inplace= True)
df['Project'].fillna(value = df['Project'].mean(), inplace= True)
df['Mid_term'].fillna(value = df['Mid_term'].mean(), inplace= True)

# no of NaNs after replacing values
print('\n NaNs after replacing values')
print(df.isnull().sum())

#final plots :
D = df.describe()
print(D.head())
df['I1'].plot(label = 'final_I1')
df['I2'].plot(label = 'final_I2')
df['Quiz'].plot(label = 'final_Quiz')
df['Project'].plot(label = 'final_Project')
df['Mid_term'].plot(label = 'final_mid_term')
plt.legend(loc = 4)
plt.title('Inputed')
plt.xlabel('ID')
plt.ylabel('Marks')
plt.show()

# mean comparision
list = [0,1,2,3,4,5]
x = np.array(df1[1:2]).tolist()
y = np.array(D[1:2]).tolist()
plt.plot(x[0], label = 'initial')
plt.plot(y[0], label = 'final')
plt.title('Mean Comparision')
plt.legend()
plt.show()

# standard deviation comparision
x = np.array(df1[2:3]).tolist()
y = np.array(D[2:3]).tolist()
plt.plot(x[0],label = 'initial')
plt.plot(y[0], label = 'final')
plt.title('std comparision')
plt.legend()
plt.show()

