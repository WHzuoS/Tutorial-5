user_Number = 0
empty_Space = ''

user_Number = int(input("Enter a number (1-9): "))

if (user_Number > 0 or user_Number < 0):
    
    print("\n")
    
    for i in range(user_Number):
        for j in range(user_Number):
            
            if(((j+1) * (i+1)) < 10):
                empty_Space = '  '
            else:
                empty_Space = ' '
                
            print(f"\t{((j+1) * (i+1))}", end=empty_Space)
            
        print('\n')
else:
    print("Error: invalid input")