# Fonction pour afficher le menu
def menu():
    print("Veuillez écrire le chiffre en lien avec la fonction que vous désirez faire.")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Quitter")

# Fonction pour les additions
def addition(x, y):
    return x + y

# Fonction pour les soustractions
def soustraction(x, y):
    return x - y

# Fonction pour les multiplications
def multiplication(x, y):
    return x * y

# Code pour la calculatrice
calculatrice = True
while calculatrice:
    menu()
    choix = input("Votre choix : ")
  
    # Code pour le fonctionnement de l'addition
    if choix == "1":
        x = float(input("Entrez la valeur du premier nombre : "))
        y = float(input("Entrez la valeur du deuxième nombre : "))
        resultat = addition(x, y)
        print("Le résultat est :", resultat)

    # Code pour le fonctionnement de la soustraction
    elif choix == "2":
        x = float(input("Entrez la valeur du premier nombre : "))
        y = float(input("Entrez la valeur du deuxième nombre : "))
        resultat = soustraction(x, y)
        print("Le résultat est :", resultat)

    # Code pour le fonctionnement de la multiplication
    elif choix == "3":
        x = float(input("Entrez la valeur du premier nombre : "))
        y = float(input("Entrez la valeur du deuxième nombre : "))
        resultat = multiplication(x, y)
        print("Le résultat est :", resultat)

    # Code pour quitter
    elif choix == "4":
        calculatrice = False
    else:
        print("Choix incorrect.")