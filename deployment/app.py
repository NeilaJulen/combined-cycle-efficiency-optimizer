import os
import streamlit as st
import numpy as np
import pandas as pd
import joblib

#Importación del modelo
# Esto le dice a Python: "Busca el archivo en la misma carpeta donde reside app.py"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'modelo_ccpp.pkl')
model = joblib.load(model_path)

st.title("🏗️ Optimizador de Eficiencia: Ciclo Combinado")

# 1. Sidebar con los inputs (Sensores)
st.sidebar.header("Condiciones Ambientales")
at = st.sidebar.slider("Temperatura (AT) [°C]", 1.8, 37.1, 20.0)
ap = st.sidebar.slider("Presión Ambiente (AP) [mbar]", 992.0, 1033.0, 1013.0)
rh = st.sidebar.slider("Humedad Relativa (RH) [%]", 25.0, 100.0, 70.0)

# 2. Función de optimización integrada
def optimizar_operacion(at, ap, rh, model):
    from scipy.optimize import minimize

    def funcion_a_minimizar(v_test):
        v = v_test[0]
        # Recalculamos las variables físicas derivadas
        air_density = ap / (at + 273.15)
        at_v_inter = at * v
        sat_pressure = np.exp((17.27 * at) / (at + 237.3))
        spec_hum = rh * sat_pressure
        features = np.array([[at, v, ap, rh, air_density, at_v_inter, spec_hum]])
        return -model.predict(features)[0]

    res = minimize(funcion_a_minimizar, [50.0], bounds=[(25.36, 81.56)], method='SLSQP')
    return res.x[0], -res.fun

# 3. Lógica del Botón
if st.button("🚀 Optimizar Setpoint de Vacío"):
    v_opt, pe_max = optimizar_operacion(at, ap, rh, model)

    col1, col2 = st.columns(2)
    col1.metric("Setpoint V ideal", f"{v_opt:.2f} cmHg")
    col2.metric("Potencia Máxima", f"{pe_max:.2f} MW")

    st.success("Recomendación: Ajuste el sistema de refrigeración del condensador al valor indicado para maximizar el rendimiento.")