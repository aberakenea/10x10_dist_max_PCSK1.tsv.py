import os
import pandas as pd
import numpy as np

# Define the file path
file_path = '/home/abera/data1/data1/ENSG00000175426___PCSK1__dist_max.tsv'

# Check if the file exists at the specified path
if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    # Load the data from the TSV file
    data = pd.read_csv(file_path, sep='\t', index_col=0)

    # Check if the data loaded correctly
    print(data.head())

    # Define the number of populations and subset size
    num_populations = 5
    subset_size = 10

    # Generate random subsets for each population
    subsets = []
    for _ in range(num_populations):
        rows = np.random.choice(data.index, subset_size, replace=False)
        cols = np.random.choice(data.columns, subset_size, replace=False)
        subset = data.loc[rows, cols]
        subsets.append(subset)

    # Combine all subsets into a single DataFrame
    combined_subset = pd.concat(subsets, axis=1)

    # Save the combined subset to a new TSV file
    subset_file_path = '/home/abera/data1/data1/combined_subset_10x10.tsv'
    combined_subset.to_csv(subset_file_path, sep='\t')

    # Display the combined subset
    print(combined_subset)
    print(f"Combined subset saved to: {subset_file_path}")
