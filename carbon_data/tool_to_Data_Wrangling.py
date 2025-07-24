import pandas as pd
import os

# 1. Read the original data
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, 'carbon_data_export_WORLD.csv')
df = pd.read_csv(csv_path)

# 2. Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 3. Extract year-month string (e.g., 2019-01)
df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)

# 4. Group by YearMonth and Sector and sum CO2 emissions
grouped = df.groupby(['YearMonth', 'Sector'])['CO2 (Mt)'].sum().reset_index()

# 5. Pivot so each Sector becomes a column
pivot = grouped.pivot(index='YearMonth', columns='Sector', values='CO2 (Mt)').reset_index()

# 6. Specify desired column order (if they exist)
desired_order = ['YearMonth', 'Domestic Aviation', 'Ground Transport', 'Industry',
                 'International Aviation', 'Power', 'Residential', 'Total']
existing_columns = ['YearMonth'] + [col for col in desired_order[1:] if col in pivot.columns]
pivot = pivot[existing_columns]

# 7. Save the result as a new CSV file
pivot.to_csv(r'D:\homework-c\ComprehensiveCourseExperiment\carbon_data\carbon_data_export_WORLD_new.csv', index=False)

# 8. Preview the first few rows
print(pivot.head())
print("Pivot table created and saved as carbon_data_export_Japan_new.csv")

# Similarly, for other files just change the input path (e.g., 'carbon_data_export_Brazil.csv')
# and the output path (e.g., 'carbon_data_export_Brazil_new.csv').
