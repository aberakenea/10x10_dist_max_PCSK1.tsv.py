import pandas as pd
import re

# Define the file path
subset_file_path = '/home/abera/data1/data1/combined_subset_10x10.tsv'

# Load the data from the TSV file
combined_subset = pd.read_csv(subset_file_path, sep='\t', index_col=0)

# Display the first few rows to understand its structure
print("Data loaded from combined subset file:")
print(combined_subset.head())

# Function to extract group information from column names
def extract_group_from_columns(columns):
    # The pattern to match groups from column names, adjust regex as necessary
    group_pattern = re.compile(r'(\D+)\d*')
    groups = [group_pattern.match(col).group(1) if group_pattern.match(col) else 'Unknown' for col in columns]
    return groups

# Extract group information from column names
groups = extract_group_from_columns(combined_subset.columns)

# Create a DataFrame for group definitions
group_definitions = pd.DataFrame({'Group': groups})
group_definitions_count = group_definitions['Group'].value_counts().reset_index()
group_definitions_count.columns = ['Group', 'Count']

# Display the group definitions
print("Group Category Definitions:")
print(group_definitions_count)

# Save the group definitions to a new TSV file
group_definitions_file_path = '/home/abera/data1/data1/group_definitions.tsv'
group_definitions_count.to_csv(group_definitions_file_path, sep='\t', index=False)
print(f"Group category definitions saved to: {group_definitions_file_path}")
