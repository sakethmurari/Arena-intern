import pandas as pd


df = pd.read_csv("sales_2.csv")   
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)


best_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("Best Selling Product:", best_product)

print(" SALES REPORT ")
print("Total Sales:", total_sales)
print("Best Selling Product:", best_product)
print("Total Items Sold:", df["Quantity"].sum())
print("------------------------")




