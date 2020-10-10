import matplotlib.pyplot as plt
import numpy as np 
my_data = np.genfromtxt('relative-humidity-monthly-mean.csv', 
                        delimiter=',',skip_header=1,dtype= str)
rh_col= np.vectorize(float)
plt.hist(rh_col(my_data[:,1]))
plt.xlabel('relative humidity')
plt.ylabel('Frequency')
plt.title('Histogram of relative humidity')
plt.grid(True)
plt.show()
