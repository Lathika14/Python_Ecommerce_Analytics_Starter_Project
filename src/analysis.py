# End-to-End E-Commerce Sales Analytics
# Run from the project root: python src/analysis.py

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
OUTPUTS = ROOT / "outputs"
PROCESSED.mkdir(parents=True, exist_ok=True)
OUTPUTS.mkdir(parents=True, exist_ok=True)

# 1. Read data from multiple sources
customers = pd.read_excel(RAW / "customers.xlsx")
orders = pd.read_csv(RAW / "orders.csv")
products = pd.read_csv(RAW / "products.txt", sep="|")
regions = pd.read_excel(RAW / "regions.xlsx")

# 2. Initial inspection
for name, df in {
    "customers": customers, "orders": orders,
    "products": products, "regions": regions
}.items():
    print(f"\\n--- {name.upper()} ---")
    print(df.head())
    print(df.shape)
    print(df.info())

# 3. Standardise column names and clean text
for df in [customers, orders, products, regions]:
    df.columns = df.columns.str.strip().str.lower()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

# 4. Convert data types
orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")
orders["quantity"] = pd.to_numeric(orders["quantity"], errors="coerce")
products["unit_price"] = pd.to_numeric(products["unit_price"], errors="coerce")

# 5. Data quality checks
print("Customer duplicates:", customers.duplicated(subset=["customer_id"]).sum())
print("Order duplicates:", orders.duplicated(subset=["order_id"]).sum())
print("Missing values in orders:\\n", orders.isna().sum())

# Remove duplicate business keys; keep first occurrence for this sample
customers = customers.drop_duplicates(subset=["customer_id"], keep="first")
orders = orders.drop_duplicates(subset=["order_id"], keep="first")
products = products.drop_duplicates(subset=["product_id"], keep="first")

# Remove records missing essential join keys
orders = orders.dropna(subset=["order_id", "customer_id", "product_id", "order_date"])
orders["quantity"] = orders["quantity"].fillna(0)
products = products.dropna(subset=["product_id", "unit_price"])

# 6. Merge datasets
master = orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
master = master.merge(products, on="product_id", how="left", validate="many_to_one")
master = master.merge(regions, on="region", how="left", validate="many_to_one")

# 7. Validate joins
print("Rows in orders:", len(orders))
print("Rows in master:", len(master))
print("Orders without customer:", master["customer_name"].isna().sum())
print("Orders without product:", master["product_name"].isna().sum())
print("Orders without region description:", master["region_description"].isna().sum())

# 8. Create business metrics
master["sales"] = master["quantity"] * master["unit_price"]
master["order_month"] = master["order_date"].dt.to_period("M").astype(str)

# Keep delivered orders for delivered-sales KPIs
delivered = master[master["order_status"].str.lower().eq("delivered")].copy()

# 9. KPI calculations
total_revenue = delivered["sales"].sum()
total_orders = delivered["order_id"].nunique()
total_units = delivered["quantity"].sum()
unique_customers = delivered["customer_id"].nunique()
average_order_value = total_revenue / total_orders if total_orders else 0

print("\\nBUSINESS KPIs")
print("Revenue:", total_revenue)
print("Delivered orders:", total_orders)
print("Units sold:", total_units)
print("Unique customers:", unique_customers)
print("Average order value:", round(average_order_value, 2))

# 10. Aggregations for charts
monthly_sales = delivered.groupby("order_month")["sales"].sum().sort_index()
category_sales = delivered.groupby("category")["sales"].sum().sort_values(ascending=False)
region_sales = delivered.groupby("region")["sales"].sum().sort_values(ascending=False)
top_products = delivered.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(5)

# 11. Save processed outputs
master.to_csv(PROCESSED / "master_orders.csv", index=False)
delivered.to_csv(PROCESSED / "delivered_orders.csv", index=False)
monthly_sales.rename("sales").to_csv(OUTPUTS / "monthly_sales.csv")

# 12. Matplotlib-only dashboard (no Seaborn, Plotly, Tableau or Power BI)
plt.rcParams["figure.figsize"] = (14, 9)
fig = plt.figure(constrained_layout=True)
fig.suptitle("E-Commerce Sales Performance Dashboard", fontsize=18, fontweight="bold")

# KPI cards
kpis = [
    ("Revenue", f"₹{total_revenue:,.0f}"),
    ("Delivered Orders", f"{total_orders:,}"),
    ("Units Sold", f"{total_units:,}"),
    ("Customers", f"{unique_customers:,}"),
    ("Avg Order Value", f"₹{average_order_value:,.0f}")
]
for i, (label, value) in enumerate(kpis, start=1):
    ax = fig.add_subplot(3, 5, i)
    ax.axis("off")
    ax.text(0.5, 0.68, value, ha="center", va="center", fontsize=15, fontweight="bold")
    ax.text(0.5, 0.25, label, ha="center", va="center", fontsize=9)

# Monthly trend
ax1 = fig.add_subplot(3, 2, 3)
monthly_sales.plot(kind="line", marker="o", ax=ax1)
ax1.set_title("Monthly Revenue")
ax1.set_xlabel("Month"); ax1.set_ylabel("Revenue (₹)")
ax1.grid(True, alpha=0.3)

# Category contribution
ax2 = fig.add_subplot(3, 2, 4)
category_sales.plot(kind="bar", ax=ax2)
ax2.set_title("Revenue by Category")
ax2.set_xlabel("Category"); ax2.set_ylabel("Revenue (₹)")
ax2.tick_params(axis="x", rotation=20)

# Regional sales
ax3 = fig.add_subplot(3, 2, 5)
region_sales.plot(kind="bar", ax=ax3)
ax3.set_title("Revenue by Region")
ax3.set_xlabel("Region"); ax3.set_ylabel("Revenue (₹)")
ax3.tick_params(axis="x", rotation=0)

# Top products
ax4 = fig.add_subplot(3, 2, 6)
top_products.sort_values().plot(kind="barh", ax=ax4)
ax4.set_title("Top Products by Revenue")
ax4.set_xlabel("Revenue (₹)")

dashboard_path = OUTPUTS / "ecommerce_dashboard.png"
fig.savefig(dashboard_path, dpi=200, bbox_inches="tight")
plt.show()

print(f"Dashboard saved to: {dashboard_path}")
print("Project completed.")
