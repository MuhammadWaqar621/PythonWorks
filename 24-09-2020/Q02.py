
import math 
p1 = [4,1.5]
p2 = [3,2]
p3 = [1,2]
#Euclidean
a1 = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
a2 = math.sqrt((p1[0]-p3[0])**2+(p1[1]-p3[1])**2)
a3 = math.sqrt((p2[0]-p3[0])**2+(p2[1]-p3[1])**2)
print ('Euclidean distance between p1 and p2 is : ' + str(a1))
print ('Euclidean distance between p1 and p3 is : ' + str(a2))
print ('Euclidean distance between p2 and p3 is : ' + str(a3))