mylist=['a','b','c','b','d','e','m','n','n']

duplicates=set([x for x in mylist if mylist.count(x)>1])

print(duplicates)

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])

print(input_set.intersection(valid))

print(input_set.difference(valid))

condition=True
print(2 if condition else 1/0)

print((1,2)[condition])