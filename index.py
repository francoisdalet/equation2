import math

print("Résolution d'une équation du second degré")

a = float(input("Entrez a : "))
b = float(input("Entrez b : "))
c = float(input("Entrez c : "))

delta = b**2 - 4*a*c

print("Delta =", delta)

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    print("Deux solutions :")
    print("x1 =", x1)
    print("x2 =", x2)

elif delta == 0:
    x = -b / (2*a)

    print("Une seule solution :")
    print("x =", x)

else:
    print("Pas de solution réelle")
