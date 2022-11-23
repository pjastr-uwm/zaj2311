a=[[1,1],[1,1],[1,1]]
b=[[2,2],[2,2],[2,2]]


wynik = []
for i in range(0,len(a)):
    c = [x+y for x,y in zip(a[i],b[i])]
    wynik.append(c)

print(wynik)