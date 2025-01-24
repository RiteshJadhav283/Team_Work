def area_of_cylinder(r,h):
    Area=float(2*3.14*r*h+2*3.14*(r**2))
    return Area

def calculate_cylinder_base_perimeter(radius):
    perimeter = float(2 * 3.142 * radius)
    return perimeter

def volumeofcylinder(r,h):
    vol = float(3.14*(r)*(r)*(h))
    return vol

r=float(input("Enter the radius of the Cylinder:"))
h=float(input("Enter the height of the cylinder:"))
x=area_of_cylinder(r,h)
y=volumeofcylinder(r,h)
z=calculate_cylinder_base_perimeter(r)

print(f'The area of cylinder={x}')
print(f'The volume of cylinder={y}')
print(f'The perimeter of cylinder={z}')

