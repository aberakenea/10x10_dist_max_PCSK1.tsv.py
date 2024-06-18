import pandas as pd

# Provide the file path
file_path = "/home/abera/data1/data1/ENSG00000175426___PCSK1__dist_max.tsv"

# Define the number of rows and columns to subset
num_rows = 500
num_cols = 500

# Initialize an empty DataFrame to store the subset
subset = pd.DataFrame()

# Read the TSV file in chunks
chunk_size = 1000  # Adjust based on your system's memory
chunks = pd.read_csv(file_path, sep='\t', chunksize=chunk_size)

# Iterate over the chunks to find the required subset
for chunk in chunks:
    # Check if the chunk contains the rows we're interested in
    if len(subset) < num_rows:
        # Append the required rows to the subset
        subset = pd.concat([subset, chunk.iloc[:num_rows - len(subset), :]], ignore_index=True)
    if len(subset) >= num_rows:
        break

# Now subset the first 10 columns
subset = subset.iloc[:, :num_cols]

# Display the subset
print(subset)

# Optionally, save the subset to a new TSV file
subset.to_csv("/home/abera/data1/data1/500x500_dist_max_PCSK1.tsv", sep='\t', index=False)
