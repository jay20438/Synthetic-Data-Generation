import pandas as pd

# Loaded the CSV files
product_df = pd.read_csv('product_asin.csv')
review_df = pd.read_csv('reviews_supplements.csv')

# Renamed columns for clarity
product_df.rename(columns={'title': 'product_title'}, inplace=True)
review_df.rename(columns={'title': 'review_title'}, inplace=True)

# Merged the two DataFrames
merged_df = pd.merge(review_df, product_df, on=['parent_asin'], how='left')

# Dropped unnecessary columns
merged_df.drop(columns=['X','cat2', 'cat3', 'cat4', 'cat5', 'cat6'], inplace=True)

# Cleaned the 'cat1' column by removing all single quotes
merged_df['cat1'] = merged_df['cat1'].str.replace("'", '', regex=False)
merged_df['categories'] = merged_df['categories'].str.replace("'", '', regex=False)

# Removed any trailing brackets from the end of the cat1 values
merged_df['cat1'] = merged_df['cat1'].str.replace(r'\]$', '', regex=True)

# Cleaned the 'categories' column by removing brackets
merged_df['categories'] = merged_df['categories'].str.replace(r"^\[|\]$", '', regex=True)

# Stripped leading/trailing spaces in 'cat1'
merged_df['cat1'] = merged_df['cat1'].str.strip()

# Filtered the DataFrame to only include rows, where cat1 is 'Vitamins & Supplements'
filtered_df = merged_df[merged_df['cat1'] == 'Vitamins & Supplements']

# Display the filtered DataFrame
print(filtered_df)

# Saved the filtered DataFrame to a new CSV file
output_file = "filtered_combined.csv"
filtered_df.to_csv(output_file, index=False)

print("Filtered CSV saved as:", output_file)

nan_check = filtered_df.isna().any()

# No columns with NaN values
print("Columns with NaN values:")
print(nan_check[nan_check])