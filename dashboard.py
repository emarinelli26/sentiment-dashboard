import streamlit as st
import pandas as pd
import os
import plotly.express as px

# Funciones auxiliares
def list_csv_files(folder='data'):
    return [f for f in os.listdir(folder) if f.endswith('.csv')]

def load_data(file_path):
    return pd.read_csv(file_path)

# Sidebar - Parámetros
st.sidebar.title("📂 Parámetros")

csv_files = list_csv_files()

if not csv_files:
    st.sidebar.warning("No hay archivos CSV en la carpeta 'data'")
    st.stop()

selected_file = st.sidebar.selectbox("Elegí un archivo", csv_files)
df = load_data(os.path.join('data', selected_file))

# Filtro de sentimiento
sentimientos = df['sentiment'].unique().tolist()
selected_sentimientos = st.sidebar.multiselect("Filtrar por sentimiento", sentimientos, default=sentimientos)

# Filtro de palabra clave
keyword = st.sidebar.text_input("🔍 Buscar palabra en comentarios")

# Aplicar filtros
df_filtrado = df[df['sentiment'].isin(selected_sentimientos)]

if keyword:
    df_filtrado = df_filtrado[df_filtrado['comment'].str.contains(keyword, case=False, na=False)]

# Visualización principal
st.title("📊 Dashboard de Análisis de Sentimiento")

st.write(f"Mostrando {len(df_filtrado)} comentarios filtrados.")

st.dataframe(df_filtrado[['comment', 'sentiment', 'polarity' if 'polarity' in df.columns else 'compound']])

# Gráfico de distribución de sentimientos
st.subheader("📈 Distribución de sentimientos")
sentiment_counts = df_filtrado['sentiment'].value_counts()
fig = px.pie(values=sentiment_counts.values, names=sentiment_counts.index, title='Distribución de sentimientos')
st.plotly_chart(fig)

# Comentarios destacados
st.subheader("🗣 Comentarios de ejemplo")
for idx, row in df_filtrado.head(5).iterrows():
    st.markdown(f"> **[{row['sentiment'].capitalize()}]** {row['comment']}")
