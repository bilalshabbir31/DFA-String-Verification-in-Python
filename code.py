print('WELCOME TO THE PROJECT OF THEORY OF AUTOMATA')
print('NAME: MUHAMMAD BILAL , ID:F2018266166')
print('NAME: Obaid Ur Rehman , ID:F2018266227')
x=int(input('Enter No of States: '))       # No of States
State= [input('Enter states:') for i in range(0,x)]  
y= int(input("Enter the numbers Sigma Σ ="))   # No of Sigmas
Sigma=[input('Enter the Values of Σ=')
    for i in range(0,y)]
Final_State=input('Which State you are gonna say final?=') 
k=[0 for i in range(len(State))]
for i in range (len(State)):
    k[i]=[0 for j in range (len(Sigma))]
    for j in range(len(Sigma)):
        k[i][j]=input('From State'+ ' ' +State[i]+ ' ' +'if' + ' ' +Sigma[j]+ ' '+'go:')
def Adding_in_List(q,w):
    lis.append(k[State.index(q)][Sigma.index(w)])
    return k[State.index(q)][Sigma.index(w)]
while True:
 lis=[]
 strt=State[0]
 w=input("Enter your test string?=")
 for i in w :
     strt=Adding_in_List(strt, i)    # Adding and Returning State
 if lis[-1]==Final_State:
         print ('String Accepted by Grammer'+State[0]+'-->'+'-->'.join(lis)+')')
 else:
     print ('HMM Sorry !!! string not accepted')
