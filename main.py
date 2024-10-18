# YOUR CODE HERE
lst1=[]
lst2=[]
a=int(input())
for i in range(a):
    n=int(input())
    lst1.append(n)
for i in range(a):
    n=int(input())
    lst2.append(n)
updated_lst=[]
def summation():
    for i in range(a):
        k=lst1[i]+lst2[i]
        updated_lst.append(k)
    return(updated_lst)
def find_min_max():
    l=min(updated_lst)
    h=max(updated_lst)
    min_max=(l,h)
    return min_max
print(summation())
print(find_min_max())
