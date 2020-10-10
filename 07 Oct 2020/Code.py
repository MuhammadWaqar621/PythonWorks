
#import numpy 
import numpy as np

#read csv file and skip header 
my_data = np.genfromtxt('Attachment_1602050354.csv', delimiter=',',skip_header=1,dtype= str)

#print rain data 
print ('\nrain-faal in singapore from 1982-2018:\n')
print (my_data)
rain_col= np.vectorize(float)
print ('\nMean is :',"%.2f" % np.mean(rain_col(my_data[:,1])))
print ('\nStandard Deviation is :',"%.2f" % np.std(rain_col(my_data[:,1])))
print ('\nMaximum is :',np.max(rain_col(my_data[:,1])))
print ('\nMinimum is :',np.min(rain_col(my_data[:,1])))

