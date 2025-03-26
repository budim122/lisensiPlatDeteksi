## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/yourusername/license-plate-detection.git
   ```
2. Masuk ke folder proyek:
   ```bash
   cd license-plate-detection
   ```
3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Penggunaan

1. **Mengumpulkan Data Gambar**:
   ```bash
   python src/data_collection.py
   ```
2. **Memberi Label Data** (Menggunakan LabelImg):
   ```bash
   python src/labeling.py
   ```
3. **Konversi XML ke CSV**:
   ```bash
   python src/convert_xml_to_csv.py
   ```
4. **Preprocessing Data**:
   ```bash
   python src/preprocessing.py
   ```
5. **Melatih Model**:
   ```bash
   python src/train_model.py
   ```
6. **Mendeteksi Plat Nomor**:
   ```bash
   python src/detect_plate.py test_image.jpg
   ```
7. **Ekstraksi Teks dari Plat Nomor**:
   ```bash
   python src/ocr_extraction.py detected_plate.jpg
   ```

## Kontributor

- Nama Anda (@username)

## Lisensi

Proyek ini dirilis di bawah lisensi MIT.
