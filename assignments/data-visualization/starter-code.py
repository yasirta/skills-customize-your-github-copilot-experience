import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path(__file__).with_name("monthly-sales.csv")


def load_data():
    """Load the dataset and return a DataFrame."""
    df = pd.read_csv(DATA_FILE)
    return df


# TODO: Load the dataset
# df = load_data()

# TODO: Inspect the dataset
# print(df.head())
# print(df.columns)
# print(df.shape)

# TODO: Clean or convert the data as needed
# df["Month"] = pd.to_datetime(df["Month"])

# TODO: Calculate a summary statistic
# monthly_sales = df.groupby("Month")["Sales"].sum()

# TODO: Create a plot
# plt.figure(figsize=(10, 6))
# plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# TODO: Save a chart to a file
# plt.savefig("monthly-sales-chart.png")
