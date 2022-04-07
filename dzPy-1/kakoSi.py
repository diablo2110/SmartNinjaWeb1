import os
from traceback import print_tb


print("Dobar dan kako si ?")

print("Molim izaberi jedan od osjećaja")

print("a) Sretno , b) Nervozno, c) Tuzno, d) Uzbudeno, e) Opusteno " )

osjecaj=input().lower()


if(osjecaj=="a"):
    print("Super")
elif(osjecaj=="nervozo"):
    print("Udahni duboko")
elif(osjecaj=="b"):
    print("Ne brini, proci ce")
elif(osjecaj=="c"):
    print("To je to")
elif(osjecaj=="d"):
    print("Bas je takav dan")
else:
    print("Neznam koji je to osjecaj")