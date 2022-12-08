m=int(input("Enter Rows:"))
n=int(input("Enter columns:"))
a=[]
for i in range(m):
    b=[]
    for j in range(n):
        j=int(input("enter number ["+str(i)+"]["+str(j)+"]"))
        b.append(j)
    a.append(b)
for i in range(m):
    for j in range(n):
        print(a[j][i],end=" ")
    print()