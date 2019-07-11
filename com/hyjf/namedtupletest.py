from collections import namedtuple

Animal=namedtuple("Animal",["name","age","type"])

perry=Animal(name="perry",age=12,type="cat")

print(perry.name)

print(perry._asdict())