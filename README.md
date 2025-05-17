# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## ***Business Understanding***
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun sudah berkembang cukup besar, perusahaan menghadapi tantangan serius dalam mengelola sumber daya manusianya, yang ditandai dengan tingginya attrition rate (tingkat keluar masuk karyawan) hingga lebih dari 10%. Hal ini berpotensi menghambat stabilitas dan kinerja perusahaan dalam jangka panjang.

Manajer HR ingin mengetahui faktor-faktor apa saja yang menyebabkan tingginya angka attrition tersebut dan membutuhkan dashboard bisnis yang dapat membantu memantau metrik penting terkait kondisi karyawan.

## ***Permasalahan Bisnis***

Permasalahan utama yang dihadapi adalah tingginya attrition rate (lebih dari 10%) yang dapat berdampak pada efisiensi dan kesinambungan operasional perusahaan. Oleh karena itu, perusahaan ingin:

- Mengidentifikasi faktor-faktor yang memengaruhi karyawan keluar dari perusahaan.
- Memvisualisasikan data tersebut dalam bentuk dashboard interaktif agar tim HR dapat dengan mudah memantau dan menganalisis kondisi SDM secara real-time.

## ***Cakupan Proyek***

Proyek ini dirancang untuk membantu perusahaan dalam memahami dan mengatasi masalah tingginya *attrition* karyawan melalui pendekatan berbasis data dengan cakupan sebagai berikut:

### Eksplorasi dan Analisis Data

Melakukan eksplorasi menyeluruh terhadap data *attrition* yang telah disediakan perusahaan guna memahami pola dan karakteristik karyawan yang keluar. Proses ini diawali dengan:

#### Pemahaman Data (*Data Understanding*)
- Mengumpulkan data historis terkait perpindahan karyawan, termasuk informasi profil, performa kerja, kepuasan kerja, serta faktor-faktor lainnya.
- Mempelajari struktur, jenis data, dan karakteristik *dataset* guna mendapatkan wawasan awal terhadap kondisi karyawan.

#### Persiapan Data (*Data Preparation*)
- Membersihkan data dari *missing values*, duplikasi, dan anomali lain yang berpotensi mengganggu kualitas analisis.
- Melakukan transformasi data seperti *encoding* data kategorikal, normalisasi, serta pemilihan fitur relevan.
- Mengevaluasi korelasi antar variabel untuk mengidentifikasi hubungan yang kuat dengan *attrition*.

### Identifikasi dan Visualisasi Faktor-faktor Terkait

Mengidentifikasi variabel-variabel yang berkorelasi dengan *attrition* dan menyajikannya dalam bentuk visualisasi interaktif. Tujuannya adalah agar *stakeholder*, terutama tim HR, dapat dengan mudah memahami pola dan tren yang terjadi.

### Pengembangan Model Prediktif

Jika dimungkinkan, akan dilakukan pembangunan model *machine learning* untuk memprediksi potensi karyawan mengalami *attrition*, melalui tahapan berikut:

#### Pemodelan (*Machine Learning Modeling*)
- Data akan dibagi menjadi *training set* dan *testing set*.
- Beberapa model klasifikasi akan dilatih untuk memprediksi *attrition* berdasarkan fitur relevan.
- Penyesuaian *hyperparameter* juga dilakukan untuk memperoleh hasil terbaik.

#### Evaluasi (*Evaluation*)
- Model yang telah dilatih akan dievaluasi menggunakan metrik seperti *accuracy*, *precision*, *recall*, dan *F1-score* untuk memastikan performa prediksi yang akurat.

#### Implementasi (*Deployment*)
- Model terbaik (misalnya *Logistic Regression*) akan diimplementasikan secara lokal agar dapat diakses oleh pengguna melalui antarmuka interaktif atau *dashboard*, sebagai bagian dari sistem pendukung keputusan.


### Persiapan

Sumber data: 
```
https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-for-hr-retaining-valuable-employees/
```
Setup environment: Anaconda

```
D:
cd D:\DS-Expert
conda create --name hr-jjm python=3.11 -y
conda activate hr-jjm
pip install --upgrade pip
pip install -r requirements.txt
```
Setup environment: Shell/Terminal
```
D:
cd D:\DS-Expert
python -m venv hr_jjm
.\hr_jjm\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pip install --upgrade pip
pip install ipykernel==6.29.3 pyzmq==25.1.2
python -m ipykernel install --user --name=hr_jjm
pip install notebook jupyter ipykernel
```

Proyek *HR Analytic* ini menggunakan model **Logistic Regression** untuk memprediksi *Attrition Rate* berdasarkan data HR. Berkas yang digunakan adalah sebagai berikut: 
  - `logistic_regression_model.joblib` : Model *Logistic Regression* yang sudah dilatih.
  - `prediction.py` : *Script* Python untuk menjalankan proses prediksi.

Cara menjalankan prediksi:
  1. Persiapan *Environment*

     - Pastikan Anda sudah berada di *environment* Python yang sesuai. Anda bisa menggunakan `pipenv` atau `conda`
     - Disini saya menggunakan venv

     ```
     .\hr_jjm\Scripts\Activate.ps1
     pip install -r requirements.txt
     ```

  2. Jalankan Prediksi

Script prediction.py membutuhkan input data dalam format CSV dengan struktur kolom yang sesuai dengan data pelatihan employee_data.csv
Setelah environment aktif dan dependensi terpasang, jalankan perintah prediksi:
     ```
     python prediction.py --input data.csv --output prediksi.csv
     ```
Pastikan data.csv tersedia di direktori yang sama atau sesuaikan path-nya.
   
  3. Cek Hasil
  Setelah eksekusi berhasil, buka file prediksi.csv — file ini akan berisi hasil prediksi dengan kolom tambahan prediction.

## ***Business Dashboard***

*Dashboard* dibuat dengan menggunakan *Google Looker Studio* untuk menampilkan distribusi data dan pengaruh variabel-variabel data terhadap *Attrition Rate*. *Dashboard* dapat diakses pada *link* berikut ini:
```
https://lookerstudio.google.com/reporting/50d33064-1443-4681-8952-b1e426df358f
```
![ichaa_agni_dashboard](https://github.com/IchaAgni/DS-Expert/blob/main/ichaa_agni_dashboard.jpg) 

## ***Conclusion***

Berdasarkan hasil eksplorasi data dan visualisasi dalam dashboard HR Analytics, dapat disimpulkan bahwa tingkat attrition karyawan di perusahaan cukup signifikan dan dipengaruhi oleh berbagai faktor demografis, pekerjaan, dan kepuasan kerja. Beberapa temuan utama dari analisis ini adalah sebagai berikut:

- Tingkat attrition mencapai 12.18%, mayoritas berasal dari Millennials dan Gen Z.
- Attrition lebih tinggi terjadi pada perempuan, karyawan yang bekerja lembur, dan yang belum menikah.
- Departemen yang paling terdampak oleh attrition adalah Research & Development (R&D) dan Sales.
- Posisi jabatan dengan tingkat keluar tertinggi adalah Staff dan Junior Supervisor.
- Karyawan yang mengalami kenaikan gaji rendah, jarang mendapatkan promosi, serta memiliki tingkat kepuasan kerja yang rendah lebih cenderung untuk meninggalkan perusahaan.

### Rekomendasi Action Items (Optional)

Untuk menurunkan tingkat attrition dan meningkatkan retensi karyawan, perusahaan perlu mengambil langkah strategis berdasarkan temuan dari dashboard. Fokus utama harus diberikan pada faktor-faktor yang paling berkontribusi terhadap keputusan karyawan untuk keluar, seperti beban kerja berlebih, kurangnya peluang karier, dan kepuasan kerja yang rendah.

Beberapa rekomendasi tindakan yang dapat diambil perusahaan adalah:

- Kurangi lembur berlebihan, terutama untuk karyawan muda seperti Gen Z dan Millennials, yang terlihat lebih rentan terhadap attrition.
- Tawarkan peluang karier dan jalur promosi yang lebih jelas, terutama bagi karyawan di posisi staff dan junior supervisor.
- Evaluasi sistem kenaikan gaji dan kepuasan kerja untuk memastikan karyawan merasa dihargai dan memiliki motivasi untuk bertahan di perusahaan.
- Fokus pada pengembangan SDM, terutama untuk generasi muda dan level jabatan rendah, melalui pelatihan, mentoring, dan program peningkatan kompetensi.

