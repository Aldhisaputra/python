def draw_circle(x_center, y_center, radius):
    x = 0
    y = radius
    d = 3 - 2 * radius

    def draw_circle_points(x_center, y_center, x, y):
        points = [
            (x_center + x, y_center + y),
            (x_center - x, y_center + y),
            (x_center + x, y_center - y),
            (x_center - x, y_center - y),
            (x_center + y, y_center + x),
            (x_center - y, y_center + x),
            (x_center + y, y_center - x),
            (x_center - y, y_center - x),
        ]
        for point in points:
            print(point)

    while y >= x:
        draw_circle_points(x_center, y_center, x, y)
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

# Example usage:
x_center = 0
y_center = 0
radius = 10
draw_circle(x_center, y_center, radius)
