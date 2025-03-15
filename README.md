# customer-sales-analy
A simple Python script for analyzing customer sales data from an Excel file.


Here’s a README template for your Sales Data Analysis project:


---

Sales Data Analysis

Description

This Python project reads sales data from an Excel file, performs basic data analysis, and generates a summary of total sales per product. It uses the pandas library to process and analyze the data, and outputs the results to a new Excel file.

Features

Load Sales Data: Reads sales data from an Excel file (sales_data.xlsx).

Total Sales Per Product: Groups the data by product and calculates the total sales for each product.

Save Summary: Saves the calculated summary of total sales per product to a new Excel file (sales_summary.xlsx).


Requirements

Python 3.x

Pandas Library


Installation

1. Install Python 3.x from python.org.


2. Install the required pandas library:



pip install pandas

3. Make sure the sales_data.xlsx file is in the same folder as your script.



Usage

1. Ensure that the sales_data.xlsx file is present in the same directory as the script.


2. Run the Python script. It will:

Load the sales data from the Excel file.

Calculate the total sales per product.

Save the summary to a new Excel file (sales_summary.xlsx).




Example:

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

Example Output

First 5 rows of the dataset:
   Product  Sales
0  ProductA   200
1  ProductB   150
2  ProductA   300
3  ProductC   120
4  ProductB   180

Total Sales Per Product:
Product
ProductA    500
ProductB    330
ProductC    120
Name: Sales, dtype: int64

Sales summary saved successfully!

License

MIT License. See LICENSE file for details.

