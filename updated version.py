
import math 
import numpy as np
import matplotlib.pyplot as plt
import random

# This version of the code randomizes the order 

A = 10
B = 10
C = 10
print(A,B,C)

Resource = 100


steal_amount = 5
resource_amount = 1

fig,ax = plt.subplots()
counter = 0
x = list()
y1 = list()
y2 = list()
y3 = list()
y4 = list()
total = A + B + C + Resource


#(A>0 and B>0) or (A>0 and C>0) or (B>0 and C>0)

while (A>0 and B>0) or (A>0 and C>0) or (B>0 and C>0):
    
    counter = counter + 1
    
    print('Interation:',counter)
    
    #---------------------------------#
    # Proportional probabilities 
    
    aggressive = [1/6, 1/3, 1/3, 1/6]
    passive = [1/3, 1/6, 1/6, 1/3]
    equal = [1/4, 1/4, 1/4, 1/4]
    
    
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
    
   
    print('A choose:', A_choice,
          ', B choose:', B_choice,
          ', C choose:', C_choice)
    #-------------------------------------#
    
    # Randomized order of their actions 
    
    action = ['A_choice', 'B_choice', 'C_choice']
    random.shuffle(action)
    print('The order of this term is', action)
    
    #-------------------------------------#
    
    for i in range(len(action)):
        
        if action[i] == 'A_choice':
            print('Calculating A')
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
                print('Calculating B')
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
            print('Calculating C')
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


           
    
    print(A,B,C, Resource)
    x.append(counter)
    y1.append(A)
    y2.append(B)
    y3.append(C)
    y4.append(Resource)
    
ax.plot(x,y1, color = 'blue', label = 'Country A')
ax.plot(x,y2, color = 'purple', label = 'Country B')
ax.plot(x,y3, color = 'orange', label = 'Country C')
ax.plot(x,y4, color = 'green', label = 'Resource')
ax.legend()
    

    
    
    

