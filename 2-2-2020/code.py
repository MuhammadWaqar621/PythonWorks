# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:38:20 2020

"""

names = ["Aliyah", "Bob", "Cathy", "Dan", "Ed", "Frank", "Darnell", 
    "Gary", "Shanice", "Irene", "Jack", "Kelly", "Demetrius"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19, 30] 
#print the all names list 
print ("\nNames:\n"+  str(names))
#print the all ages 
print ("\nAges:\n"+str(ages))
#zip function return the object
#create the dictionary
zip_=dict(zip(names,ages))
print ("\ndictionary : ")
print (zip_)
#iterator of tuples based on the iterable objects and dict function make 
#dictionary and zip combined both list 
entername=input("Please input an user to find out their age: ")
left_chance=5;

while (left_chance>1):
    '''
    check the name is exist in the dictionary or not 
    if name exist then print the age of the person by using 
    get function. get function give the corresponding value that 
    are store with key.
    '''
    if entername in zip_.keys():
        Age_of_Name=zip_.get(entername)
        print (entername + " is " +str(Age_of_Name)+ "!")
        break 
    else:
        ''''
        if name not exist in first time then re_enter the name 
        for 5 tries and decrease the try chance
        '''
        entername=input("There is nobody here named "+ entername +",please try again: ")
        left_chance=left_chance-1