# Country Experiment 

import math 
import numpy as np
import matplotlib.pyplot as plt

A = 10
B = 10
C = 10
#print(A,B,C)


Grass = 100
#print(Resource)

#competitors = [A,B,C]
steal_amount = 5
resource_amount = 1

def competition(A,B,C, Resource, steal_amount, resource_amount):
    actions = ['idle', 'steal', 'resource']
    counter = 0
    Winner = 0
    while (A>0 and B>0) or (A>0 and C>0) or (B>0 and C>0):
        counter = counter + 1
        #print('Interation:',counter)
        
        #---------------------------------------#
        
        # Absorption added, so when a country goes to 0, it stops playing
        
        if A == 0:
            A_choice = 'idle'
        else:
            A_choice = np.random.choice(actions, p = [1/3, 1/3, 1/3])
        
        #print('A choose', A_choice)
        
        if A_choice == 'resource':
            if Resource > 0 and Resource - resource_amount >= 0:
                A = A + resource_amount 
                Resource = Resource - resource_amount
            elif Resource > 0 and Resource - resource_amount < 0:
                A = A + Resource
                Resource = 0
            elif Resource == 0:
                A = A - resource_amount
            else:
                A = A
        #print('resource left', Resource)
        
        if A_choice == 'steal':
            A_steal_from = np.random.choice(['B','C'], p = [1/2, 1/2])
            #print('A choose', A_steal_from)
            
            if A_steal_from == 'B':
                if (B > 0) and (B - steal_amount)>= 0: 
                    A = A+steal_amount
                    B = B-steal_amount
                elif (B > 0) and (B - steal_amount) < 0:
                    A = A + B
                    B = 0
                elif (B == 0) and (A - steal_amount >= 0 ):
                    A = A - steal_amount
                elif (B == 0) and (A - steal_amount < 0):
                    A = 0
                else:
                    A = A
                    

            if A_steal_from == 'C':
                if (C > 0) and (C - steal_amount >= 0):
                    A = A+steal_amount
                    C = C-steal_amount
                elif (C > 0) and (C - steal_amount < 0):
                    A = A + C
                    C = 0 
                elif (C == 0) and (A - steal_amount >= 0):
                    A = A- steal_amount
                elif (C == 0) and (A - steal_amount < 0):
                    A = 0
                else:
                    A = A

        #-------------------------------------# 
        
        if B == 0:
            B_choice = 'idle'
        else:
            B_choice = np.random.choice(actions, p = [1/3, 1/3, 1/3])
        #print('B choose', B_choice)
        
        if B_choice == 'resource':
            if Resource > 0 and Resource - resource_amount > 0:
                B = B + resource_amount 
                Resource = Resource - resource_amount
            elif Resource > 0 and Resource - resource_amount <= 0:
                    B = B + Resource
                    Resource = 0
            elif Resource == 0:
                    B= B - resource_amount
            else:
                B = B
        #print('resource left', Resource)
        
        if B_choice == 'steal':
            B_steal_from = np.random.choice(['A','C'], p = [1/2, 1/2])
            #print('B choose', B_steal_from)
            
            
            if B_steal_from == 'A':
                if (A >0 ) and (A - steal_amount >= 0):
                    B = B+steal_amount
                    A = A-steal_amount
                elif (A >0) and (A - steal_amount < 0):
                    B = B + A
                    A = 0
                elif (A == 0) and (B - steal_amount >= 0):
                    B = B - steal_amount
                elif (A == 0) and (B - steal_amount < 0):
                    B = 0
                else:
                    B = B
                    
            if B_steal_from == 'C':
                if (C > 0) and (C - steal_amount >= 0):
                    B = B+steal_amount
                    C = C-steal_amount 
                elif (C > 0) and (C - steal_amount < 0):
                    B = B + C
                    C = 0
                elif (C == 0) and (B - steal_amount >= 0 ):
                    B = B - steal_amount
                elif (C == 0) and (B - steal_amount < 0):
                    B = 0
                else:
                    B = B

            
        #-----------------------------------#
        if C == 0:
            C_choice = 'idle'
        else:
            C_choice = np.random.choice(actions, p = [1/3, 1/3, 1/3])
        
        #print('C choose', C_choice)
        
        if C_choice == 'resource':
            if Resource > 0 and Resource - resource_amount > 0:
                C = C + resource_amount 
                Resource = Resource - resource_amount
            elif Resource > 0 and Resource - resource_amount <= 0:
                 C = C + Resource
                 Resource = 0
            elif Resource == 0:
                 C = C - resource_amount     
            else:
                C = C
        #print('resource left', Resource)
        
        if C_choice == 'steal':
            C_steal_from = np.random.choice(['B','A'], p = [1/2, 1/2])
            #print('C choose', C_steal_from)
            
            if C_steal_from == 'B':
                if (B >0) and (B - steal_amount >= 0):
                    C = C + steal_amount
                    B = B - steal_amount
                elif (B >0) and (B - steal_amount < 0):
                    C = C+B
                    B = 0
                elif (B == 0) and (C - steal_amount >= 0 ):
                    C = C - steal_amount
                elif (B == 0) and (C - steal_amount < 0):
                    C = 0
                else:
                    C = C
                    
            if C_steal_from == 'A':
                if (A > 0) and (A - steal_amount >= 0):
                    C = C + steal_amount
                    A = A - steal_amount 
                elif (A >0) and (A - steal_amount <0):
                    C = C+A
                    A = 0
                elif (A == 0) and (C - steal_amount >= 0 ):
                    C = C - steal_amount
                elif (A == 0) and (C - steal_amount < 0):
                    C = 0
                else:
                    C = C
    #print('In the end-----', Resource)
            
    return Resource

storage = np.zeros(10000, dtype = float)

for i in range(len(storage)):
    storage[i] = competition(A,B,C, Grass, steal_amount, resource_amount)

plt.hist(storage)
