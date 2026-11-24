
from pathlib import Path
import matplotlib.pyplot as plt


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def create_dashboard(
    delivered_data,
    monthly_sales,
    product_sales,
    category_sales,
    region_sales,
    order_status
):

    # Dashboard layout
    fig = plt.figure(figsize=(18, 13), facecolor="#F3F6FA")

    gs = fig.add_gridspec(
        3, 6,
        height_ratios=[0.8, 2, 2],
        hspace=0.5,
        wspace=0.6
    )

    fig.suptitle(
        "E-Commerce Sales Performance Dashboard",
        fontsize=22,
        fontweight="bold",
        color="#17324D",
        y=0.98
    )

    # -----------------------------
    # 1. KPI Calculations
    # -----------------------------

    total_revenue = delivered_data["sales"].sum()
    total_orders = delivered_data["order_id"].nunique()
    total_quantity = delivered_data["quantity"].sum()
    total_customers = delivered_data["customer_id"].nunique()

    average_order_value = (
        total_revenue / total_orders if total_orders else 0
    )

    kpis = [
        ("Total Revenue", f"₹{total_revenue:,.0f}"),
        ("Total Orders", f"{total_orders}"),
        ("Total Quantity", f"{total_quantity}"),
        ("Total Customers", f"{total_customers}"),
        ("Average Order Value", f"₹{average_order_value:,.2f}")
    ]

    # -----------------------------
    # 2. KPI Cards
    # -----------------------------

    for i, (label, value) in enumerate(kpis):

        ax = fig.add_subplot(gs[0, i:i+1])

        ax.set_facecolor("#FFFFFF")
        ax.set_xticks([])
        ax.set_yticks([])

        for spine in ax.spines.values():
            spine.set_visible(False)

        ax.text(
            0.5, 0.65,
            value,
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold",
            color="#176B87"
        )

        ax.text(
            0.5, 0.25,
            label,
            ha="center",
            va="center",
            fontsize=10,
            color="#526579"
        )

    # -----------------------------
    # 3. Monthly Sales Trend
    # -----------------------------

    ax1 = fig.add_subplot(gs[1, 0:3])

    ax1.plot(
        monthly_sales["month_name"],
        monthly_sales["total_sales"],
        marker="o",
        color="#176B87",
        linewidth=2
    )

    ax1.set_title(
        "Monthly Sales Trend",
        fontsize=14,
        fontweight="bold",
        color="#17324D"
    )

    ax1.set_ylabel("Sales (₹)")
    ax1.grid(True, alpha=0.3)

    # -----------------------------
    # 4. Product-wise Sales
    # -----------------------------

    ax2 = fig.add_subplot(gs[1, 3:6])

    ax2.barh(
        product_sales["product_name"],
        product_sales["sales"],
        color="#3296B8"
    )

    ax2.set_title(
        "Product-wise Sales",
        fontsize=14,
        fontweight="bold",
        color="#17324D"
    )

    ax2.set_xlabel("Sales (₹)")

    # -----------------------------
    # 5. Category-wise Sales
    # -----------------------------

    ax3 = fig.add_subplot(gs[2, 0:2])

    ax3.pie(
        category_sales["sales"],
        labels=category_sales["category"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax3.set_title(
        "Category-wise Sales",
        fontsize=14,
        fontweight="bold",
        color="#17324D"
    )

    # -----------------------------
    # 6. Region-wise Sales
    # -----------------------------

    ax4 = fig.add_subplot(gs[2, 2:4])

    ax4.bar(
        region_sales["region"],
        region_sales["sales"],
        color="#75B9D1"
    )

    ax4.set_title(
        "Region-wise Sales",
        fontsize=14,
        fontweight="bold",
        color="#17324D"
    )

    ax4.set_ylabel("Sales (₹)")
    ax4.tick_params(axis="x", rotation=0)

    # -----------------------------
    # 7. Order Status Distribution
    # -----------------------------

    ax5 = fig.add_subplot(gs[2, 4:6])

    ax5.pie(
        order_status.values,
        labels=order_status.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax5.set_title(
        "Order Status Distribution",
        fontsize=14,
        fontweight="bold",
        color="#17324D"
    )

    # -----------------------------
    # 8. Save Dashboard
    # -----------------------------

    dashboard_path = (
        REPORTS_DIR / "ecommerce_sales_dashboard.png"
    )

    fig.savefig(
        dashboard_path,
        dpi=300,
        bbox_inches="tight",
        facecolor="#F3F6FA"
    )

    plt.show()
    plt.close(fig)

    print("\nDashboard saved successfully!")
    print("Location:", dashboard_path)
