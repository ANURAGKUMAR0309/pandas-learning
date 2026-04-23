import pandas as pd
data_frame = {
    'name':['A','B','C','D','E'],
    'marks':[46,'None',35,'None',70]
}
df=pd.DataFrame(data_frame)
df['marks'] = pd.to_numeric(df['marks'], errors='coerce')
print(df.isnull().sum())
print(df)