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

    r1 = cargar_rotor("text/Rotor1.txt")
    r2 = cargar_rotor("text/Rotor2.txt")
    r3 = cargar_rotor("text/Rotor3.txt")
    print("Rotores cargados")

    while True:
        menu.mostrar_menu()
        opcio = input("Tria una opcio: ")

        if opcio == '1':
            print("Has triat xifrar...")

            # Pedimos las 3 letras directamente
            pos1 = input("Lletra Rotor 1: ")
            pos2 = input("Lletra Rotor 2: ")
            pos3 = input("Lletra Rotor 3: ")
            
            # Las pasamos a mayusculas
            pos1 = pos1.upper()
            pos2 = pos2.upper()
            pos3 = pos3.upper()
            
            print("Configuracio guardada: " + pos1 + " " + pos2 + " " + pos3)
            
            print("Llegint el missatge...")
            
            # Abrimos el archivo
            f = open("text/Missatge.txt", "r")
            
            # Leemos todo lo que hay dentro y lo guardamos en la variable 'missatge'
            missatge = f.read()
            f.close()
            
            print("Missatge original: " + missatge)

            print("Limpiando el mensaje...")
            
            # Limpiamos el mensaje usando la función de abajo
            missatge_net = preprocesar_missatge(missatge)
            
            print("Mensaje limpio: " + missatge_net)

            
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

