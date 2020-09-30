
def myIsEmpty(set1):
    if len(set1) == 0: # length of set is empty then return true otherwise false
        return True
    else:
        return False
def myIntersection(set1,set2):
    result=set()
    for i in set1:
        if i in set2:
            result.add(i) #adding elements to set using add()
            return result
        # u can use set1 & set2 to return intersection of two sets
        #result = set1 & set2
        # u can also use intersection()
        # result=set1.intersection(set2)
        return result
def myUnion(set1,set2):
    for i in set2:
        set1.add(i)#adding elements of set2 to set1   
        return set1
    # u can use set1 | set2 to return union of two sets
    #result = set1 | set2
    # u can also use union()
    # result=set1.union(set2)
def myDisjoint(set1,set2):
    for i in set1:
        if i in set2:
            return False
        return True
    # u can also use isdisjoint()
    # result=set1.isdisjoint(s2)
s1=set([2,3,1,5])# initializing two sets using set()
s2=set([5,6,7,8])
print ("A=",s1)
print ("B=",s2)
status=myIsEmpty(s1)
if status==True:
    print ("A is empty")
else:
    print ("A is not empty")
status=myDisjoint(s1,s2)
if status==True:
    print ("A and B are disjoint")
else:
    print ("A and B are not disjoint")
    print ("Intersection of two sets are",myIntersection(s1,s2))
    print ("Union of two sets are ",myUnion(s1,s2))