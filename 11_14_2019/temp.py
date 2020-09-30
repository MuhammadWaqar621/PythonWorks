# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def calculateDetail(lst):
    print ("Average Sale: $" +str(float(sum(lst)/len(lst))))
    print ("Lowest Sale: $"+str(min(lst)))
    print ("Highest Sale: $"+str(max(lst)))
    allavg.append(float(sum(lst)/len(lst)))
    allmin.append(min(lst))
    allmax.append(max(lst))
reuse =True
allname=[]
allsale=[]
alldetails=[]
allavg=[]
allmin=[]
allmax=[]
while reuse:
    remainList=[]
    Name=input('Enter Name :')
    allname.append(Name)
    FirstSale=int(input("Enter First Sale Amount :$"))
    remainList.append(FirstSale)
    NoSale=int(input("Enter Number of Sales:"))
    allsale.append(NoSale)
    for i in range(NoSale-1):    
        while True:         
            input_=int(input("Enter Remaining Sales Amount :$"))
            if input_<0 or input_>25000:
                print ("You Enter the Amount of Range ($0-$25000)")
            else:
                remainList.append(input_)
                break
    alldetails.append(remainList)
    calculateDetail(remainList)
    char=input("Do you want to enter more Sale Person?")
    if char=="y":
        reuse=True
    else:
         print ("Name \t First Sale \t No.Sale \t Remaining Sale  \t Average Sale \t Loweset Sale \t Highest Sale")
         for i in range (len(allname)):
             print(allname[i]+"\t  "+str(alldetails[i][i]) +"\t\t  "+str(allsale[i]) +"\t\t" + str(alldetails[i][1:allsale[i]])+"  \t"+str(allavg[i])+ "\t\t"+str(allmin[i])+"\t\t"+ str(allmax[i]) ) 
         break 
    
    
