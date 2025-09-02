import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

# --- Cargar modelo entrenado ---
ruta_modelo = os.path.join(os.path.dirname(__file__), "..", "models", "final_model.pkl")
ruta_modelo = os.path.abspath(ruta_modelo)  # convierte a ruta absoluta
modelo = joblib.load(ruta_modelo)

st.title("Predicción de precios de portátiles 💻")

st.write("En este modelo de Machine Learning, hemos utilizado datos reales de Amazon, recopilados a través de web scrapping")

archivo = st.file_uploader("Sube un archivo CSV", type="csv")

if archivo:
    datos = pd.read_csv(archivo)

    # Predicciones
    datos["Prediccion_Price"] = modelo.predict(datos)

    # KPIs rápidos
    st.subheader("📊 Métricas principales")
    col1, col2, col3 = st.columns(3)
    col1.metric("Precio medio", round(datos["Prediccion_Price"].mean(), 2))
    col2.metric("Mínimo", round(datos["Prediccion_Price"].min(), 2))
    col3.metric("Máximo", round(datos["Prediccion_Price"].max(), 2))

    # Tabla con predicciones
    st.subheader("Datos con predicciones")
    st.dataframe(datos.head())  # preview

    # Checkbox para mostrar todo el dataset
    if st.checkbox("Ver dataset completo"):
        st.dataframe(datos)

    # Estadísticas
    st.subheader("Resumen de las predicciones")
    st.write(datos["Prediccion_Price"].describe())

    # Gráfica distribución
    st.subheader("Distribución de precios predichos")
    st.bar_chart(datos["Prediccion_Price"])

    # Comparación real vs predicho (si hay Price real en CSV)
    if "Price" in datos.columns:
        st.subheader("Comparación Precio real vs Predicho (línea)")
        st.line_chart(datos[["Price", "Prediccion_Price"]])

        st.subheader("Precio real vs predicho (scatter)")
        fig, ax = plt.subplots()
        sns.scatterplot(x=datos["Price"], y=datos["Prediccion_Price"], ax=ax)
        ax.plot(
            [datos["Price"].min(), datos["Price"].max()],
            [datos["Price"].min(), datos["Price"].max()],
            "r--"
        )
        ax.set_xlabel("Precio real")
        ax.set_ylabel("Precio predicho")
        st.pyplot(fig)

    # Botón para descargar resultados
    csv = datos.to_csv(index=False).encode("utf-8")
    st.download_button("Descargar predicciones en CSV", csv, "predicciones.csv", "text/csv")
