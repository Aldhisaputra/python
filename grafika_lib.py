import matplotlib.pyplot as plt
import numpy as np

def gbr_titik(imageDataTemp, x, y, r, g, b):
    if 0 <= x < imageDataTemp.shape[1] and 0 <= y < imageDataTemp.shape[0]:
        imageDataTemp[y, x] = [r, g, b, 255]  # Setting the RGBA value

def gbr_lingkaran(imageDataTemp, xc, yc, radius, r, g, b):
    for x in range(xc - radius, xc + radius + 1):
        y_offset = int(np.sqrt(radius**2 - (x - xc)**2))
        y1 = yc + y_offset
        y2 = yc - y_offset
        gbr_titik(imageDataTemp, x, y1, r, g, b)
        gbr_titik(imageDataTemp, x, y2, r, g, b)

# Ukuran canvas
canvas_width = 400
canvas_height = 400

# Membuat canvas dengan latar belakang putih
canvas = np.ones((canvas_height, canvas_width, 4), dtype=np.uint8) * 255

# Pusat lingkaran dan radius
centerX = canvas_width // 2
centerY = canvas_height // 2
radius = 100

# Menggambar lingkaran
gbr_lingkaran(canvas, centerX, centerY, radius, 255, 0, 0)

# Menampilkan gambar menggunakan matplotlib
plt.imshow(canvas)
plt.axis('off')  # Menonaktifkan axis
plt.title("Lingkaran di Tengah Canvas")
plt.show()
