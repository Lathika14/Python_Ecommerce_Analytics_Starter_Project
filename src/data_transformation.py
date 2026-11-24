
import pandas as pd


def transform_data(orders, customers, products, regions):

    # Merge datasets
    customer_orders = pd.merge(
        orders, customers, on="customer_id", how="left"
    )

    customer_product = pd.merge(
        customer_orders, products, on="product_id", how="left"
    )

    final_data = pd.merge(
        customer_product, regions, on="region", how="left"
    )

    # Calculate sales
    final_data["sales"] = (
        final_data["quantity"] * final_data["unit_price"]
    )

    # Extract date information
    final_data["year"] = final_data["order_date"].dt.year
    final_data["month"] = final_data["order_date"].dt.month
    final_data["month_name"] = final_data["order_date"].dt.month_name()
    final_data["day"] = final_data["order_date"].dt.day

    print("Data transformation completed!")
    print("Final dataset shape:", final_data.shape)

    return final_data
