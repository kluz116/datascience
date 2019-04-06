import pandas as pd
#dictionary with data stored in lists
raw_data = {'name': ['Allan', 'Herbert', 'Richard', 'Cate', 'Aisha'],
            'age': [22, 42, 36, 24, 73],
            'salary': [30000, 24000, 310000, 300000, 34000],
            'city': ["Jinja", "Kampala", "Arua", "Gulu", "Masaka"]}
#create a data frame
df = pd.DataFrame(raw_data, columns=['name', 'age', 'salary', 'city'])
#Save the data in the dataframe as a CSV under a specified path. Remember to change your path.
df.to_csv('/home/kluz/raw_data_created.csv')
