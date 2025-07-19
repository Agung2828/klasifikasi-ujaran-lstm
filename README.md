# 🧠 Sistem Klasifikasi Ujaran Kebencian Berbahasa Indonesia

Proyek ini adalah aplikasi berbasis web yang digunakan untuk mengklasifikasikan teks berbahasa Indonesia apakah mengandung ujaran kebencian, kata kasar, sarkasme, atau netral, menggunakan model deep learning **Long Short-Term Memory (LSTM)**.

---

## 🚀 Fitur Utama

- Deteksi otomatis terhadap:
  - Netral
  - Kata Tidak Sopan
  - Sarkasme
  - Teguran
  - Kasar
- Highlight kata kasar pada teks masukan
- Antarmuka web interaktif dengan navigasi menu (Beranda, Tentang, Kontak, Uji Tes)
- Model LSTM terlatih dari dataset komentar Twitter Indonesia

---

## 🛠️ Teknologi yang Digunakan

- **Python 3.10+**
- **Flask** (Backend web framework)
- **TensorFlow/Keras** (Model LSTM)
- **HTML + Jinja2** (Templating)
- **Bootstrap 5** (Tampilan responsif)
- **Numpy, Regex** (Preprocessing)

---

## 🗂️ Struktur Folder

project_nlp/
│
├── app.py # Main Flask application
├── model_klasifikasi_lstm.h5 # Trained LSTM model
│
├── templates/
│ ├── layout.html
│ ├── index.html
│ ├── tentang.html
│ ├── kontak.html
│ └── test.html
│
├── static/
│ ├── styles.css
│ └── uploads/
│ └── logo.png