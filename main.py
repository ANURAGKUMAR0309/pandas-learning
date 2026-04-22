import pandas as pd
data = {
    'Name' : ['ANI','Rahul','Raghav','Ram','Ravi'],
    'Age':[21,12,14,18,19],
    'Salary':[10000,20000,30000,40000,50000]
}
df = pd.DataFrame(data)
print(df)
print(df.info()) 
print(df[df['Salary'] > 30000])
print(df['Age'].mean())