import math

#header
print('==================\nArea Calculator 📐\n==================')

#space
print('')

#shape gui
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')
print('') #space
shape = int(input('Which shape: '))

#loop for the gui
while shape != 1 and shape != 2 and shape != 3 and shape != 4 and shape != 5:
    shape = int(input('Please select one of the shapes above: '))
#Triangle
if shape == 1:
    height = int(input('Height: '))
    base = int(input('Base: '))
    area = (height * base) // 2
    print(f'The area is {area}')
#Rectangle
elif shape == 2:
    lenght = int(input('Length: '))
    width = int(input('Width: '))
    area = lenght * width
    print(f'The area is {area}')
#Square
elif shape == 3:
    side = int(input('Side: '))
    area = side * side
    print(f'The area is {area}')
#Circle
elif shape == 4:
    radius = int(input('Radius: '))
    area = math.pi * radius ** 2
    #area = 3.14 * radius ** 2
    print(f'The area is {area}')
else:
    print('Bye Bye!')



