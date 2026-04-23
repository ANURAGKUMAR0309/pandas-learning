import pandas as pd

data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice Smith', 'Bob Jones', 'Charlie Brown', 'Dana White', 'Edgar Allan', 'Fiona Apple'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales', 'HR'],
    'Salary': [60000, 85000, 78000, None, 55000, 62000],
    'Join_Date': ['2020-01-01', '2021-03-15', '2019-07-22', '2022-11-05', '2021-01-10', '2023-04-12']
}
df = pd.DataFrame(data)
#print(df)
df.to_csv("data.csv",index=False)
#print(df)
df = pd.read_csv("data.csv")
#print(df)
df.info()
#print(df.isnull().sum())

avg_salary=df['Salary'].mean()
df['Salary']=df['Salary'].fillna(avg_salary)
print(df.isnull().sum())