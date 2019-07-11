def add_to(num,target=None):
    if not target:
        target=[]
    target.append(num)
    return target

add_to(1)
add_to(2)
add_to(3)
print(add_to(4))