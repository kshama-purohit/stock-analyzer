import pandas as pd
from django.contrib.auth.models import User
from webapp.models import Stock

def run():
    # Read CSV file into a DataFrame
    csv_file_path = 'all_stocks_5yr.csv'
    df = pd.read_csv(csv_file_path)

    # Create Stock objects from DataFrame rows
    stock_objects = [
        Stock(
            name=row['Name'],
            date=pd.to_datetime(row['date'], format='%d-%m-%Y').date(),
            low=float(row['low']),
            high=float(row['high']),
            open=float(row['open']),
            close=float(row['close']),
            volume=int(row['volume'])
        ) for index, row in df.iterrows()
    ]

    # Bulk insert into the database
    Stock.objects.bulk_create(stock_objects)
    print(f"Successfully imported {len(stock_objects)} stock records.")

if __name__ == "__main__":  
    run()
