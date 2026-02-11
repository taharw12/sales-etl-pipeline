import pandas as pd

def transform(df):
    print("Cleaning and Transforming data...")

   # remove leading/trailing spaces from column names
    df = df[df['UnitPrice'] > 0]

   # remove rows with discount greater than 1 (100%)
    df = df[df['Discount'] <= 1]

   # remove rows where Quantity is negative but ReturnStatus is not 'returned'
    df = df[~((df['Quantity'] < 0) & (df['ReturnStatus'] != 'returned'))]

    # remove leading/trailing spaces and convert to lowercase
    df["ReturnStatus"] = df["ReturnStatus"].astype(str).str.strip().str.lower()

    # create ReturnsQuantity column
    df["ReturnsQuantity"] = df.apply(
        lambda x: abs(x["Quantity"]) if x["ReturnStatus"] == "returned" else 0,
        axis=1
        )

    
     # calculate Gross Revenue
    df["GrossRevenue"] = df["Quantity"] * df["UnitPrice"]

    # calculate Net Revenue after discount
    df["NetRevenue"] = df["GrossRevenue"] * (1 - df["Discount"])

    print(f"Data transformed successfully. Remaining rows: {len(df)}")
    return df