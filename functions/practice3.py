def calculate_area(radius):
    radius= 3.14 * (radius**2)
    return radius
radii = [3,5,7]
for radius in radii:
    print(calculate_area(radius))
