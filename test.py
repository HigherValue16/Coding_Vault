import math

def calculate_area_of_circle(radius):
    area = math.pi * radius**2
    return area

# Example usage:
radius = 5.0  # Replace with your desired radius
area = calculate_area_of_circle(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")