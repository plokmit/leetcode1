a=[0,1,2,2,3,0,4,2]
val=2
i=0
print(len(a)-a.count(val))
while i<a.count(val):
    a.extend("_")
    i+=1
while a.count(val)>0:
    a.remove(val)

print(a)