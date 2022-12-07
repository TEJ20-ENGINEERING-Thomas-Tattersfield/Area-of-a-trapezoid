# area of a Trapezoid
# the program will ask the user for the dimensions of a Trapezoid then calculate the area using those dimensions
print (" Today, we are going to calculate the area of a trapezoid ")
 
# Gets 1st base from the user
Base1 = int(input("Please input base 1 length in cm: "))

# Gets the 2nd base length from user
Base2 = int(input("Please input base 2 length in cm: "))

# gets the height from user
height = int(input("Please input height in cm: "))

# calculate's the total area
area = Base1 * Base2 / 2 * height 

# display's the area
print (" the area of the Trapezoid with length " + str(Base1) + " cm and Base2 " + str(Base2) + " cm and height" + str(height) + " cm is " + str(area) + "cm^2") 
  