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