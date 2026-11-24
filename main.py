
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.data_transformation import transform_data
from src.data_analysis import analyze_data
from src.dashboard import create_dashboard


def main():

    print("Starting E-Commerce Sales Analytics Project...")

    # 1. Load datasets
    customers, orders, products, regions = load_data()

    # 2. Clean datasets
    customers, orders, products, regions = clean_data(
        customers, orders, products, regions
    )

    # 3. Transform datasets
    final_data = transform_data(
        orders, customers, products, regions
    )

    # 4. Perform data analysis
    (
        delivered_data,
        monthly_sales,
        product_sales,
        category_sales,
        region_sales,
        order_status
    ) = analyze_data(final_data)

    # 5. Create dashboard
    create_dashboard(
        delivered_data,
        monthly_sales,
        product_sales,
        category_sales,
        region_sales,
        order_status
    )

    print("\nE-Commerce Sales Analytics Completed Successfully!")


if __name__ == "__main__":
    main()
