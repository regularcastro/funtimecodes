i=217

list=[]
if i%2==0:
  list.append(0)
if i%2>0:
  list.append(1)
while i!=1:
  i=i//2
  if i%2>0:
    list.append(1)
  if i%2==0:
    list.append(0)

print(list)
