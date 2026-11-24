
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_data():
    customers = pd.read_excel(DATA_DIR / "customers.xlsx")
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    products = pd.read_csv(DATA_DIR / "products.txt", sep="|")
    regions = pd.read_excel(DATA_DIR / "regions.xlsx")

    return customers, orders, products, regions


if __name__ == "__main__":
    customers, orders, products, regions = load_data()

    print("All datasets loaded successfully!")
    print("Customers:", customers.shape)
    print("Orders:", orders.shape)
    print("Products:", products.shape)
    print("Regions:", regions.shape)
