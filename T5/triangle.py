number = 0

number = int(input("Please Enter the number of rows desired for the number triangle: \n")) + 1

for i in range(number):
    
    print(str(i)*i, end='\n')