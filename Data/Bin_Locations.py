import pandas as pd
import numpy as np

# 1. Your core 6 locations (The 'Nodes')
base_data = {
    "Bin_ID": ["B01", "B02", "B03", "B04", "B05", "B06"],
    "Name": ["Sipna Depot", "Rajapeth", "Badnera Stn", "Irwin Area", "Sai Nagar", "Gadge Nagar"],
    "Lat": [20.8818, 20.92059, 20.8575, 20.93339, 20.89595, 20.9502],
    "Lon": [77.7471, 77.75428, 77.73219, 77.73219, 77.74754, 77.76579],
    "Type": ["Depot", "Commercial", "Transport", "Healthcare", "Student residence", "Market"],
    "Avg_Fill_Rate": [2, 10, 8, 5, 6, 12], # Typical rate for that area type
    "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

}

# 2. Expand to 100 rows
rows = []
for i in range(100):
    # Pick a random bin from the base 6
    idx = np.random.randint(0, 6)
    
    # Get base details
    bin_id = base_data["Bin_ID"][idx]
    area_type = base_data["Type"][idx]
    base_rate = base_data["Avg_Fill_Rate"][idx]
    
    # Add 'Noise' to make it realistic
    # Current_Fill: Randomly between 20% and 90%
    current_fill = np.random.randint(20, 95)
    

    # When creating your 100 rows:
    # ... inside the loop ...
    day = np.random.choice(base_data["days"])
    # Now the model has a 'reason' for the outliers!
    # Variation in fill rate (e.g., Sunday might be busier)
    # This ensures the model has to 'learn' and can't just memorize
    actual_rate = base_rate + np.random.uniform(-1.5, 1.5)
    
    # Calculate target: Hours_Left = (100 - Current) / Rate
    hours_left = (100 - current_fill) / actual_rate
    
    rows.append({
        "Bin_ID": bin_id,
        "Area_Type": area_type,
        "Current_Fill_Pct": current_fill,
        "Actual_Fill_Rate": round(actual_rate, 2),
        "Hours_Left": round(hours_left, 2),
        "Lat": base_data["Lat"][idx],
        "Lon": base_data["Lon"][idx],
        "days":day

    })

# 3. Create DataFrame and Save
df_synthetic = pd.DataFrame(rows)
df_synthetic.to_csv("amravati_historical_waste.csv", index=False)

print("Success! Created 100 rows of historical data.")
print(df_synthetic.head())