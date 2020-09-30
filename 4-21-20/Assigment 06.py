# -*- coding: utf-8 -*-
"""
Name 
Date 
Assigment :06
"""
#a


def ﬁnd_doubleletter(word):
    n=len(word)
    for i in range(n-1):
        if (word[i] == word[i + 1]):
            return True 
    return False 
            


#b
    
 
def uniqueCharacters(str): 
    for i in range(len(str)): 
        for j in range(i + 1,len(str)):  
            if(str[i] == str[j]): 
                return False; 
    return True; 


def count_word():
    count=0
    file= open("word.txt","r")
    for i in file:
        if(ﬁnd_doubleletter(file.readline())):
            count=count+1
        elif(~uniqueCharacters(file.readline())):
            count=count+1
        else: 
            count=count
    return count

print ('File have',str(count_word()),' word which contains double letter')