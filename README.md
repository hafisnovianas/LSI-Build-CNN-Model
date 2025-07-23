# Klasifikasi Kualitas Minyak Goreng menggunakan CNN

Repositori ini berisi kode untuk membangun, melatih, dan menggunakan model *Convolutional Neural Network* (CNN) untuk mengklasifikan gambar minyak goreng ke dalam tiga kategori: **Curah**, **Kemasan**, dan **Oplosan**. Proyek ini dibuat menggunakan TensorFlow dan Keras.

## 📝 Deskripsi Proyek

Tujuan dari proyek ini adalah untuk membuat sebuah model *deep learning* yang dapat secara otomatis membedakan jenis minyak goreng berdasarkan citra visualnya. Model dilatih pada dataset gambar yang telah dilabeli dan mampu memprediksi kategori dari gambar baru yang belum pernah dilihat sebelumnya.

## 📂 Struktur Direktori

Berikut adalah struktur direktori yang direkomendasikan untuk proyek ini:

```
LSI-Build-CNN-Model/
├── dataset/
│   ├── data_train/
│   │   ├── curah/
│   │   ├── kemasan/
│   │   └── oplosan/
│   └── data_test/
│       ├── curah/
│       ├── kemasan/
│       └── oplosan/
├── model_results/
│   ├── best_model.keras
│   └── last_model (bukan best).keras
├── module/
│   ├── generator.py
│   └── utility.py
├── .gitignore
├── LICENSE
├── predict.py
├── README.md
├── run_train.py
└── train_resume.py
```

## ✨ Fungsionalitas Script

Berikut adalah penjelasan untuk setiap file utama dalam proyek ini:

### 1\. `run_train.py`

Script utama untuk membangun dan melatih model CNN dari awal.

  * **Arsitektur Model**: Terdiri dari beberapa layer `Conv2D` dan `MaxPooling2D`, diikuti oleh `Flatten` dan `Dense`. Menggunakan `Dropout` untuk mencegah *overfitting*.
  * **Callbacks**: Mengimplementasikan `ModelCheckpoint` untuk menyimpan model dengan `val_accuracy` terbaik dan `EarlyStopping` untuk menghentikan pelatihan jika tidak ada peningkatan performa.
  * **Output**: Model terbaik disimpan sebagai `model_results/best_model.keras`.

### 2\. `train_resume.py`

Digunakan untuk melanjutkan proses pelatihan dari model yang sudah ada (`best_model.keras`). Ini berguna jika proses training sebelumnya berhenti atau jika Anda ingin melatih model lebih lanjut dengan data baru.

### 3\. `predict.py`

Script untuk melakukan prediksi pada gambar-gambar baru menggunakan model yang telah dilatih (`best_model.keras`).

  * **Proses**: Memuat gambar, mengubah ukurannya, melakukan normalisasi, dan kemudian memprediksi kelasnya.
  * **Output**: Hasil prediksi (nama file dan kelas prediksi) akan dicetak di terminal dan disimpan dalam sebuah file Excel di dalam folder gambar uji.

### 4\. `module/generator.py`

Modul ini berisi fungsi `data_generator` yang menggunakan `ImageDataGenerator` dari Keras untuk membuat *batch* data gambar dari direktori. Fungsi ini juga melakukan normalisasi piksel gambar ke rentang [0, 1].

### 5\. `module/utility.py`

Berisi fungsi-fungsi pembantu yang digunakan di seluruh proyek, seperti:

  * `saveToExcel()`: Menyimpan data (misalnya hasil prediksi) ke file `.xlsx`.
  * `pickle_load()`: Memuat file pickle.
  * `cetak()`: Mencetak DataFrame Pandas ke konsol.
  * `copyAllFile()`: Menyalin semua file dari satu folder ke folder lain.

### 6\. `.gitignore`

File ini berisi daftar file dan folder yang akan diabaikan oleh Git, seperti:

  * File gambar (`*.jpg`).
  * File model Keras (`*.keras`).
  * File Excel (`*.xlsx`, `*.xls`).
  * Cache Python (`__pycache__/`, `*.pyc`).

## 🚀 Cara Menggunakan

### Prasyarat

Pastikan Anda sudah menginstall semua *library* yang dibutuhkan. Anda bisa menginstalnya menggunakan pip:

```bash
pip install tensorflow pandas numpy openpyxl
```

### 1\. Menyiapkan Dataset

  * Buat struktur folder `dataset/data_train` dan `dataset/data_test` seperti yang dijelaskan di atas.
  * Masukkan gambar-gambar yang sesuai ke dalam subfolder `curah`, `kemasan`, dan `oplosan`.

### 2\. Melatih Model Baru

Untuk memulai pelatihan dari awal, jalankan script `run_train.py`:

```bash
python run_train.py
```

Proses ini akan melatih model dan menyimpan bobot terbaik ke `model_results/best_model.keras`.

### 3\. Melanjutkan Pelatihan

Jika Anda ingin melanjutkan pelatihan dari model yang sudah tersimpan, jalankan:

```bash
python train_resume.py
```

### 4\. Melakukan Prediksi

  * Letakkan gambar yang ingin Anda uji di dalam folder `dataset/data_test/<nama_kelas>`.
  * Ubah variabel `dataName` dan `ujiFolderPath` di dalam script `predict.py` sesuai dengan lokasi data uji Anda.
  * Jalankan script `predict.py`:
    ```bash
    python predict.py
    ```
    Hasilnya akan ditampilkan di layar dan disimpan dalam file Excel.

## ⚖️ Lisensi

Proyek ini dilisensikan di bawah **CC0 1.0 Universal**, yang berarti berada dalam domain publik. Anda bebas memodifikasi, mendistribusikan, dan menggunakan kode ini untuk tujuan apa pun tanpa batasan.