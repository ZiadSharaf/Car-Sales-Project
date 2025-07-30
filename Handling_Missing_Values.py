import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime

# Load CSV and treat blank/space cells as NaN
df = pd.read_csv("C:/Users/zyadn/Downloads/Car_sales/Car_sales.csv", na_values=["", " "])

# Save original copy for restoring non-missing columns
original_df = df.copy()

# Label encode categorical columns
label_encoders = {}
for col in ['Manufacturer', 'Model', 'Vehicle_type']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

# Convert 'Latest_Launch' to datetime
df['Latest_Launch'] = pd.to_datetime(df['Latest_Launch'], format='mixed', dayfirst=True, errors='coerce')

# Create numerical column from date for model use
df['Launch_days'] = (df['Latest_Launch'] - pd.Timestamp("2000-01-01")).dt.days

# List of columns with missing values
missing_cols = [
    '__year_resale_value', 'Price_in_thousands', 'Engine_size', 'Horsepower',
    'Wheelbase', 'Width', 'Length', 'Curb_weight', 'Fuel_capacity',
    'Fuel_efficiency', 'Power_perf_factor'
]

# Fill missing values using Random Forest
for col in missing_cols:
    df_temp = df.copy()
    not_null = df_temp[df_temp[col].notna()]
    is_null = df_temp[df_temp[col].isna()]

    if not is_null.empty:
        # Drop target and datetime column
        X = not_null.drop(columns=[col, 'Latest_Launch'])
        y = not_null[col]

        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(X, y)

        # Predict and fill
        predicted = model.predict(is_null.drop(columns=[col, 'Latest_Launch']))
        df.loc[df[col].isna(), col] = predicted

# Restore original non-missing columns (excluding Launch_days)
non_missing_cols = [col for col in original_df.columns if col not in missing_cols]
df[non_missing_cols] = original_df[non_missing_cols]

# Drop the helper column used only for modeling
df.drop(columns=['Launch_days'], inplace=True)

# Save cleaned and filled dataset
df.to_csv("Car_Sales_Filling_Missing_Values.csv", index=False)
