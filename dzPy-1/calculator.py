a= int(input("Unesi prvi broj : "))

b= int(input("Unesi drugi broj : "))

izbor=input("Odaberi matematicku operaciju +, -, *, / i dobiti ćes rezultat ")

if (izbor== "+"):
    print(a+b)
elif (izbor== "-"):
    print(a-b)
elif (izbor== "*"):
    print(a*b)
elif (izbor== "/"):
    print(a/b)
else:
    print("Nepodrzana operacija, Hvala")
