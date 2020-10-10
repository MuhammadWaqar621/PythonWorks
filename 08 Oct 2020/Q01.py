
import numpy  as np
my_data = np.genfromtxt('rainfall-monthly-total.csv',
                        delimiter=',',skip_header=1,dtype= str)

rain_col= np.vectorize(float)
avg=np.mean(rain_col(my_data[:,1]))
print ('\nMean is :',avg,'\n')
print ('\nrain-fall in singapore from 1982-2018 have rain more then mean :\n')
count=0;
for row in range(len(my_data)):
    if (rain_col(my_data[row,1]))>avg:
        count =count+1
        print (my_data[row])

print ('\nTotal Number of month have more than mean is :',count)