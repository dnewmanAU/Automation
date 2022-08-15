import pandas as pd

df = pd.read_excel("supermarket-sales.xlsx")

# Get specific columns
df = df[["Gender", "Product line", "Total"]]

# Get the total value of every product line summed by gender
pivot_table = df.pivot_table(
    index="Gender", columns="Product line", values="Total", aggfunc="sum"
).round(0)

# Export pivot table starting at row 4 and call the sheet 'Report'
pivot_table.to_excel("pivot-table.xlsx", "Report", startrow=4)
