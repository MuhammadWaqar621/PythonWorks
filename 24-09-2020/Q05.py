
def chebyshewdistance(v,w):
    
    ans = 0
    for i,j in zip(v,w):
        ans = max(ans,abs(i-j))
    return ans
v=[4,1]
w=[7,2]
print ('chebyshew distance is: '+ str(chebyshewdistance(v,w)))