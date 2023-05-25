# Test Automation

Ini adalah proyek Test Automation yang dibangun menggunakan Selenium dan Python untuk mengotomatiskan pengujian perangkat lunak. Proyek ini menggunakan Selenium untuk mengendalikan browser dan menjalankan skrip pengujian yang telah ditulis dengan Python.

## Persyaratan

- Python 3.x
- Selenium
- Webdriver (untuk browser yang diinginkan, misalnya ChromeDriver untuk Chrome)

Pastikan Anda telah menginstal Python dan mengatur lingkungan virtual (seperti menggunakan `venv`). Selanjutnya, instal Selenium dengan menjalankan perintah berikut:

pip install selenium

Pastikan juga Anda telah mengunduh dan menginstal Webdriver yang sesuai untuk browser yang akan digunakan dalam pengujian. Pastikan versi Webdriver sesuai dengan versi browser yang Anda gunakan.

## Struktur Folder

- `Test Automation/` : Direktori utama proyek.
    - `folder1/` : Folder pengujian pertama.
        - `test1.py` : Skrip pengujian pertama.
    - `folder2/` : Folder pengujian kedua.
        - `test2.py` : Skrip pengujian kedua.
    - ...
    - `folder13/` : Folder pengujian ketiga belas.
        - `test13.py` : Skrip pengujian ketiga belas.
    - `Dockerfile` : File konfigurasi untuk Docker.
    - `docker-compose.yml` : File konfigurasi untuk Docker Compose.
    - `requirements.txt` : File yang berisi dependensi Python yang diperlukan.

## Menjalankan Test Automation

1. Pastikan Anda telah menginstal semua persyaratan yang disebutkan di bagian Persyaratan.
2. Ubah direktori ke dalam folder utama proyek:

cd Test Automation/


3. (Opsional) Jika Anda ingin menjalankan Test Automation menggunakan Docker, pastikan Anda telah menginstal Docker dan Docker Compose. Kemudian jalankan perintah berikut untuk membangun dan menjalankan container:

```
docker-compose up
```

4. (Opsional) Jika Anda ingin menjalankan Test Automation secara lokal, pastikan Anda telah mengatur WebDriver yang sesuai. Kemudian jalankan skrip pengujian menggunakan perintah berikut:

python -m unittest discover


Perintah ini akan menjalankan semua skrip pengujian yang ada di folder pengujian. Anda dapat menyesuaikan perintah ini sesuai dengan kebutuhan Anda.

## Kontribusi

Kontribusi terbuka untuk proyek ini sangat diterima! Jika Anda ingin berkontribusi, silakan buat pull request atau buka issue baru untuk membahas perubahan yang diusulkan.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).