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
git clone https://github.com/username/ecommerce-dashboard.git
cd ecommerce-dashboard

2. Buat dan aktifkan Virtual Environment:
Windows:
python -m venv venv
.\venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install --upgrade pip
pip install -r requirements.txt

4. Jalankan Streamlit:
streamlit run Dashboard_Dicoding.py

## Dataset

Dataset berisi informasi:

* Order
* Customer
* Payment
* Review
* Product
* Delivery timestamp

Pastikan file `all_df.csv.gz` berada dalam direktori yang sama dengan `Dashboard.py`.

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

# E-Commerce Analytics Dashboard (Streamlit)

Dashboard interaktif berbasis **Streamlit** untuk menganalisis performa bisnis e-commerce. Dashboard ini membantu memahami keterlambatan pengiriman, kualitas produk berdasarkan review pelanggan, serta tren penjualan bulanan.

---

## 🚀 Fitur Utama

### 📍 Geo Delay Analysis

Menganalisis keterlambatan pengiriman berdasarkan **kota dan state**.

* Menampilkan hubungan antara jumlah transaksi dan rata-rata keterlambatan
* Mengidentifikasi wilayah dengan performa logistik yang kurang optimal

---

### ⭐ Review Score Analysis

Mengevaluasi kualitas produk berdasarkan **rating pelanggan**.

* Menampilkan kategori produk dengan rating rendah
* Filter dinamis berdasarkan threshold review score
* Dilengkapi jumlah order per kategori

---

### 💰 Monthly Sales & MoM Growth

Menganalisis tren penjualan bulanan.

* Visualisasi total penjualan per bulan
* Perhitungan **Month-over-Month (MoM) Growth (%)**
* Menampilkan bulan dengan penjualan tertinggi (peak sales)
* Menghitung rata-rata pertumbuhan penjualan

---

### 🎛️ Interactive Sidebar

Dashboard dilengkapi fitur filter interaktif:

* Rentang tanggal
* Status pesanan

Semua visualisasi akan otomatis menyesuaikan dengan filter yang dipilih.

---

## ⚙️ Teknologi yang Digunakan

* Python
* Streamlit
* Pandas
* Matplotlib
* Seaborn

---

## 📁 Struktur Proyek

```
.
├── Dashboard_Dicoding.py
├── all_df.csv
└── README.md
```

---

## ▶️ Cara Menjalankan

1. Clone repository

```
git clone https://github.com/username/ecommerce-dashboard.git
cd ecommerce-dashboard
```

2. Buat dan aktifkan virtual environment

**Windows**

```
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux**

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```
pip install --upgrade pip
pip install -r requirements.txt
```

4. Jalankan aplikasi

```
streamlit run Dashboard_Dicoding.py
```

---

## 📊 Dataset

Dataset mencakup informasi berikut:

* Order
* Customer
* Payment
* Review
* Product
* Delivery timestamp

Pastikan file `all_df.csv` berada dalam direktori yang sama dengan `Dashboard_Dicoding.py`.

---

## 🔍 Insight yang Dapat Diperoleh

* Mengetahui wilayah dengan tingkat keterlambatan pengiriman tinggi
* Mengidentifikasi kategori produk dengan kepuasan pelanggan rendah
* Memahami tren dan pertumbuhan penjualan bulanan
* Menganalisis pengaruh waktu terhadap performa bisnis

---

## 📌 Catatan

Dashboard ini dirancang untuk eksplorasi data secara interaktif dan dapat dikembangkan lebih lanjut untuk kebutuhan analisis bisnis yang lebih kompleks.

