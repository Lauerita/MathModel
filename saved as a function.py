# Country Experiment 

import math 
import numpy as np
#import matplotlib.pyplot as plt
import pandas
from collections import Counter
import random 

A = 10
B = 10
C = 10
aggressive = [1/6, 1/3, 1/3, 1/6]
passive = [1/3, 1/6, 1/6, 1/3]
equal = [1/4, 1/4, 1/4, 1/4]
#print(A,B,C)

Resource = 10
#print(Resource)

#competitors = [A,B,C]
steal_amount = 5
resource_amount = 1

def competition(A,B,C, Resource, steal_amount, resource_amount):
    #actions = ['idle', 'steal', 'resource']
    counter = 0
    Winner = 0
    while (A>0 and B>0) or (A>0 and C>0) or (B>0 and C>0):
        
        counter = counter + 1
        
        #print('Interation:',counter)
        
        #---------------------------------#
        # Proportional probabilities 
        
        # Adding absorptions with each choice 
        #--------------------------------------#
        
        if A == 0:
            A_choice = 'idle'
        else: 
            A_choice = np.random.choice(['idle', 'steal_B', 'steal_C', 'resource'], p = aggressive)
        if B == 0:
            B_choice = 'idle'
        else:
            B_choice = np.random.choice(['idle', 'steal_A', 'steal_C', 'resource'], p = passive)
        if C == 0:
            C_choice = 'idle'
        else:
            C_choice = np.random.choice(['idle', 'steal_B', 'steal_A', 'resource'], p = equal)
        
       
     
        #-------------------------------------#
        
        # Randomized order of their actions 
        
        action = ['A_choice', 'B_choice', 'C_choice']
        random.shuffle(action)
        #print('The order of this term is', action)
        
        #-------------------------------------#
        
        for i in range(len(action)):
            
            if action[i] == 'A_choice':
                #print('Calculating A')
                if A_choice == 'resource':
                    if Resource > 0:
                        A = A + resource_amount 
                        Resource = Resource - resource_amount
                    elif Resource > 0 and Resource - resource_amount < 0:
                        A = A + Resource
                        Resource = 0
                    elif Resource == 0:
                        A = A - resource_amount
                    else:
                        A = A
                
                if A_choice == 'steal_B':
                    if (B > 0) and (B - steal_amount)>= 0: 
                        A = A+steal_amount
                        B = B-steal_amount
                    elif (B > 0) and (B - steal_amount) < 0:
                        A = A + B
                        B = 0
                    elif (B == 0) and (A - steal_amount > 0 ):
                        A = A - steal_amount
                    elif (B == 0) and (A - steal_amount <= 0):
                        A = 0
                    else:
                        A = A
                            

                if A_choice == 'steal_C':
                    if (C > 0) and (C - steal_amount >= 0):
                            A = A+steal_amount
                            C = C-steal_amount
                    elif (C > 0) and (C - steal_amount < 0):
                            A = A + C
                            C = 0 
                    elif (C == 0) and (A - steal_amount > 0):
                            A = A- steal_amount
                    elif (C == 0) and (A - steal_amount <= 0):
                            A = 0
                    else:
                            A = A
                            
                            
            if action [i] == 'B_choice':
                
                if B_choice == 'resource':
                    #print('Calculating B')
                    if Resource > 0:
                        B = B + resource_amount 
                        Resource = Resource - resource_amount
                    elif Resource > 0 and Resource - resource_amount < 0:
                        B = B + Resource
                        Resource = 0
                    elif Resource == 0:
                        B= B - resource_amount
                    else:
                        B = B
                
                if B_choice == 'steal_A':
                    if (A >0) and (A - steal_amount >= 0):
                        B = B+steal_amount
                        A = A-steal_amount
                    elif (A >0) and (A - steal_amount < 0):
                        B = B + A
                        A = 0
                    elif (A == 0) and (B - steal_amount > 0):
                        B = B - steal_amount
                    elif (A == 0) and (B - steal_amount <= 0):
                        B = 0
                    else:
                        B = B
                            
                if B_choice == 'steal_C':
                    if (C > 0) and (C - steal_amount >= 0):
                        B = B+steal_amount
                        C = C-steal_amount 
                    elif (C > 0) and (C - steal_amount < 0):
                        B = B + C
                        C = 0
                    elif (C == 0) and (B - steal_amount > 0 ):
                        B = B - steal_amount
                    elif (C == 0) and (B - steal_amount <= 0):
                        B = 0
                    else:
                        B = B
                
                
            if action[i] == 'C_choice':
                #print('Calculating C')
                if C_choice == 'resource':
                    if Resource > 0:
                        C = C + resource_amount 
                        Resource = Resource - resource_amount
                    elif Resource > 0 and Resource - resource_amount < 0:
                         C = C + Resource
                         Resource = 0
                    elif Resource == 0:
                         C = C - resource_amount     
                    else:
                        C = C
                
                if C_choice == 'steal_B':
                    if (B >0) and (B - steal_amount >= 0):
                        C = C + steal_amount
                        B = B - steal_amount
                    elif (B >0) and (B - steal_amount < 0):
                        C = C+B
                        B = 0
                    elif (B == 0) and (C - steal_amount > 0 ):
                        C = C - steal_amount
                    elif (B == 0) and (C - steal_amount <= 0):
                        C = 0
                    else:
                        C = C
                            
                if C_choice == 'steal_A':
                    if (A > 0) and (A - steal_amount >= 0):
                        C = C + steal_amount
                        A = A - steal_amount 
                    elif (A >0) and (A - steal_amount <0):
                        C = C+A
                        A = 0
                    elif (A == 0) and (C - steal_amount > 0 ):
                        C = C - steal_amount
                    elif (A == 0) and (C - steal_amount <= 0):
                        C = 0
                    else:
                        C = C

        #-------------------------------------#
        
        #-------------------------------------#
    if (A > B) and (A > C):
        Winner = 'A'
            
    if (B > A) and  (B > C):
        Winner = 'B'
            
    if (C > A) and (C > B):
        Winner = 'C'
    
    if A == B == C:
        Winner = 'E'

    print('Winner is:', Winner)
            
    return Winner

result = competition(A,B,C, Resource, steal_amount, resource_amount)


storage = np.zeros(10000, dtype = str)

for i in range(len(storage)):
    storage[i] = competition(A,B,C, Resource, steal_amount, resource_amount)
    
# Convert strong vector to historgram 
letter_counts = Counter(storage)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar')





