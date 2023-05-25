# Menggunakan base image Python versi terbaru
FROM python:latest

# Menetapkan working directory di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependensi Python yang dibutuhkan
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file dan folder ke dalam container
COPY . .

# Menjalankan skrip testing automation
CMD [ "python", "-m", "unittest", "discover" ]