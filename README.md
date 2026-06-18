# Combined Cycle Efficiency Optimizer

## 🏗️ Project Overview
This project focuses on the performance optimization of a **Combined Cycle Power Plant (CCPP)**. By developing a digital twin using historical sensor data, the system predicts net hourly electrical power output (**PE**) and identifies the optimal operating setpoints to maximize efficiency, even under fluctuating ambient conditions.

![CCPP Flow Process](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Combined_cycle.svg/640px-Combined_cycle.svg.png)

## 🚀 Key Features
* **Predictive Modeling:** High-accuracy regression analysis using **XGBoost** to predict power output ($R^2 \approx 0.96$).
* **Feature Engineering:** Implementation of thermodynamic indices (*Air Density Index, AT-V Interaction, Specific Humidity*) to improve the model's physical intuition and convergence.
* **Prescriptive Engine:** A mathematical optimization module using `scipy.optimize` (**SLSQP**) to calculate the ideal exhaust vacuum (**V**) setpoint, maximizing efficiency based on current ambient inputs.
* **Interactive Dashboard:** A **Streamlit**-based UI that allows operators to perform real-time *"What-if"* analysis.

## 🛠️ Tech Stack
* **Language:** Python
* **ML Library:** XGBoost, Scikit-learn
* **Optimization:** SciPy (SLSQP algorithm)
* **UI/Dashboard:** Streamlit
* **Data Handling:** Pandas, NumPy, Matplotlib/Seaborn

## 📊 Results
The model successfully explains over **96% of the variance** in power production. This allows operators to mitigate the negative impacts of adverse ambient conditions by proactively adjusting cooling parameters, translating directly into operational cost savings.

## 📁 Repository Structure
* `/data`: Contains the CCPP dataset.
* `/notebooks`: Exploratory Data Analysis (EDA) and Model Training.
* `app.py`: The Streamlit dashboard application for real-time optimization.

## 👤 About the Author
**Julen Neila Garcia** | [www.linkedin.com/in/julen-neila-garcia-a42304268]

*Passionate about bridging the gap between Mechanical Engineering and Data Science.*
