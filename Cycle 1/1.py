n1=int(input("enter the 1st intervel:"))
n2=int(input("enter the 2nd intervel:"))
for x in range(n1,n2):
    if x >1:
        for m in range(2,x):
            if(x % m)==0:
                print(x)
                break




