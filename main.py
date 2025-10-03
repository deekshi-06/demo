PI = 3.14

def calculate_area(radius):
    return PI * radius * radius

def calculate_circumference(radius):
    return 2 * PI * radius

if __name__ == "__main__":
    r = 5
    area = calculate_area(r)
    circumference = calculate_circumference(r)
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")