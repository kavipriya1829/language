r=int(input())
k=list(map(int,input().split()[: r]))
k.sort()
for v in k:
  print(v,end=" ")
