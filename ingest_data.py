import pandas as pd
from sqlalchemy import create_engine
from time import time
import os
import argparse

def ingest_taxi_data(csv_name, table, engine):
    df_iter = pd.read_csv(csv_name, chunksize=100000)

    df = next(df_iter)

    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.head(n=0).to_sql(name=table, con=engine, if_exists='replace')
    df.to_sql(name=table, con=engine, if_exists='append')

    while True:
        try:
            t_start = time()
            
            df = next(df_iter)
            
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            
            df.to_sql(name=table, con=engine, if_exists='append')
            
            t_end = time()
            
            print('Inserted chunk... (%.3f second)' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

def ingest_zones_data(csv_name, table, engine):
    df = pd.read_csv(csv_name)
    df.to_sql(name=table, con=engine, if_exists='replace')
    print("Finished ingesting data into the postgres database")

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table = params.table
    url = params.url
    
    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'
    
    os.system(f"wget {url} -O {csv_name}")
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    if table == 'zones':
        ingest_zones_data(csv_name, table, engine)
    else:
        ingest_taxi_data(csv_name, table, engine)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='User name for Postgres')
    parser.add_argument('--password', required=True, help='Password for Postgres')
    parser.add_argument('--host', required=True, help='Host for Postgres')
    parser.add_argument('--port', required=True, help='Port for Postgres')
    parser.add_argument('--db', required=True, help='Database name for Postgres')
    parser.add_argument('--table', required=True, help='Name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='URL of the csv file')

    args = parser.parse_args()

    main(args)
