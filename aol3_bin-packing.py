# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:22:58 2023

@author: t-jan
"""

import random
import matplotlib.pyplot as plt
#import math

def Harmonic_Number(n):
   # return 0.5772156649 + math.log(n) + 1/(2*n)
    Hn=0
    for i in range(1,n+1):
        Hn+=1/i
    return Hn

def Harmonic_Number_2(n):
    Hn2=0
    for i in range(1,n+1):
        Hn2+=1/i**2
    return Hn2

def random_number(rozklad,n): # <1,n>
    prawdopodobienstwa=[]
    przedzialy=[]
    if rozklad=='jednostajny' or rozklad=='j':
        for i in range(0,n):
            prawdopodobienstwa.append(1/n)
    elif rozklad=='harmoniczny' or rozklad=='h':
        Hn=Harmonic_Number(n)
        for i in range(1,n+1):
            prawdopodobienstwa.append(1/(i*Hn))
    elif rozklad=='dwuharmoniczny' or rozklad=='d' or rozklad=='dh':
        Hn2=Harmonic_Number_2(n)
        for i in range(1,n+1):
            prawdopodobienstwa.append(1/(i**2*Hn2))
    elif rozklad=='geometryczny' or rozklad=='g':
        for i in range(1,n):
            prawdopodobienstwa.append(1/2**i)
        prawdopodobienstwa.append(1/2**(n-1))
    else: return 'nieznany rozklad'
    przedzialy.append(0)
    for i in range(1,len(prawdopodobienstwa)+1):
        przedzialy.append(przedzialy[i-1]+prawdopodobienstwa[i-1])
    przedzialy.append(1)    
    X=random.random()
    for i in range(0,len(przedzialy)):
        if X>=przedzialy[i] and X<przedzialy[i+1]:
            return i+1


def bin_packing(ciag,algorithm):
    if algorithm=='next_fit' or algorithm=='nf':
        fill=0
        bins_counter=0
        for elem in range (0,len(ciag)):
            fill+=ciag[elem]
            if fill>1:
                elem-=1
                fill=0
                bins_counter+=1
        return bins_counter
        
    #elif algorithm=='random_fit' or algorithm=='rf':
    
        
    #elif algorithm=='first_fit' or algorithm=='ff':
        
    
    #elif algorithm=='best_fit' or algorithm=='bf':
        
    
    #elif algorithm=='worst_fit' or algorithm=='wf':
            
    
    else: return 'nieznany algorytm'



rozklad = 'j'
algorithm='nf'
ciag=[]
while len(ciag)<100:
    elem=random.random()
    k=random_number(rozklad,10)
    for i in range(0,k):
        ciag.append(elem)
        if len(ciag)==100:
            break

print(bin_packing(ciag, algorithm))
