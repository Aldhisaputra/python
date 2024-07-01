# Mengimpor library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar satu titik pada canvas
def gbr_titik(imageDataTemp, x, y, r, g, b):
    # Memeriksa apakah koordinat x dan y berada dalam batas canvas
    if 0 <= x < imageDataTemp.shape[1] and 0 <= y < imageDataTemp.shape[0]:
        # Menetapkan nilai warna (RGBA) pada posisi (x, y)
        imageDataTemp[y, x] = [r, g, b, 255]  # 255 adalah nilai alpha (opacity)

# Fungsi untuk menggambar lingkaran menggunakan pendekatan DDA
def gbr_lingkaran_dda(imageDataTemp, xc, yc, radius, r, g, b):
    steps = 1000  # Jumlah langkah untuk aproksimasi lingkaran
    theta = np.linspace(0, 2 * np.pi, steps)
    
    for angle in theta:
        x = int(xc + radius * np.cos(angle))
        y = int(yc + radius * np.sin(angle))
        gbr_titik(imageDataTemp, x, y, r, g, b)

# Menentukan ukuran canvas
canvas_width = 400
canvas_height = 400

# Membuat canvas dengan latar belakang putih
canvas = np.ones((canvas_height, canvas_width, 4), dtype=np.uint8) * 255

# Menentukan pusat lingkaran dan radius
centerX = canvas_width // 2
centerY = canvas_height // 2
radius = 100

# Menggambar lingkaran menggunakan pendekatan DDA
gbr_lingkaran_dda(canvas, centerX, centerY, radius, 255, 0, 0)  # Warna merah

# Menampilkan gambar menggunakan matplotlib
plt.imshow(canvas)
plt.axis('off')  # Menonaktifkan axis
plt.title("Lingkaran di Tengah Canvas Menggunakan Pendekatan DDA")
plt.show()
