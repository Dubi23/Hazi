# A program bekér 5 db számot. Ha kisebb mint 100 a szám, azt megszorozza kettővel, ha nagyobb osztja kettővel. 

for x in range(1,6,1):
    szam = int(input("Add meg a számot:"))
    szorzas = szam * 2
    osztas = szam % 2 == 0
    if szam < 100:
        print("A(z)",szam,"kisebb mint 100, ezért a szorzat:",szorzas)
    else:
        print("A(z)",szam,"nagyobb mint 100, ezért az osztás végeredménye:",osztas)
