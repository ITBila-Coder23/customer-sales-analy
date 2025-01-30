sales_analysis.py
import pandas as pd

# Load the dataset (Make sure 'sales_data.xlsx' is in the same folder)
file_path = "sales_data.xlsx"
df = pd.read_excel(file_path)

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Total sales per product
sales_per_product = df.groupby('Product')['Sales'].sum()
print("\nTotal Sales Per Product:")
print(sales_per_product)

# Save the summary to a new Excel file
sales_per_product.to_excel("sales_summary.xlsx")
print("\nSales summary saved successfully!")
