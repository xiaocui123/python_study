def chain(*iterables):
    for it in iterables:
        yield from it

s='ABCDEF'
t=tuple(range(10))

print(list(chain(s,t)))