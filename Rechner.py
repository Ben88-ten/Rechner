#Rechner
def add(x,y):
   return x + y
def subtract(x,y):
   return x-y
def multiply(x,y):
   return x*y
def divide(x,y):
   return x/y
print("Wähle die Operation aus :")
print("1.Addieren (+)")
print("2.Sub (-)")
print("3.Multi(*)")
print("4.Div(/)")
choice = int(input("Eingabe:"))
if choice == int(1,2,3,4):
    num1 = int(input("Gebe die erste Zahl ein: "))
    num2 = int(input("Gebe die zweite Zahl ein: "))
elif choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == 2:
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == 3:
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == 4:
   print(num1,"/",num2,"=", divide(num1,num2))
