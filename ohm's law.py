print("Verifiaction of Ohm's Law")

# Determine the the missing value
print("select the missing value:")


print("1. Voltage (v)")
print("2. current (I)")
print("3. Resistance(R)")
missing_value_choice = input("Enter the option number for the missing value:")

#prompt the user to enter the other two values
if missing_value_choice == "1":
    I= float(input("Enter current(I):"))
    R= float(input("Enter resistance(R)"))
    V= I*R
    print(f"Voltage(V)={V}")

elif missing_value_choice =="2":
    V=float(input("Enter voltage(V)"))
    R= float(input("enter resistance(R)"))
    I= V/R                  
    print(f"Current(I)={I}")

elif missing_value_choice == "3":
    V=float(input("Enter voltage(V)"))
    I= float(input("Enter current(I):"))
    R= V/I
    print(f"Resistance(R)= {R}")

else:
    print("Invalid option selected for the missing value.") 