import menu


def cargar_rotor(nom):
    ruta = "text/" + nom
    f = open(ruta, "r")  # Obrim el fitxer
    linies = f.readlines()
    f.close()
   
    # La primera linia es el cablejat
    cablejat = linies[0].strip()
   
    # La segona es el notch. Si falta, es Z
    if len(linies) > 1:
        notch = linies[1].strip()
    else:
        notch = "Z"
       
    return cablejat, notch




def inicio():
    while True:
        menu.mostrar_menu()
        opcio = input("Tria una opcio: ")

        if opcio == '1':
            print("Has triat xifrar...")
            # AUN TENEMOS QUE HACER ESTO 
            
        elif opcio == '2':
            print("Has triat desxifrar...")
            # AUN TENEMOS QUE HACER ESTO 
            
        elif opcio == '3':
            print("Has triat editar rotors...")
            # AUN TENEMOS QUE HACER ESTO 

        elif opcio == '4':
            print("has sortit del programa")
            break
        else:
            print("Opcio no valida.")

inicio()

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

