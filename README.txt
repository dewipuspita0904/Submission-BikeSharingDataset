🍎 Bike Sharing Dashboard

📌 Deskripsi

Dashboard interaktif yang menganalisis pola peminjaman sepeda berdasarkan cuaca, waktu, dan faktor lainnya. Dibangun menggunakan Python dan Streamlit untuk visualisasi data yang menarik dan mudah dipahami.

🚀 Cara Menjalankan

1. Pastikan Python dan Streamlit sudah terinstal

Jika belum, instal dengan perintah berikut:

pip install streamlit pandas numpy matplotlib seaborn

2. Install dependensi tambahan

Jalankan perintah berikut untuk menginstal library yang dibutuhkan:

pip install -r requirements.txt

3. Jalankan dashboard

Gunakan perintah berikut untuk menjalankan dashboard Streamlit:

streamlit run dashboard/dashboard.py

4. Akses dashboard

Setelah dijalankan, dashboard akan terbuka secara otomatis di browser.

📊 Fitur

Visualisasi Data: Menampilkan pola peminjaman sepeda berdasarkan berbagai faktor.

Analisis Waktu: Tren peminjaman berdasarkan jam, hari, dan musim.

Analisis Cuaca: Pengaruh cuaca terhadap jumlah peminjaman.

Filter Interaktif: Memungkinkan eksplorasi data dengan filter dinamis.

📂 Struktur Folder

submission/
├───dashboard/
│   ├───day.csv          # Dataset harian
│   ├───hour.csv         # Dataset per jam
│   ├───dashboard.py     # Kode utama untuk dashboard
├───notebook.ipynb       # Notebook analisis data
├───requirements.txt     # Daftar library yang digunakan
└───README.md            # Panduan menjalankan proyek

🌍 Deployment (Opsional)

Jika ingin mendepoy ke Streamlit Cloud:

Push kode ke repository GitHub.

Buka Streamlit Cloud dan buat aplikasi baru.

Hubungkan ke repository, pilih dashboard/dashboard.py sebagai entry point.

Setelah proses selesai, salin link dan tambahkan ke file url.txt.

👤 Kontributor

Nama Anda – GitHub | LinkedIn