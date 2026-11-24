
import pandas as pd


def clean_data(customers, orders, products, regions):

    dataframes = [customers, orders, products, regions]

    # Clean column names
    for df in dataframes:
        df.columns = df.columns.str.strip().str.lower()

    # Remove unwanted spaces
    for df in dataframes:
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].str.strip()

    # Convert data types
    orders["order_date"] = pd.to_datetime(orders["order_date"])
    orders["quantity"] = pd.to_numeric(orders["quantity"])
    products["unit_price"] = pd.to_numeric(products["unit_price"])

    print("Data cleaning completed!")

    return customers, orders, products, regions
