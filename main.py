import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

def calculate_average_tokens(directory):
    # List to store the results
    results = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            
            # Initialize variables to calculate average
            total_sum = 0
            total_count = 0

            try:
                # Read the CSV file in chunks
                for chunk in pd.read_csv(filepath, chunksize=10000, on_bad_lines='skip'):
                    # Convert 'tokens' column to numeric, setting errors='coerce' will replace non-numeric values with NaN
                    chunk['tokens'] = pd.to_numeric(chunk['tokens'], errors='coerce')

                    # Replace NaN values with 0
                    chunk['tokens'].fillna(0, inplace=True)

                    # Update total sum and count
                    total_sum += chunk['tokens'].sum()
                    total_count += chunk['tokens'].count()

                # Calculate the average of the 'tokens' column
                average_tokens = total_sum / total_count if total_count != 0 else 0

                # Append the result to the list
                results.append((filename, average_tokens))
            except pd.errors.ParserError as e:
                print(f"Error parsing {filename}: {e}")
            except Exception as e:
                print(f"Unexpected error with file {filename}: {e}")
    
    # Print the results as a table
    print(f"{'Filename':<100}{'Average Tokens'}")
    print("="*120)
    for filename, avg_tokens in results:
        print(f"{filename:<100}{avg_tokens:.2f}")

# Define the directory
log_dumps_directory = 'log_dumps'

# Call the function
calculate_average_tokens(log_dumps_directory)