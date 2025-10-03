PI = 3.14

def calculate_area(radius):
    return PI * radius * radius

def calculate_circumference(radius):
    return 2 * PI * radius

def calculate_diameter(radius):
    return 2 * radius

def calculate_radius(diameter):
    return diameter / 2

if __name__ == "__main__":
    r = 5
    area = calculate_area(r)
    circumference = calculate_circumference(r)
    diameter = calculate_diameter(r)
    radius = calculate_radius(diameter)
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
    print(f"Diameter: {diameter}")
    print(f"Radius: {radius}")