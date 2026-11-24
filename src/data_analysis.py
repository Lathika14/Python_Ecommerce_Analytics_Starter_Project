
def analyze_data(final_data):

    # Filter delivered orders
    delivered_data = final_data[
        final_data["order_status"] == "Delivered"
    ].copy()

    # KPIs
    total_revenue = delivered_data["sales"].sum()
    total_orders = delivered_data["order_id"].nunique()
    total_quantity = delivered_data["quantity"].sum()
    total_customers = delivered_data["customer_id"].nunique()

    average_order_value = (
        total_revenue / total_orders if total_orders else 0
    )

    print("\n--- E-COMMERCE SALES KPIs ---")
    print("Total Revenue:", total_revenue)
    print("Total Orders:", total_orders)
    print("Total Quantity:", total_quantity)
    print("Total Customers:", total_customers)
    print("Average Order Value:", average_order_value)

    # Monthly sales
    monthly_sales = (
        delivered_data.groupby("month")["sales"]
        .sum()
        .reset_index(name="total_sales")
    )

    monthly_sales["month_name"] = (
        monthly_sales["month"]
        .apply(lambda x: __import__("calendar").month_abbr[x])
    )

    # Product sales
    product_sales = (
        delivered_data.groupby("product_name")["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=True)
    )

    # Category sales
    category_sales = (
        delivered_data.groupby("category")["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=False)
    )

    # Region sales
    region_sales = (
        delivered_data.groupby("region")["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=False)
    )

    # Order status
    order_status = final_data["order_status"].value_counts()

    return (
        delivered_data,
        monthly_sales,
        product_sales,
        category_sales,
        region_sales,
        order_status
    )

