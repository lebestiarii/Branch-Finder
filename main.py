import pandas as pd
import sqlite3

# Step 1: Load Data
df = pd.read_json("transformed_file.json")

# Step 2: Data Cleanup
df.columns = df.columns.str.strip()

# Step 3: Create Connection to DB
connection = sqlite3.connect('branches.db')

# Step 4: Insert the dataframe into the SQLite DB
df.to_sql('branches', connection, if_exists="replace")

# Step 5: Close connection (We'll reopen it later for querying)
connection.close()

def main():
    user_input = input("Enter a Port Code: ")
    user_input = user_input.upper()
    
    # Re-open the connection
    connection = sqlite3.connect('branches.db')
    
    # Execute the query using parameterized query
    #query = "SELECT * FROM branches WHERE `Port Code` = ?"
    query = "SELECT * FROM branches WHERE `Port Code` = ? OR `Number1` = ? OR `Number2` = ?"
    df_results = pd.read_sql_query(query, connection, params=(user_input,user_input,user_input))
    
    # Close the connection
    connection.close()
    
    # Adjust the DataFrame based on the 'Number2' column
    columns_to_print = ['Number1', 'Port Code', 'City', 'Country', 'Country Code']
    if 'Number2' in df_results.columns and not df_results['Number2'].eq('none').all():
        columns_to_print.insert(1, 'Number2')  # Include 'Number2' if it's not 'None'
    
    adjusted_df = df_results[columns_to_print].transpose()
    
    # Print results
    if not df_results.empty:
        print(adjusted_df)
    else:
        print("No matching records found.")
    
if __name__ == "__main__":
    main()
