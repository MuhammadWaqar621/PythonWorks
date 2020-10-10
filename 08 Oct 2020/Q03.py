import numpy  as np
import matplotlib.pyplot as plt
def gradient_and_intercept(xs,ys):
    gradient = (((np.mean(xs)*np.mean(ys)) - np.mean(xs*ys)) /
         ((np.mean(xs)*np.mean(xs)) - np.mean(xs*xs)))
    intercept = np.mean(ys) - gradient *np.mean(xs)
    
    return gradient , intercept

rain_fall_data = np.genfromtxt('rainfall-monthly-total.csv', 
                               delimiter=',',skip_header=1,dtype= str)
rel_hum_data=np.genfromtxt('relative-humidity-monthly-mean.csv', 
                           delimiter=',',skip_header=1,dtype= str)
norm_col= np.vectorize(float)
col_rain_fall=norm_col(rain_fall_data[:,1])
col_rel_hum=norm_col(rel_hum_data[:,1])
plt.scatter(col_rel_hum,col_rain_fall,label='data')
plt.title('relative humidity vs rainfall monthly')
plt.xlabel('relative humidity')
plt.ylabel('rainfall monthly')
#find gradient and intercept
m,b=gradient_and_intercept(col_rel_hum,col_rain_fall)
regression_line = [(m*x)+b for x in col_rel_hum]
plt.plot(col_rel_hum, regression_line,color='red',label='regression line')
plt.grid()
equation='y='+ str(round(m))+'x'+str(round(b))
plt.text(78, 165, equation,fontsize=20,color='black')
plt.show()
