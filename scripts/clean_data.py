import pandas as pd

df = pd.read_csv('../data/sales.csv')

# Fill missing values
df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)

# Save cleaned data
df.to_csv('../data/sales_clean.csv', index=False)
print("Data cleaned and saved!")
