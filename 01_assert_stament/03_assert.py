width = int(input("enter width of rectangle: "))
assert width > 0 , 'width must be greater than 0'
height = int(input("enter height of rectangle: "))
assert height > 0 , 'height must be greater than 0'

area = width * height
print(f'{area}')