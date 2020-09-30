
#Task 1
import numpy as np
import pandas as pd
pd.set_option("display.precision", 2)
print ("\nTask 01:\n")
print ("numpy and pandas successfully import\n")

#task 02
df=pd.read_csv('C:\\Users\\waqar\\Desktop\\telecom_churn.csv')
print ("\nTask 02:\n")
print ("Dataset successfully import\n")

#Task 03
print ("\nTask 03:\n")
print ("first ten rows are:\n")
print(df.head(10))

#Task 04
print ("\nTask 04:\n")
print(df.iloc[0:200,0:len(df.columns)])

#Task 05
print ("\nTask 05:\n")
print (df.loc[0:499, ["State", "Account length","Total day minutes"]])

#task 06
print ("\nTask 06:\n")
print (df['Total eve calls'].astype(np.float64))

#task 07
print ("\nTask 07:\n")
print (df['State'].value_counts())

#task 08
print ("\nTask 08:\n")
print (df['State'].value_counts(True))


#task 09
print ("\nTask 09:\n")
df['Total eve calls'].hist()

#task 10
print ("\nTask 10:\n")
df['Total day charge'].hist()