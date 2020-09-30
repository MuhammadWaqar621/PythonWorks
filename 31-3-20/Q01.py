#Task 0
import numpy as np
#Task01
print ("Task 01")
print(np.__version__)

#task02
array=np.zeros(10)
print ("Task 02")
print (array)


#task03
array2=np.ones(10)
print ("Task 03")
print (array2)

#task04
array3=np.ones(10)
print ("Task 04")
print (array3)


#task 05
array4=np.arange(10,49)
print("\nTask 05")
print (array4)

#task06
print("\nTask 06")
array5=np.arange(10)
print("Original : ")
print (array5)
array5=np.flipud(array5)
print ("Reverse :")
print (array5)


#Task 07
print ("\nTask  07")
array6=np.arange(9).reshape(3,3)
print (array6)


# task 08
print ("\nTask  08")
array7=np.ones(9).reshape(3,3)
print (array7)

#Task 09
print ("\nTask  09")
R_arr=np.random.rand(3,3)
print(R_arr)

#Task 10 
print ("\nTask  10")
R_array=np.random.rand(3,3,3)
print(R_array)

#Task 11 
print ("\nTask  11")
R_array_10=np.random.rand(10,10)
print(R_array_10)
print("Minimum is :"+ str(np.min(R_array_10)))
print ("Maximum is :"+str(np.max(R_array_10)))

#Task 12
print ("\nTask  12")
R_array_M=np.random.rand(1,30)
print(R_array_M)
print("Average is :"+ str(np.mean(R_array_M)))


#Task 13
print ("\nTask  13")
A=np.zeros([3,3])
B=np.ones([1,3])
C=np.ones([5,1])
array_5to5=np.concatenate((B,A,B))
array_5to5=np.concatenate((C,array_5to5,C),axis = 1)
print(array_5to5)
