def merge(S1,S2):
    i=j=0
    S=[]
    while(i+j < len(S1)+len(S2)):
        if j==len(S2) or (i<len(S1) and S1[i]<S2[j]):
            S.append(S1[i])
            i+=1
        else:
            S.append(S2[j])
            j+=1
    return S

S1=[3, 9, 14, 18]
S2=[2, 5, 6, 15, 56]
print(merge(S1,S2))