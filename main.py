<<<<<<< HEAD
def preprocesar_missatge(text):
    # Variable buida per anar guardant el missatge net
    resultat = ""
    
    # Definim manualment quines lletres acceptem (l'abecedari)
    lletres_valides = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Recorrem el text lletra per lletra convertint-ho tot a majuscules al moment
    for lletra in text.upper():
        # Si la lletra esta a la llista de valides...
        if lletra in lletres_valides:
            # ...l'afegim al resultat final
            resultat = resultat + lletra
            
    return resultat
=======
def mostrar_menu():
    print()
    print("ENIGMA:")
    print("-------------------------")
    print("1. Xifrar missatge")
    print("2. Desxifrar missatge")
    print("3. Editar rotors")
    print("4. Sortir")
    print()

# Codi principal
while True:
    mostrar_menu()
    opcio = input("Tria una opcio: ")
    
    if opcio == '4':
        print("Has sortit del programa")
        break
>>>>>>> origin/main
