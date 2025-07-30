# 🚗 Car Sales Project

## 📌 Project Overview  
This project analyzes a comprehensive dataset of car sales, covering 30 manufacturers and 157 car models. It aims to clean and transform raw data, predict missing values using machine learning, and extract valuable insights through interactive dashboards to help stakeholders make informed decisions.

---

## 🎯 Objective  
- Predict missing values in the dataset (e.g., price, horsepower, engine size).
- Fix incorrect data types (especially dates).
- Perform detailed data analysis using Excel's Power Query, Power Pivot, and DAX.
- Visualize performance and financial trends using dashboards.
- Provide data-driven insights to support business strategy.

---

## 🧾 Dataset Description  
Each row in the dataset represents a car model with the following features:

| Column | Description |
|--------|-------------|
| `Manufacturer` | The company that produced the vehicle |
| `Model` | The specific name of the car model |
| `Sales_in_thousands` | Number of units sold in thousands |
| `__year_resale_value` | Estimated resale price after one year of use |
| `Vehicle_type` | Whether the car is Light or Medium |
| `Price_in_thousands` | Initial sale price in thousands of dollars |
| `Engine_size` | Engine displacement in liters |
| `Horsepower` | Power output of the engine (hp) |
| `Wheelbase` | Distance between the front and rear axles (in inches) |
| `Length` | Overall car length (in inches) |
| `Width` | Car width (in inches) |
| `Curb_weight` | Vehicle weight without passengers or cargo (lbs) |
| `Fuel_capacity` | Maximum fuel tank capacity (in gallons) |
| `Fuel_efficiency` | Fuel mileage (miles per gallon) |
| `Latest_Launch_Date` | Launch date of the latest version |
| `Power_perf_factor` | A calculated performance metric combining power and weight |

---

## 🛠️ Tools and Technologies  
- **Python**: For data preprocessing and predicting missing values  
  - `scikit-learn`: Machine learning library used to fill in missing values  
  - `pandas`, `datetime`: For data manipulation and type conversion  
- **Excel**: For data modeling and dashboarding  
  - Power Query  
  - Power Pivot  
  - DAX formulas  

---

## 📊 Exploratory Data Analysis  
The analysis included:
- Distribution of car types (Light vs Medium)
- Profit contribution by manufacturer and model
- Performance metrics like fuel efficiency, horsepower, engine size
- Price vs performance analysis

**Key Insights:**
- Total cars sold: **8,320,698**
- Total revenue: **$181.8 billion**
- Light cars account for **55.22%** of total cars and **70.70%** of total profit
- Medium cars account for **44.78%** of cars and **29.30%** of profit
- Top 5 manufacturers by profit: **Ford, Dodge, Toyota, Honda, Chevrolet** — making up **53.14%** of total profit
- Top 5 models by profit: **F-Series, Explorer, Expedition, Ram Pickup, Taurus** — contributing **20.21%**

  🔍 *For more insights, please check the **Main Dashboard**.*
---

## 🧹 Data Cleaning  
- Handled missing values in columns such as:
  - `__year_resale_value`, `Price_in_thousands`, `Engine_size`, `Horsepower`, `Wheelbase`, `Length`, `Width`, `Fuel_capacity`, `Fuel_efficiency`, `Power_perf_factor`
  - Used scikit-learn models for accurate prediction
- Fixed incorrect date types in the `Latest_Launch` column using Python’s `datetime` module

---

## 📈 Results and Insights  

### Manufacturer Performance:
- **Lincoln**: Highest average fuel capacity → *23 gallons*
- **Saturn**: Highest average fuel efficiency → *30.4 mpg*
- **Porsche**: Highest average horsepower → *272.33 hp*
- **Lincoln**: Highest average engine size → *4.87 liters*

📊 Shown in **Dashboard: Performance 1**

### Price vs Performance Analysis:
- Power Performance Factor vs Price  
- Horsepower vs Price  
- Fuel Capacity vs Price  
- Fuel Efficiency vs Price  
- Engine Size vs Price  

📊 Detailed in **Dashboard: Performance 2**

---

## 📌 Conclusion and Recommendations  
- Light vehicles are more profitable overall — focus on their production and marketing
- Invest in high-performing models with strong resale value
- Manufacturers like Lincoln,Saturn and Porsche demonstrate strong technical metrics

---

## 💡 How to Use the Project  
1. Open the Excel file: `Car_Sales_Project.xlsm`  
2. Use slicers to filter data by manufacturer, vehicle type, and performance metrics  
3. Explore:
   - **Main Dashboard**: Overall insights and key business metrics 
   - **Performance 1 Dashboard**: Fuel and engine metrics
   - **Performance 2 Dashboard**: Price vs performance analysis

---

## 🖼️ Screenshots  

### 📊 Main Dashboard  
![Main Dashboard](Car-Sales-Project/Screenshots/Main_Dashboard.png)

### ⚙️ Performance 1 Dashboard  
![Performance 1 Dashboard](Car-Sales-Project/Screenshots/Performance_1_Dashboard.png)

### 📈 Performance 2 Dashboard  
![Performance 2 Dashboard](Car-Sales-Project/Screenshots/Performance_2_Dashboard.png)

---

## 📂 Data Source  
Dataset available at:  
🔗 [Kaggle - Car Sales Dataset](https://www.kaggle.com/datasets/gagandeep16/car-sales)
