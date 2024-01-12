import os
import pandas as pd
import sqlite3

def import_csv_to_sqlite(folder_path, database_path):
    conn = sqlite3.connect(database_path)
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.CSV'):
            # Construct the full file path
            file_path = os.path.join(folder_path, file_name)        
            df = pd.read_csv(file_path)
            
            # Extract table name from file name (without extension)
            table_name = os.path.splitext(file_name)[0]
            
            # Write DataFrame to SQLite database
            df.to_sql(table_name, conn, index=False, if_exists='replace')
            
            print(f"Table '{table_name}' imported successfully.")
    
    # Close the database connection
    conn.close()

# Specify the folder containing CSV files and the SQLite database path
#csv_folder = '/path/to/csv/folder'
#database_path = '/path/to/sqlite/database.db'

# Call the function to import CSV files into SQLite
#import_csv_to_sqlite("/home/sebastian/infoRange/gps_data/sololo", "/home/sebastian/apps/kenya/sololo.sqlite")

# Function to merge all CSV files into one file
def merge_csv_files(folder_path, output_file):
    dfs = []

    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith('.CSV'):
            file_path = os.path.join(folder_path, file_name)
            # Read CSV file into a Pandas DataFrame, skip first row for files after the first one
            skip_rows = 1 if dfs else 0
            df = pd.read_csv(file_path, skiprows=skip_rows)

            # Append DataFrame to the list
            dfs.append(df)

    # Concatenate all DataFrames into one
    merged_df = pd.concat(dfs, ignore_index=True)

    # Write the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)

    print(f"All CSV files merged successfully and saved to '{output_file}'.")

# Specify the folder containing CSV files and the output file path
csv_folder = '/home/sebastian/infoRange/gps_data/sololo/'
output_csv = '/home/sebastian/infoRange/gps_data/sololo/sololo_total.csv'

# Call the function to merge CSV files
merge_csv_files(csv_folder, output_csv)