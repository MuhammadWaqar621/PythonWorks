
n=int(input('enter a positive number:'))
while (True):
    if(n>0):
        break
    else:
        n=int(input('Re enter a positive number:'))
    
for i in range (n):
    print ((i+1)**2)