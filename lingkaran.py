#install pip install matplotlib numpy

# Mengimpor library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar satu titik pada canvas
def gbr_titik(imageDataTemp, x, y, r, g, b):
    # Memeriksa apakah koordinat x dan y berada dalam batas canvas
    if 0 <= x < imageDataTemp.shape[1] and 0 <= y < imageDataTemp.shape[0]:
        # Menetapkan nilai warna (RGBA) pada posisi (x, y)
        imageDataTemp[y, x] = [r, g, b, 255]  # 255 adalah nilai alpha (opacity)

# Fungsi untuk menggambar lingkaran menggunakan algoritma Bresenham
def gbr_lingkaran_bresenham(imageDataTemp, xc, yc, radius, r, g, b):
    # Inisialisasi variabel
    x = 0
    y = radius
    d = 3 - 2 * radius  # Nilai keputusan awal

    # Menggambar delapan simetri titik pertama
    gbr_titik(imageDataTemp, xc + x, yc + y, r, g, b)
    gbr_titik(imageDataTemp, xc - x, yc + y, r, g, b)
    gbr_titik(imageDataTemp, xc + x, yc - y, r, g, b)
    gbr_titik(imageDataTemp, xc - x, yc - y, r, g, b)
    gbr_titik(imageDataTemp, xc + y, yc + x, r, g, b)
    gbr_titik(imageDataTemp, xc - y, yc + x, r, g, b)
    gbr_titik(imageDataTemp, xc + y, yc - x, r, g, b)
    gbr_titik(imageDataTemp, xc - y, yc - x, r, g, b)

    # Loop untuk menggambar titik-titik lingkaran
    while y >= x:
        x += 1  # Meningkatkan x
        if d > 0:
            y -= 1  # Menurunkan y jika nilai keputusan lebih besar dari 0
            d = d + 4 * (x - y) + 10  # Mengupdate nilai keputusan
        else:
            d = d + 4 * x + 6  # Mengupdate nilai keputusan

        # Menggambar delapan simetri titik lainnya
        gbr_titik(imageDataTemp, xc + x, yc + y, r, g, b)
        gbr_titik(imageDataTemp, xc - x, yc + y, r, g, b)
        gbr_titik(imageDataTemp, xc + x, yc - y, r, g, b)
        gbr_titik(imageDataTemp, xc - x, yc - y, r, g, b)
        gbr_titik(imageDataTemp, xc + y, yc + x, r, g, b)
        gbr_titik(imageDataTemp, xc - y, yc + x, r, g, b)
        gbr_titik(imageDataTemp, xc + y, yc - x, r, g, b)
        gbr_titik(imageDataTemp, xc - y, yc - x, r, g, b)

# Menentukan ukuran canvas
canvas_width = 400
canvas_height = 400

# Membuat canvas dengan latar belakang putih
canvas = np.ones((canvas_height, canvas_width, 4), dtype=np.uint8) * 255

# Menentukan pusat lingkaran dan radius
centerX = canvas_width // 2
centerY = canvas_height // 2
radius = 100

# Menggambar lingkaran menggunakan algoritma Bresenham
gbr_lingkaran_bresenham(canvas, centerX, centerY, radius, 255, 0, 0)  # Warna merah

# Menampilkan gambar menggunakan matplotlib
plt.imshow(canvas)
plt.axis('off')  # Menonaktifkan axis
plt.title("Lingkaran di Tengah Canvas")
plt.show()
