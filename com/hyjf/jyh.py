def reverse(word):
    return word[::-1]

print(reverse("testing"))

fruits=['strawberry','fig','apple','cherry','raspberray','banana']

print(sorted(fruits,key=len))

fruits.sort(key=reverse,reverse=True)

print(fruits)

def fact(n):
    return 1 if n<2 else n*fact(n-1)

print(list(map(fact,range(6))))

print([fact(n) for n in range(6)])

print(list(map(fact,filter(lambda n: n%2,range(6)))))

print([fact(n) for n in range(6) if n%2])