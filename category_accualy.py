import os
import pandas as pd

# Define the file path
file_path = '/home/abera/data1/data1/combined_subset_10x10.tsv'

# Check if the file exists
if os.path.exists(file_path):
    # Load the dataset
    combined_subset = pd.read_csv(file_path, sep='\t')

    # Display the first few rows of the dataframe to understand its structure
    print("Dataframe head:")
    print(combined_subset.head())

    # Display column names
    print("\nColumn names:")
    print(combined_subset.columns)

    # Define the category and column name to search
    category_to_find = 0  # Replace with the actual category value you are searching for
    column_name = 'Category'  # Replace with the actual column name

    # Check if the column exists in the dataframe
    if column_name in combined_subset.columns:
        # Check if the category exists in the column
        if category_to_find in combined_subset[column_name].unique():
            print(f"\nCategory {category_to_find} found in column {column_name}.")
            # Proceed with your original logic that uses the category
        else:
            print(f"\nCategory {category_to_find} not found in column {column_name}.")
            # Handle the error, perhaps by skipping this category or using a default value
            # Example: Log an error or skip processing
            print("Handling missing category...")
    else:
        print(f"\nColumn {column_name} not found in the dataframe.")
        # Handle the error, perhaps by providing a default action or logging the issue
        print("Handling missing column...")
else:
    print(f"File not found: {file_path}")
