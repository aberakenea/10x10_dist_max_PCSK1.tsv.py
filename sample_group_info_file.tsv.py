import pandas as pd

# Define the file path
subset_file_path = '/home/abera/data1/data1/combined_subset_10x10.tsv'

# Load the data from the TSV file
combined_subset = pd.read_csv(subset_file_path, sep='\t', index_col=0)

# Display the first few rows to understand its structure
print(combined_subset.head())

# Assuming the sample group information is part of the column names or index
# Modify this part according to the actual structure of your data
if 'group' in combined_subset.columns:
    # Group information is in columns
    group_info = combined_subset['group']
elif 'group' in combined_subset.index.names:
    # Group information is in the index
    group_info = combined_subset.index.get_level_values('group')
else:
    # Group information needs to be extracted differently
    group_info = combined_subset.columns.str.extract(r'(\D+)')[0]  # Example regex to extract non-digit parts

# Display the group information
print("Sample Group Information:")
print(group_info)

# If needed, save the group information to a new file
group_info.to_csv('/home/abera/data1/data1/sample_group_info.tsv', sep='\t', header=True)
print(f"Sample group information saved to: /home/abera/data1/data1/sample_group_info.tsv")
