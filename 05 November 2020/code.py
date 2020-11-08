# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:10:01 2020

@author: waqar
"""

import pandas as pd 
import numpy as np 
df1=pd.read_excel('test.xlsx',sheet_name='Sheet1')
df2=pd.read_excel('test.xlsx',sheet_name='Sheet2')
size=len(df1.Artist)
matrix=np.zeros([size,size])
df3=pd.DataFrame(matrix,index=df1.Artist,columns=df1.Artist)
#print(df1)
#print(df2)
for i in df3.index:
    for j in df3.columns:
        #print (i,j,df2.Records_Sold[k])
        if(i=='coldplay') & (j=='y_l'):
            df3[j][i]=df2.Records_Sold[0]
        elif(i=='coldplay') & (j=='coldplay'):
            df3[j][i]=df2.Records_Sold[1]
        elif(i=='drake') & (j=='drake'):
            df3[j][i]=df2.Records_Sold[2]
        elif(i=='drake') & (j=='kodak'):
            df3[j][i]=df2.Records_Sold[3]
        elif(i=='j_taylor') & (j=='j_taylor'):
            df3[j][i]=df2.Records_Sold[4]
        elif(i=='j_taylor') & (j=='j_timber'):
            df3[j][i]=df2.Records_Sold[5]
        elif(i=='j_timber') & (j=='j_taylor'):
            df3[j][i]=df2.Records_Sold[6]
        elif(i=='j_timber') & (j=='j_timber'):
            df3[j][i]=df2.Records_Sold[7]
        elif(i=='kodak')&(j=='drake'):
            df3[j][i]=df2.Records_Sold[8]
        elif(i=='kodak')&(j=='kodak'):
            df3[j][i]=df2.Records_Sold[9]
        elif(i=='prince')&(j=='w_houston'):
            df3[j][i]=df2.Records_Sold[10]
        elif(i=='prince')&(j=='prince'):
            df3[j][i]=df2.Records_Sold[11]           
        elif(i=='w_houston')&(j=='w_houston'):
            df3[j][i]=df2.Records_Sold[12]
        elif(i=='w_houston')&(j=='prince'):
            df3[j][i]=df2.Records_Sold[13]
        elif(i=='y_l')&(j=='y_l'):
            df3[j][i]=df2.Records_Sold[14]
        elif(i=='y_l')&(j=='coldplay'):
            df3[j][i]=df2.Records_Sold[15]

print (df3)
'''
for i in range(len(df2.Artist)):
    for j in range (len(df2.Artist_2)):
        if (df2.Artist[i] in df3.index) & (df2.Artist[j] in df3.columns):
            df3[df3.index[i]][df3.columns[j]]=df2.Records_Sold[j]
        '''