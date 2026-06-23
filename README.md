# Combined Cycle Efficiency Optimizer

## 🏗️ Project Overview
This project focuses on the performance optimization of a **Combined Cycle Power Plant (CCPP)**. By developing a digital twin using historical sensor data, the system predicts net hourly electrical power output (**PE**) and identifies the optimal operating setpoints to maximize efficiency, even under fluctuating ambient conditions.

![Integrated Gasification Combined Cycle Process Diagram](img/CCPP.jpg)

## 🚀 Key Features
* **Predictive Modeling:** At first, a high-accuracy regression analysis using **LinearRegression** to predict power output ($R^2 \approx 0.94$).
* * **Mathematical Smoothing:** Utilizing a **Polynomial Regression (Degree 2 Pipeline)** to guarantee a continuous, differentiable surface. This mathematical pivot prevents gradient-based optimizers from getting trapped in local minima or discrete "steps" common in tree-based algorithms like XGBoost.
* **Feature Engineering:** Implementation of thermodynamic indices (*Air Density Index, AT-V Interaction, Specific Humidity*) to improve the model's physical intuition and convergence.
* **Prescriptive Engine:** A mathematical optimization module using `scipy.optimize` (**SLSQP**) to calculate the ideal exhaust vacuum (**V**) setpoint, maximizing efficiency based on current ambient inputs.
* **Interactive Dashboard:** A **Streamlit**-based UI that allows operators to perform real-time *"What-if"* analysis.

## 🛠️ Tech Stack
* **Language:** Python
* **ML & Regressions:** Scikit-learn (PolynomialFeatures, LinearRegression)
* **Optimization Engine:** SciPy (SLSQP algorithm)
* **UI/Dashboard:** Streamlit
* **Data Engineering:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn

## 📊 Model Performance & Insights
The Polynomial Pipeline achieves an outstanding balance between predictive accuracy and prescriptive utility:
* **$R^2$ Score:** 0.9419 (explaining over 94% of the operational variance).
* **RMSE:** 4.1060 MW (~1% relative error across the typical production range).

The digital twin correctly identifies the underlying thermodynamic principle: minimizing exhaust vacuum ($V$) maximizes the enthalpy drop across the steam turbine, leading to peak electrical power output (**PE**).

## 📁 Repository Structure
* `/data`: Contains the CCPP dataset.
* `/notebooks`: Exploratory Data Analysis (EDA), model benchmarking (XGBoost vs. Random Forest vs. Polynomial), and sensitivity analysis.
* `/deployment`: The Streamlit dashboard application for real-time optimization. Contains the app file and the model.
* `/img`: Images, graphics and correlation matrixes obtained from the EDA process.
* `requirements.txt`: List of dependencies required to run the environment.

# Combined Cycle Efficiency Optimizer

> 🔗 **Live Dashboard:** [Access the Streamlit Application](https://combined-cycle-efficiency-optimizer-julen-neila-garcia.streamlit.app/)


## 👤 About the Author
**Julen Neila Garcia** | [www.linkedin.com/in/julen-neila-garcia-a42304268]

*Passionate about bridging the gap between Mechanical Engineering and Industrial Data Science.*
