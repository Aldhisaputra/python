import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar satu titik pada canvas
def gbr_titik(imageDataTemp, x, y, r, g, b):
    # Memeriksa apakah koordinat x dan y berada dalam batas canvas
    if 0 <= x < imageDataTemp.shape[1] and 0 <= y < imageDataTemp.shape[0]:
        # Menetapkan nilai warna (RGBA) pada posisi (x, y)
        imageDataTemp[y, x] = [r, g, b, 255]  # 255 adalah nilai alpha (opacity)

# Fungsi untuk menggambar garis menggunakan algoritma DDA
def gbr_garis_dda(imageDataTemp, x1, y1, x2, y2, r, g, b):
    # Menghitung perbedaan koordinat
    dx = x2 - x1
    dy = y2 - y1
    
    # Menentukan jumlah langkah yang diperlukan untuk menggambar garis
    steps = max(abs(dx), abs(dy))
    
    # Menghitung perubahan koordinat per langkah
    x_inc = dx / float(steps)
    y_inc = dy / float(steps)
    
    # Memulai dari titik awal
    x = x1
    y = y1
    
    # Menggambar setiap titik sepanjang garis
    for i in range(steps + 1):
        gbr_titik(imageDataTemp, int(round(x)), int(round(y)), r, g, b)
        x += x_inc
        y += y_inc

# Menentukan ukuran canvas
canvas_width = 400
canvas_height = 400

# Membuat canvas dengan latar belakang putih
canvas = np.ones((canvas_height, canvas_width, 4), dtype=np.uint8) * 255

# Menentukan titik awal dan akhir garis
x1, y1 = 50, 50
x2, y2 = 350, 350

# Menggambar garis menggunakan algoritma DDA
gbr_garis_dda(canvas, x1, y1, x2, y2, 255, 0, 0)  # Warna merah

# Menampilkan gambar menggunakan matplotlib
plt.imshow(canvas)
plt.axis('off')  # Menonaktifkan axis
plt.title("Garis Menggunakan Algoritma DDA")
plt.show()
