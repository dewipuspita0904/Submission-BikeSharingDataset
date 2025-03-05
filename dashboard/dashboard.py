import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    day_df = pd.read_csv("data/day.csv")
    hour_df = pd.read_csv("data/hour.csv")
    return day_df, hour_df

day_df, hour_df = load_data()

# Sidebar - Filter berdasarkan rentang tanggal
st.sidebar.header("📅 Filter Data")
min_date = pd.to_datetime(day_df["dteday"]).min()
max_date = pd.to_datetime(day_df["dteday"]).max()

selected_date = st.sidebar.slider(
    "Pilih Rentang Tanggal", 
    min_value=min_date.to_pydatetime(), 
    max_value=max_date.to_pydatetime(), 
    value=(min_date.to_pydatetime(), max_date.to_pydatetime())
)

# Filter data berdasarkan tanggal yang dipilih
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
filtered_df = day_df[
    (day_df["dteday"] >= pd.Timestamp(selected_date[0])) & 
    (day_df["dteday"] <= pd.Timestamp(selected_date[1]))
]

# Sidebar - Filter kondisi cuaca
weather_options = {1: "Cerah", 2: "Mendung", 3: "Hujan Ringan", 4: "Hujan Lebat"}
selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca", 
    options=list(weather_options.keys()), 
    default=list(weather_options.keys())
)

# Handle kondisi jika tidak ada opsi dipilih
if selected_weather:
    filtered_df = filtered_df[filtered_df["weathersit"].isin(selected_weather)]

# 📌 **Dashboard Title**
st.title("🚴 Dashboard Penyewaan Sepeda")

# 📊 **1. Tren Penyewaan Sepeda per Hari**
st.subheader("📈 Tren Penyewaan Sepeda per Hari")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=filtered_df, x="dteday", y="cnt", ax=ax, marker="o")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Penyewaan Sepeda")
plt.xticks(rotation=45)
st.pyplot(fig)

# 🕒 **2. Penyewaan Sepeda Berdasarkan Jam**
st.subheader("⏳ Rata-rata Penyewaan Sepeda per Jam")
hourly_avg = hour_df.groupby("hr")["cnt"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, ax=ax, marker="o")
plt.xlabel("Jam")
plt.ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig)

# ☀️ **3. Pengaruh Cuaca terhadap Penyewaan (Ganti Boxplot ke Bar Chart)**
st.subheader("🌦️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
weather_counts = filtered_df.groupby("weathersit")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=weather_counts, x="weathersit", y="cnt", ax=ax, palette="pastel")
ax.set_xticklabels([weather_options[w] for w in sorted(filtered_df["weathersit"].unique())])
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

# 📊 **4. Distribusi Penyewaan Sepeda**
st.subheader("📊 Distribusi Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_df["cnt"], bins=30, kde=True, ax=ax)
plt.xlabel("Jumlah Penyewaan Sepeda")
plt.ylabel("Frekuensi")
plt.title("Distribusi Penyewaan Sepeda (Histogram)")
st.pyplot(fig)

# 🚀 **Selesai!**
st.success("Dashboard berhasil dimuat! 🎉")
