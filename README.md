# End-to-End E-Commerce Sales Analytics

## Run
1. Create/activate a virtual environment.
2. `pip install -r requirements.txt`
3. `python src/analysis.py`

Input files are in `data/raw`. Processed tables and dashboard are saved in `data/processed` and `outputs`.

# 🛒 End-to-End E-Commerce Sales Data Analytics Project

## 📌 Project Overview

This project focuses on analyzing e-commerce sales data using Python. The main objective is to perform an end-to-end data analytics process, starting from data collection and cleaning to data transformation, exploratory data analysis (EDA), and dashboard creation.

Multiple data sources in different formats (CSV, Excel, and TXT) are integrated to create a consolidated dataset. The cleaned data is then analyzed to identify sales trends, product performance, category-wise revenue, regional sales, and order status distribution.

A visual dashboard is created using Matplotlib to present key business insights in an easy-to-understand format.

## 🎯 Project Objectives

- Import data from multiple file formats.
- Perform data cleaning and preprocessing.
- Handle data types and prepare data for analysis.
- Combine multiple datasets using Pandas.
- Perform exploratory data analysis (EDA).
- Calculate important business KPIs.
- Analyze monthly, product-wise, category-wise, and region-wise sales.
- Create a dashboard using Python Matplotlib.
- Export the cleaned dataset into CSV and Excel formats.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data cleaning, transformation, and analysis |
| Matplotlib | Data visualization and dashboard creation |
| Jupyter Notebook | Development and execution environment |
| Excel | Data storage and inspection |
| CSV | Data storage |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
Python_Ecommerce_Analytics_Starter_Project/
│
├── data/
│   └── raw/
│       ├── customers.xlsx
│       ├── orders.csv
│       ├── products.txt
│       └── regions.xlsx
│
├── reports/
│   ├── ecommerce_sales_dashboard.png
│   ├── cleaned_sales_data.csv
│   └── cleaned_sales_data.xlsx
│
├── README.md
└── requirements.txt
```

## 📊 Dataset Description

The project uses four datasets from different sources.

| Dataset | File Format | Description |
|---|---|---|
| Customers | Excel | Customer details such as ID, name, email, city, and region |
| Orders | CSV | Order details, order date, customer ID, product ID, quantity, and order status |
| Products | TXT | Product details, category, and unit price |
| Regions | Excel | Region information and region descriptions |

## ⚙️ Project Workflow

### 1. Data Loading

Imported datasets using Pandas:

- `read_excel()` – To read Excel files.
- `read_csv()` – To read CSV files.
- `read_csv(sep='|')` – To read pipe-delimited TXT files.

### 2. Data Inspection

Performed initial data inspection using:

- `head()`
- `shape`
- `columns`
- `info()`
- `describe()`
- `isnull().sum()`
- `duplicated().sum()`

### 3. Data Cleaning

Performed the following cleaning operations:

- Standardized column names.
- Removed unwanted leading and trailing spaces.
- Converted order date into datetime format.
- Converted quantity and unit price into numeric formats.
- Checked missing values and duplicate records.

### 4. Data Integration

Combined the four datasets using Pandas merge operations.

- Orders and Customers – Customer ID
- Customer Orders and Products – Product ID
- Customer Product Data and Regions – Region

Created a consolidated dataset named `final_data`.

### 5. Data Transformation

Created calculated columns:

- Sales = Quantity × Unit Price
- Year
- Month
- Month Name
- Day

Filtered delivered orders separately for delivered-sales analysis.

### 6. Exploratory Data Analysis (EDA)

Performed different types of business analysis:

- Monthly Sales Analysis
- Product-wise Sales Analysis
- Category-wise Sales Analysis
- Region-wise Sales Analysis
- Order Status Analysis
- Customer-wise Sales Analysis

### 7. KPI Calculation

Calculated key performance indicators:

- Total Revenue
- Total Orders
- Total Quantity Sold
- Total Customers
- Average Order Value (AOV)

### 8. Data Visualization

Created visualizations using Matplotlib:

- Monthly Sales Trend – Line Chart
- Product-wise Sales – Horizontal Bar Chart
- Category-wise Sales – Pie Chart
- Region-wise Sales – Bar Chart
- Order Status Distribution – Pie Chart

### 9. Dashboard Creation

Combined the KPI cards and charts into a single E-Commerce Sales Analytics Dashboard using Matplotlib.

The dashboard follows a consistent Blue and White color theme.

### 10. Data Export

Exported the final consolidated dataset into:

- CSV format
- Excel format

Saved the dashboard as a high-resolution PNG image.

## 📈 Key Business Insights

Based on the sample dataset:

| KPI | Result |
|---|---:|
| Total Revenue | ₹7,450 |
| Total Orders | 8 |
| Total Quantity Sold | 14 |
| Total Customers | 4 |
| Average Order Value | ₹931.25 |

**Additional observations:**

- 80% of the sample orders were delivered.
- 10% of orders were returned.
- 10% of orders were cancelled.
- Bluetooth Speaker generated the highest product-wise sales in the sample dataset.

*Note: Revenue and KPI calculations are based on delivered orders. Order status distribution includes all orders. These results are from a small sample dataset and are intended for project demonstration.*

## 📷 Dashboard Preview

The project dashboard includes:

- KPI Cards
- Monthly Sales Trend
- Product-wise Sales
- Category-wise Sales
- Region-wise Sales
- Order Status Distribution

Dashboard image: `reports/ecommerce_sales_dashboard.png`

## 🚀 How to Run This Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd Python_Ecommerce_Analytics_Starter_Project
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Open Jupyter Notebook

```bash
jupyter notebook
```

Open the project notebook and execute the cells in order.

## 📦 Requirements

Create a `requirements.txt` file with:

```text
pandas
matplotlib
openpyxl
jupyter
```

## 💡 Skills Demonstrated

- Python Programming
- Data Cleaning and Preprocessing
- Data Integration and Merging
- Data Transformation
- Exploratory Data Analysis (EDA)
- Data Aggregation and Grouping
- KPI Calculation
- Data Visualization
- Dashboard Development
- CSV and Excel Data Handling

## 🔮 Future Enhancements

- Work with larger real-world e-commerce datasets.
- Add interactive dashboard filters.
- Perform sales forecasting.
- Add profit and discount analysis when cost data is available.
- Automate the data cleaning and reporting process.
- Develop an interactive dashboard using Streamlit.

## 👩‍💻 Author

**Lathika S**

Aspiring Data Analyst | Python | SQL | Excel | Data Visualization

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.