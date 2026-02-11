from extract import extract
from transform import transform
from load import load_to_mysql
# Main ETL function
def main():
    input_file = "data/raw/online_sales_dataset.csv"
    
   
    df = extract(input_file)
    
    if df is not None:
        
        df_transformed = transform(df)
        
        load_to_mysql(df_transformed, "fact_sales") 

if __name__ == "__main__":
    main()