x = input()
n = len(x)
c=0
l=0
for i in range(n):
    if(x[i]=='('):
        c=c+1
    elif(x[i]==')'):
        l=l+1
    
if(c==l and (x[0]=='(' and x[n-1]==')')):
    print("Valid")
else:
    print("Invalid")
