import create_dataframe as pd

my_dic = {
    'name': ['allan', 'Yusuf', 'Jane', 'James'],
    'age': [1, 2, 3, 4]}

df = pd.DataFrame(my_dic, index=[1, 2, 3, 4])
df.to_csv('/home/kluz/data.csv')
print(df.tail(2))
