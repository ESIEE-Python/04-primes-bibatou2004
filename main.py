"""Nombre Premier"""
from math import sqrt
#### Fonction secondaire
def isprime(p):
    """Nombres Premiers"""
    y=True
    for i in range(1,int(sqrt(p))):
        if p%i==0 and p!=1:
            y=False
            break
    print(y)
# votre code ici
#### Fonction principale
def main():
    """Appel Fonction Secondaire"""
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
