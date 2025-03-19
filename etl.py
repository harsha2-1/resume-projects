import pandas as pd
from sqlalchemy import create_engine
from config import DB_CONFIG

def extract_data():
    """Extract data from source PostgreSQL database using SQLAlchemy."""
    try:
        source_engine = create_engine(
            f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['source_db']}"
        )
        print("✅ Connected to source database successfully!")

        query = "SELECT * FROM schema1.table1;"  # Replace with actual table
        df = pd.read_sql(query, source_engine)  # ✅ Using SQLAlchemy engine

        source_engine.dispose()  # Close connection
        return df
    except Exception as e:
        print("❌ Extraction failed:", e)
        return None

def transform_data(df):
    """Transform data (Example: Convert names to uppercase)."""
    if df is not None:
        df["name"] = df["name"].str.upper()
        return df
    else:
        print("❌ No data to transform!")
        return None

def load_data(df):
    """Load data into target PostgreSQL database using SQLAlchemy."""
    if df is not None:
        try:
            target_engine = create_engine(
                f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['target_db']}"
            )
            df.to_sql("target_table", target_engine, if_exists="replace", index=False)  # Replace with actual table

            target_engine.dispose()  # Close connection
            print("✅ Data loaded into target database successfully!")
        except Exception as e:
            print("❌ Loading failed:", e)

if __name__ == "__main__":
    print("🚀 Starting ETL process...")
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)
    print("🎯 ETL process completed successfully!")

