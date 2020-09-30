

p1 = [4,1.5]
p2 = [3,2]
p3 = [1,2]
#Manhattan
a1 = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
a2 = abs(p1[0]-p3[0])+abs(p1[1]-p3[1])
a3 = abs(p2[0]-p3[0])+abs(p2[1]-p3[1])
print ('Manhattan distance between p1 and p2 is : ' + str(a1))
print ('Manhattan distance between p1 and p3 is : ' + str(a2))
print ('Manhattan distance between p2 and p3 is : ' + str(a3))