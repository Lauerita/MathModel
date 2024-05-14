# Country Experiment 

import math 
import numpy as np
import matplotlib.pyplot as plt

A = 10
B = 10
C = 10
print(A,B,C)

Resource = 200
print(Resource)

actions = ['idle', 'steal', 'resource']
#competitors = [A,B,C]
steal_amount = 1
resource_amount = 1

sum = 0

while (A>0 and B>0) or (A>0 and C>0) or (B>0 and C>0):
    sum = sum + 1
    print('Interation:',sum)
    
    A_choice = np.random.choice(actions, p = [1/3, 1/3, 1/3])
    B_choice = np.random.choice(actions, p = [1/3, 1/3, 1/3])
    C_choice = np.random.choice(actions, p = [1/3, 1/3, 1/3])
    print(A_choice, B_choice, C_choice)
    
    #----------------------------------#
    
    
    if A_choice == 'resource':
        if Resource > 0:
            A = A + resource_amount 
            Resource = Resource - resource_amount
        else:
            A = A
    
    if A_choice == 'steal':
        A_steal_from = np.random.choice(['B','C'], p = [1/2, 1/2])
        print('A choose', A_steal_from)
        
        if A_steal_from == 'B':
            if (B > 0) and (B - steal_amount)>= 0: 
                A = A+steal_amount
                B = B-steal_amount
            elif (B > 0) and (B - steal_amount) < 0:
                A = A + B
                B = 0
        
            else:
                A = A
                

        if A_steal_from == 'C':
            if (C > 0) and (C - steal_amount >= 0):
                A = A+steal_amount
                C = C-steal_amount
            elif (C >0) and (C- steal_amount < 0):
                A = A + C
                C = 0
          
            else:
                A = A

    #-------------------------------------# 
    
    if B_choice == 'resource':
        if Resource > 0:
            B = B + resource_amount 
            Resource = Resource - resource_amount

        else:
            B = B
    
    if B_choice == 'steal':
        B_steal_from = np.random.choice(['A','C'], p = [1/2, 1/2])
        print('B choose', B_steal_from)
        
        
        if B_steal_from == 'A':
            if (A >0 ) and (A - steal_amount >= 0):
                B = B+steal_amount
                A = A-steal_amount
            elif (A >0) and (A - steal_amount < 0):
                B = B + A
                A = 0
        
            else:
                B = B
                
        if B_steal_from == 'C':
            if (C > 0) and (C - steal_amount >= 0):
                B = B+steal_amount
                C = C-steal_amount 
            elif (C > 0) and (C - steal_amount < 0):
                B = B + C
                C = 0
            else:
                B = B

        
    #-----------------------------------#
    
    if C_choice == 'resource':
        if Resource > 0:
            C = C + resource_amount 
            Resource = Resource - resource_amount
            
        else:
            C = C
    
    if C_choice == 'steal':
        C_steal_from = np.random.choice(['B','A'], p = [1/2, 1/2])
        print('C choose', C_steal_from)
        
        if C_steal_from == 'B':
            if (B >0) and (B - steal_amount >= 0):
                C = C + steal_amount
                B = B - steal_amount
            elif (B >0) and (B - steal_amount < 0):
                C = C+B
                B = 0
            else:
                C = C
                
        if C_steal_from == 'A':
            if (A > 0) and (A - steal_amount >= 0):
                C = C + steal_amount
                A = A - steal_amount 
            elif (A >0) and (A - steal_amount <0):
                C = C+A
                A = 0
            else:
                C = C

    #-------------------------------------#
    print(A,B,C)
    

    
    
    
    
        
    
    
        