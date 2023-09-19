weight=int(input("Weight: "))
con=input("(L)bs or (K)g: ")
if con.upper()=="L":
    unit=weight*0.45
    print(f"You are {unit} kilos")
elif con.upper()=="K":
    unit1=weight/0.45
    print(f"You are {unit1} pounds")
else:
    print("Wrong input")

print("we are expected")
        
        

    