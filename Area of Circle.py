rept = "yes"
while rept.lower() =="yes":

    class Area_Circle:
        def __init__(self,given):
            self.given = given
        def area():
            given = input("PICK A LETTER THAT YOU WANT TO SOLVE \n A. Radius \n B.Diameter \n >>>:")

        if given =='A':
            num = int(input("Write the value of Radius: "))
            print("The area of the circle with the given radius is : ", 3.141592 * num * num, "\n")
        if given == 'B':
            num1 = int(input("Write the value of Diameter:"))
            print("The area of the circle with the given radius is : ", 0.25 * 3.141592 * num1 * num1, "\n")
        else:
            print("Syntax Error")