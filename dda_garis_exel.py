def dda_line(x1, y1, x2, y2):
    # Hitung delta x dan delta y
    dx = x2 - x1
    dy = y2 - y1

    # Tentukan jumlah langkah
    steps = max(abs(dx), abs(dy))

    # Hitung increment untuk setiap langkah
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)

    # Mulai dari titik awal
    x = x1
    y = y1

    # List untuk menyimpan hasil koordinat
    coordinates = []

    # Simpan koordinat awal
    coordinates.append((round(x), round(y)))

    # Iterasi untuk menghasilkan titik-titik antara titik awal dan akhir
    for _ in range(int(steps)):
        x += x_increment
        y += y_increment
        coordinates.append((round(x), round(y)))

    return coordinates

def main():
    # Koordinat titik awal (x1, y1) dan titik akhir (x2, y2)
    x1, y1 = 2, 1
    x2, y2 = 6, 8

    # Panggil fungsi DDA untuk menghitung titik-titik garis
    line_coordinates = dda_line(x1, y1, x2, y2)

    # Cetak hasil koordinat titik-titik garis
    print("Koordinat titik-titik yang membentuk garis:")
    for (x, y) in line_coordinates:
        print(f"({x}, {y})")

if __name__ == "__main__":
    main()
