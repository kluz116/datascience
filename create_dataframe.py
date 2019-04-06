import pandas as pd

raw_data = {'name': ['Allan', 'Herbert', 'Richard', 'Cate', 'Aisha'],
            'age': [22, 42, 36, 24, 73],
            'salary': [30000, 24000, 310000, 300000, 34000],
            'city': ["Jinja", "Kampala", "Arua", "Gulu", "Masaka"]}
df = pd.DataFrame(raw_data, columns=['name', 'age', 'salary', 'city'])
print(df)
