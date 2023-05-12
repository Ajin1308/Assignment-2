l=[]
ele=int(input("Elements:"))
for i in range(ele):
    a=int(input("1st"))
    b=int(input("2nd"))
    l.append((a,b))
print(l)
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i][-1] > l[j][-1]:
            l[j], l[i]=l[i], l[j]
print(l)