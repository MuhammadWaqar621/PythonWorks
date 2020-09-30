class GroupofStudents:
    def group_avg():
        print ("************************************\n")
        print ("average is " ,sum(Scores)/len(Scores))
    
    def low_score():
        print ("************************************\n")
        print("Lower than average are: \n")
        for i in range (len(Names)):
            if Scores[i]<sum(Scores)/len(Scores):
                print ("Name",Names[i],"\t and Scores is ",Scores[i],"\n" )
            
        
    def high_score():
        print ("************************************\n")
        print("Higest Score : ")
        for i in range(len(Names)):
            if Scores[i]==max(Scores):
                print ("Name",Names[i],"\t and Scores is ",Scores[i],"\n" )
            
    def display():
        print ("************************************\n")
        print ("Students Data\n")
        for i in range(len(Names)):
            print ("Name",Names[i],"\t and Scores is ",Scores[i],"\n" )
            
Names=[]
Scores=[]  
def data(name,score):
    Names.append(name)
    Scores.append(score)
        
        
group1=GroupofStudents

data("Ayesha",58)
data("Maryam",89)
data("Fatima",34)
data("Reem",98)
data("Meera",85)
group1.display()
group1.group_avg()
group1.low_score()
group1.high_score()