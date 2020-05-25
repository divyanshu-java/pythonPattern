c = 'H'
thickness = int(input("Enter any odd number: "))

for i in range(thickness):  #upperCone
    print((c*i).rjust(thickness-1)+c+(c*i))
for i in range(thickness+1):#verticalBelt
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range((thickness+1)//2):#horizontalBelt
    print((c*thickness*5).center(thickness*6))
for i in range(thickness+1):#verticalBelt
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range(thickness):#lowerCone
    print((c*(thickness-i-1)).rjust(thickness*5-1)+c+(c*(thickness-i-1)))
