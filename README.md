# E-Commerce Analytics Dashboard (Streamlit)

Dashboard interaktif berbasis **Streamlit** untuk menganalisis performa data e-commerce, mencakup analisis keterlambatan pengiriman, kualitas produk berdasarkan review, serta tren penjualan bulanan.

---
##  Fitur Utama

### 1. 📍 Geo Delay Analysis

* Menganalisis keterlambatan pengiriman berdasarkan **kota dan state**
* Menampilkan hubungan antara:

  * Jumlah transaksi (volume)
  * Rata-rata keterlambatan (delay)
* Membantu mengidentifikasi wilayah dengan performa logistik buruk

---

### 2. ⭐ Review Score Analysis

* Menampilkan kategori produk dengan **rating rendah**
* Filter dinamis menggunakan **threshold review score**
* Dilengkapi jumlah order per kategori

---

### 3. 💰 Monthly Sales & MoM Growth

* Visualisasi tren penjualan bulanan
* Menghitung **Month-over-Month (MoM) Growth (%)**
* Menyesuaikan dengan rentang waktu dari sidebar
* Menampilkan:

  * Peak sales month
  * Average growth

---

### 4. Interactive Sidebar

* Filter berdasarkan:

  * Rentang tanggal
  * Status pesanan
* Semua visualisasi otomatis menyesuaikan filter

---

## Teknologi yang Digunakan

* Python
* Streamlit
* Pandas
* Matplotlib
* Seaborn

---

## Struktur Proyek

```
.
├── Dashboad_Dicoding.py
├── all_df.csv
└── README.md
```

---

## Cara Menjalankan

1. Clone repository:

```bash
git clone https://github.com/username/ecommerce-dashboard.git
cd ecommerce-dashboard
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Jalankan Streamlit:

```bash
streamlit run app.py
```

---

## Dataset

Dataset berisi informasi:

* Order
* Customer
* Payment
* Review
* Product
* Delivery timestamp

Pastikan file `all_df.csv` berada dalam direktori yang sama dengan `Dashboard.py`.

---

## Insight yang Bisa Didapat

* Wilayah dengan tingkat keterlambatan tinggi
* Kategori produk dengan kepuasan pelanggan yang cukup baik
* Tren pertumbuhan penjualan bulanan
* Dampak waktu terhadap performa bisnis

---

## Catatan

* Data harus sudah bersih (tidak ada missing value kritikal)
* Format tanggal harus sesuai (datetime)
* MoM Growth akan bernilai `NaN` pada periode pertama


