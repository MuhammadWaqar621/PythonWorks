#part A
part_a=[48,66,97,86,72,83,68,93,81,78] 
print ("Task A:")
print("Original List :")
print (part_a)
#part b
for i in range(1,len(part_a)): 
    temp=part_a[i] 
    j=i-1 
    while j>=0 and temp>part_a[j]:
        part_a[j+1]=part_a[j] 
        j-=1
        part_a[j+1]=temp
        
        
print ("Task B:")
print("Sorted List :")
print (part_a)

#task c
for n,i in enumerate (part_a):
    if(90<=i<=100):
        part_a[n]="A"
    elif 80<=i<=89: 
        part_a[n]="B" 
    elif 70<=i<=79: 
        part_a[n]="C" 
    elif 60<=i<=69: 
        part_a[n]="D" 
    elif 0<=i<=59: 
        part_a[n]="F" 



print ("Task C:")
print("List Replace with letter :")
print (part_a)
