num = int(input()) 
storage = []
result = []
for i in range(1,num+1):
    a = int(input(" "+"  "))
    storage.append(a) 
for m in range(len(storage)):
    b = min(storage)
    storage.remove(b)
    result.append(b) 
j = ' '.join(str(i) for i in result)
print(j)
