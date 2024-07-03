def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    
    return points

# Fungsi utama
def main():
    x1, y1 = 2, 3
    x2, y2 = 8, 6
    
    points = bresenham_line(x1, y1, x2, y2)
    for point in points:
        x, y = point
        if x <= 10 and y <= 10:
            print(f"({x}, {y})")

if __name__ == "__main__":
    main()
