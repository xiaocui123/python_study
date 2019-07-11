import pandas as pd

df=pd.DataFrame([[1,2],[4,5],[7,8]],index=['cobra','viper','sidewinder'],columns=['max-speed','shield'])

print(df)

print()

print(type(df.loc['viper']))
print(df.loc['viper'])

print()

print(type(df.loc[['viper','sidewinder']]))
print(df.loc[['viper','sidewinder']])

print()

print(type(df.loc['cobra','shield']))
print(df.loc['cobra','shield'])

print()

print(type(df.loc['cobra':'sidewinder','max-speed':'shield']))
print(df.loc['cobra':'sidewinder','max-speed':'shield'])

print()
print(df.loc[[False,False,True]])

print()
print(df.loc[df['shield']>6,['max-speed']])

print()
df.loc[df['shield']>6,'max-speed']

print()
print(df.loc[lambda df:df['shield'] == 8])

print()
df.loc[['viper','sidewinder'],'shield'] = 50
print(df)

print()
df.loc['cobra'] = 10
print(df)

print()
df.loc[:,'max-speed'] = 30
print(df)

print()
df.loc[df['shield']>35] = 0
print(df)