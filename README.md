Tentu, saya akan membuatkan dokumentasi yang detail dan mudah dipahami bagi orang awam untuk menggunakan proyek klasifikasi kualitas minyak goreng ini. Dokumentasi ini akan mencakup penjelasan setiap skrip, cara penggunaannya, dan penyesuaian yang mungkin perlu dilakukan.

### Dokumentasi Proyek: Klasifikasi Kualitas Minyak Goreng menggunakan CNN

Dokumentasi ini akan memandu Anda dalam menggunakan serangkaian program untuk melatih dan menguji model kecerdasan buatan (*Artificial Intelligence*) yang dapat membedakan kualitas minyak goreng berdasarkan gambarnya.

-----

### 📝 **Deskripsi Proyek**

Tujuan dari proyek ini adalah untuk membangun sebuah model *Convolutional Neural Network* (CNN) yang mampu mengklasifikasikan gambar minyak goreng ke dalam tiga kategori: **Curah**, **Kemasan**, dan **Oplosan**. Model ini dilatih menggunakan gambar-gambar yang sudah diberi label dan nantinya dapat digunakan untuk memprediksi kategori dari gambar minyak goreng baru.

-----

### 📂 **Struktur Direktori**

Agar proyek berjalan dengan baik, pastikan Anda mengikuti struktur folder seperti di bawah ini. Anda mungkin perlu membuat beberapa folder ini secara manual.

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

-----

### ✨ **Fungsionalitas Setiap Berkas**

Berikut adalah penjelasan fungsi dari setiap berkas penting dalam proyek ini:

#### 1\. `run_train.py`

Berkas ini adalah skrip utama untuk **membangun dan melatih model dari awal**.

  * **Arsitektur Model**: Model CNN ini dibangun dengan beberapa lapisan `Conv2D` dan `MaxPooling2D` untuk ekstraksi fitur dari gambar, serta lapisan `Dense` untuk klasifikasi. Terdapat juga lapisan `Dropout` untuk mengurangi risiko *overfitting*.
  * **Callbacks**: Skrip ini menggunakan `ModelCheckpoint` untuk menyimpan versi model terbaik (berdasarkan `val_accuracy`) dan `EarlyStopping` untuk menghentikan pelatihan secara otomatis jika tidak ada peningkatan performa.
  * **Output**: Model terbaik akan disimpan dengan nama `best_model.keras` di dalam folder `model_results`.

#### 2\. `train_resume.py`

Gunakan berkas ini jika Anda ingin **melanjutkan proses pelatihan** dari model yang sudah ada (`best_model.keras`). Ini sangat berguna jika pelatihan sebelumnya terhenti atau jika Anda ingin melatih ulang model dengan data yang baru.

#### 3\. `predict.py`

Skrip ini berfungsi untuk **melakukan prediksi pada gambar baru** menggunakan model yang sudah dilatih (`best_model.keras`).

  * **Proses**: Skrip akan memuat gambar, mengubah ukurannya, melakukan normalisasi, lalu memprediksi kelasnya (Curah, Kemasan, atau Oplosan).
  * **Output**: Hasil prediksi akan ditampilkan di terminal dan juga disimpan dalam format Excel (`.xlsx`) di dalam folder tempat gambar uji berada.

#### 4\. `module/generator.py`

Modul ini berisi fungsi `data_generator` yang tugasnya adalah memuat data gambar dari direktori dan menyiapkannya untuk proses pelatihan. Fungsi ini akan secara otomatis memberi label pada gambar sesuai dengan nama subfolder tempat gambar tersebut disimpan dan melakukan normalisasi nilai piksel gambar.

#### 5\. `module/utility.py`

Berkas ini berisi fungsi-fungsi pendukung yang digunakan di skrip lain, seperti menyimpan data ke Excel, memuat data, atau menyalin berkas.

-----

### 🚀 **Cara Menggunakan Proyek Ini**

Ikuti langkah-langkah berikut untuk menjalankan proyek ini dari awal hingga akhir.

#### **Prasyarat**

Pastikan Anda sudah menginstal *library* yang dibutuhkan. Buka terminal atau Command Prompt, lalu jalankan perintah berikut:

```bash
pip install tensorflow pandas numpy openpyxl
```

#### **Langkah 1: Menyiapkan Dataset**

Ini adalah langkah paling penting. Kualitas model Anda sangat bergantung pada kualitas dan kuantitas data yang Anda siapkan.

1.  **Buat Struktur Folder**: Ikuti struktur direktori `dataset` yang telah dijelaskan di atas. Buat folder `data_train` (untuk melatih model) dan `data_test` (untuk menguji model).
2.  **Isi Folder Dataset**:
      * Di dalam `dataset/data_train`, masukkan gambar-gambar minyak goreng sesuai dengan kategorinya ke dalam subfolder `curah`, `kemasan`, dan `oplosan`. Semakin banyak gambar, semakin baik.
      * Lakukan hal yang sama untuk `dataset/data_test`. Pastikan gambar di `data_test` **berbeda** dari yang ada di `data_train`.

#### **Langkah 2: Melatih Model Baru**

Jika Anda memulai dari nol, jalankan skrip `run_train.py` untuk melatih model.

1.  Buka terminal atau Command Prompt.
2.  Arahkan ke direktori proyek (`LSI-Build-CNN-Model`).
3.  Jalankan perintah berikut:
    ```bash
    python run_train.py
    ```
4.  Proses pelatihan akan dimulai. Anda akan melihat *progress bar* untuk setiap *epoch*. Setelah selesai, model terbaik akan tersimpan di `model_results/best_model.keras`.

#### **Langkah 3: Melakukan Prediksi**

Setelah model berhasil dilatih, Anda bisa menggunakannya untuk melakukan prediksi.

1.  **Siapkan Data Uji**: Letakkan gambar yang ingin Anda prediksi di dalam folder yang sesuai, misalnya di `dataset/data_test/curah/`.

2.  **Penyesuaian Kode**: Buka berkas `predict.py` dan lakukan penyesuaian pada bagian ini:

    ```python
    # Ubah 'curah' sesuai dengan nama folder kelas yang ingin diuji
    dataName = 'curah' 

    # Pastikan path ini sesuai dengan struktur folder di komputer Anda
    ujiFolderPath = os.path.join('dataset\\TA HENDRA\\data_test', dataName) 
    ```

      * Ubah nilai `dataName` menjadi nama folder dari kelas gambar yang ingin Anda uji (misalnya `'kemasan'` atau `'oplosan'`).
      * Pastikan `ujiFolderPath` mengarah ke lokasi yang benar. Jika Anda mengikuti struktur direktori yang disarankan, Anda mungkin hanya perlu mengubah `dataName`.

3.  **Jalankan Prediksi**: Jalankan skrip `predict.py` melalui terminal:

    ```bash
    python predict.py
    ```

4.  Hasil prediksi akan muncul di layar dan juga tersimpan sebagai berkas Excel di dalam folder `ujiFolderPath`.

-----

### 🔧 **Penyesuaian Kustom oleh Pengguna**

Anda dapat dengan mudah menyesuaikan beberapa parameter dalam kode agar sesuai dengan kebutuhan Anda.

#### 1\. Di `run_train.py` dan `train_resume.py`:

  * **Ukuran Gambar**: Jika gambar Anda memiliki dimensi yang berbeda, ubah nilai `IMG_HEIGHT` dan `IMG_WIDTH`.
    ```python
    IMG_HEIGHT = 120
    IMG_WIDTH = 160
    ```
  * **Parameter Pelatihan**: Anda bisa mengubah `BATCH_SIZE` (jumlah gambar yang diproses dalam satu waktu) dan `EPOCHS` (berapa kali model "belajar" dari keseluruhan dataset).
    ```python
    BATCH_SIZE = 32
    EPOCHS = 50 
    ```

#### 2\. Di `predict.py`:

  * **Nama Kelas**: Jika Anda melatih model untuk kelas yang berbeda (misalnya, 'minyak zaitun', 'minyak kelapa'), sesuaikan `class_names` agar cocok dengan nama folder dataset Anda.
    ```python
    class_names = ['Curah', 'Kemasan', 'Oplosan']
    ```

#### 3\. Di `module/generator.py` (Untuk Augmentasi Data):

Jika jumlah data Anda sedikit, Anda bisa menggunakan **augmentasi data** untuk memperbanyak variasi data secara sintetis. Caranya adalah dengan menghilangkan komentar (tanda `#`) pada parameter di dalam `ImageDataGenerator`.

```python
train_datagen = ImageDataGenerator(
    rescale=1./255,  # Normalisasi
    
    #====Jika butuh augmentasi, silahkan hilangkan tanda # di bawah====#
    rotation_range=20,      # Rotasi gambar acak
    width_shift_range=0.2,  # Pergeseran horizontal
    height_shift_range=0.2, # Pergeseran vertikal
    shear_range=0.2,        # Transformasi geser
    zoom_range=0.2,         # Zoom in/out gambar
    horizontal_flip=True,   # Membalik gambar secara horizontal
    fill_mode='nearest',    # Mengisi piksel yang hilang
)
```

Semoga dokumentasi ini membantu Anda dalam memahami dan menggunakan proyek ini. Selamat mencoba\!