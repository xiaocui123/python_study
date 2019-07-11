mutiples=[x for x in range(30) if x%3 == 1]

print(mutiples)

squared={x*2 for x in [1,2,2]}
print(squared)

a=[(1,2),(4,1),(9,10),(13,-3)]

a.sort(key=lambda x:x[0])

print(a)