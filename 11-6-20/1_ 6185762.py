
class MySetOperations:
   def myIsEmpty(self,A):
       if len(A):
           return False
       return True
   def myDisjoint(self,A,B):

       C= A&B
       if len(C):
           return False
       return True
   def myIntersection(self,A,B):
       return A&B
   def myUnion(self,A,B):
       return A | B
   def myDifference(self,A,B):
       return A-B
   def mySymDifference(self,A,B):
       return A^B

ob=MySetOperations()
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print (ob.myIsEmpty(A))
print (ob.myDisjoint(A,B))
print (ob.myIntersection(A,B))
print (ob.myUnion(A,B))
print (ob.myDifference(A,B))
print (ob.mySymDifference(A,B))