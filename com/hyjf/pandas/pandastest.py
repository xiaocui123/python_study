import pandas as pd

reviews=pd.read_csv('../../../ign.csv')
print(reviews.head(5))

print(reviews.shape)

print(reviews.iloc[0:5,1:])

print(reviews.index)

# print(reviews.values)

print(reviews.loc[0:5,['score','release_year']])

print()
print(reviews['score'].head())

print(reviews['score'].mean())

print()
print(type(reviews.head(10).mean()))
print(reviews.head(10).mean())

print()
xbox_one_filter=(reviews['score'] > 7) & (reviews['platform'] == 'Xbox One')
print(reviews.loc[xbox_one_filter,['score','platform']])