import pandas as pd
import os

# 1. 读取原始数据
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, 'carbon_data_export_WORLD.csv')
df = pd.read_csv(csv_path)

# 2. 转换日期列
df['Date'] = pd.to_datetime(df['Date'])

# 3. 提取年月字符串（如 2019-01）
df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)

# 4. 按 YearMonth 和 Sector 分组求和
grouped = df.groupby(['YearMonth', 'Sector'])['CO2 (Mt)'].sum().reset_index()

# 5. 使用透视表将 Sector 列转为列
pivot = grouped.pivot(index='YearMonth', columns='Sector', values='CO2 (Mt)').reset_index()

# 6. 指定想要的列顺序（如果存在）
desired_order = ['YearMonth', 'Domestic Aviation', 'Ground Transport', 'Industry', 
                 'International Aviation', 'Power', 'Residential', 'Total']
existing_columns = ['YearMonth'] + [col for col in desired_order[1:] if col in pivot.columns]
pivot = pivot[existing_columns]

# 7. 保存为新 CSV 文件
pivot.to_csv(r'D:\homework-c\ComprehensiveCourseExperiment\carbon_data\carbon_data_export_WORLD_new.csv', index=False)

# 8. 打印前几行预览
print(pivot.head())
print("透视表已生成，保存为 carbon_data_export_Japan_new.csv")



#  同理，处理其他表格时只需要修改读取中的“carbon_data_export_Brazil.csv”和保存中的“carbon_data_export_Brazil_new.csv”路径即可。

