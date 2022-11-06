# A program bekér 10 számot, és megvizsgálja, hogy osztható-e kettővel. Ha nem kiírja, hogy nem osztható, ellenkező esetben pedig azt hogy osztható:
for x in range(1,11,1):
    szam = int(input("Add meg a számot:"))
    if szam != 2:
        print("A",szam,"nem osztható kettővel.")
    else:
        print("A",szam,"osztható kettővel!")