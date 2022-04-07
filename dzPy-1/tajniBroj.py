
broj=7

guess=0

# dok su razliciti ponavljaj blok naredbi
while guess!=broj:

    guess=int(input("Pogodi broj izmedu 1 i 10 "))

    if guess==broj:
        print("Bravo pogodili ste, Čestitam")
    else:
        print("Zao mi je vise sreće drugi put")
        
