"""Sort function to return Package Type -- Sindhu Puli"""
def sort(width, height, length, mass):
    if width < 150 and height < 150 and length < 150:
        volume = width * height * length
        print('volume:', volume)
        if volume < 1000000 and mass < 20:
            print('check point0')
            return 'NORMAL'
        elif (volume >= 1000000 and mass < 20) or (volume < 1000000 and mass >= 20):
            print('check point1')
            return 'SPECIAL'
        else:
            print('check point2')
            return 'REJECTED'
    elif mass < 20:
        print('check point3:')
        return 'SPECIAL'
    else:
        print('check point4')
        return 'REJECTED'
    
print('Output check point0: ', sort(20, 130, 130, 19))
print('Output check point1: ', sort(120, 130, 130, 19))
print('Output check point2: ', sort(120, 130, 130, 20))
print('Output check point3: ', sort(20, 130, 150, 19))
print('Output check point4: ', sort(20, 130, 150, 20))
    