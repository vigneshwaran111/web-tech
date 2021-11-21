'''row = int(input("enter row : "))

for i in range(1,row+1):
    k = i
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+(row-j)
    print()'''

'''def visit(a,b):
    if a>b :
        return a-b
    else:
        return b-a
def distance(m,n,c):      #m-list of house n-cele.house c-cele in detail
    list_of_house = []
    m = int(m)
    n = int(n)
    for i in range(1,m+1):
        list_of_house.append(int(i))
    print(list_of_house)
    non_cele_house = []
    for i in list_of_house:
        if i not in c:
            non_cele_house.append(int(i))
    result=[]
    for i in non_cele_house:
        visit_distance = []
        for j in c:
            visit_distance.append(visit(i,j))
        result.append(min(visit_distance))
    print(max(result))
m = input()   
n = input()   
c = input().split(" ")
for i in range(0, len(c)):
    c[i] = int(c[i])
distance(m,n,c)'''
