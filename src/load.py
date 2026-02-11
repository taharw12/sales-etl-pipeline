import pandas as pd
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
# Load function to MySQL database
def load_to_mysql(df, table_name):
    user = "root"
    password = urllib.parse.quote_plus("YOUR_PASSWORD")
    host = "localhost"
    port = "3306"
    db_name = "online_sales_db" 

    try:
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}")
        
        print(f"Loading data into MySQL table: {table_name}...")
        
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        
        print("Data loaded to MySQL successfully!")
        
    except Exception as e:
        print(f"Error occurred: {e}")