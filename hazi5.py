# A program bekéri a személy nevét és születési évét, és kiírja az életkorát
nev = input("Add meg a neved:")
szuletes = int(input("Add meg a születési éved:"))
eletkor = 2022 - szuletes
print("Kedves",nev,"a te életkorod",eletkor)