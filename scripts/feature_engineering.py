import pandas as pd

# Load cleaned data
df = pd.read_csv('../data/sales.csv')

# Feature Engineering
df['TotalSales'] = df['Quantity'] * df['Price']
df['OrderMonth'] = pd.to_datetime(df['OrderDate']).dt.month
df['OrderDay'] = pd.to_datetime(df['OrderDate']).dt.day

# Save features
df.to_csv('../data/sales_features.csv', index=False)
print("Features created and saved!")
