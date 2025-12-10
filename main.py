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


def inicio():
    r1 = cargar_rotor("Rotor1.txt")       
    r2 = cargar_rotor("Rotor2.txt")
    r3 = cargar_rotor("Rotor3.txt")
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


            # Limpiamos el mensaje usando la función de abajo
            missatge_net = preprocesar_missatge(missatge)
            
            print("Mensaje limpio: " + missatge_net)

            print("Xifrant missatge...")
            
            abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            missatge_xifrat = "" 
            
            cables1 = r1[0]
            cables2 = r2[0]
            cables3 = r3[0]

            # Buscamos el numero del Rotor 1
            num1 = 0
            for lletra in abecedario:
                if lletra == pos1:
                    break 
                num1 = num1 + 1
            
            # Buscamos el numero del Rotor 2 
            num2 = 0
            for lletra in abecedario:
                if lletra == pos2:
                    break
                num2 = num2 + 1
                
            # Buscamos el numero del Rotor 3
            num3 = 0
            for lletra in abecedario:
                if lletra == pos3:
                    break
                num3 = num3 + 1

        
            for lletra_original in missatge_net:
                
                # Giro de rotores
                num1 = num1 + 1
                
                # Si se pasa de la z, vuelve a la a
                if num1 == 26:
                    num1 = 0
                    
                    # Mueve el Rotor 2
                    num2 = num2 + 1
                    if num2 == 26:
                        num2 = 0
                        
                        # Mueve el Rotor 3
                        num3 = num3 + 1
                        if num3 == 26:
                            num3 = 0
            

                #convertimos la letra a numero 
                indice = 0
                for l in abecedario:
                    if l == lletra_original: break
                    indice = indice + 1
                
                #rotor 1
                indice = (indice + num1) % 26      # Sumar posicion
                letra_salida = cables1[indice]     # Cambiar letra
                
                # Buscamos numero de la nueva letra
                indice = 0
                for l in abecedario:
                    if l == letra_salida: break
                    indice = indice + 1
                
                indice = (indice - num1) % 26      # Restar posicion
                
                #rotor 2
                indice = (indice + num2) % 26
                letra_salida = cables2[indice]
                
                indice = 0
                for l in abecedario:
                    if l == letra_salida: break
                    indice = indice + 1
                
                indice = (indice - num2) % 26
                
                # rotor 3
                indice = (indice + num3) % 26
                letra_salida = cables3[indice]
                
                indice = 0
                for l in abecedario:
                    if l == letra_salida: break
                    indice = indice + 1
                    
                indice = (indice - num3) % 26

                # convertimos el numero final a letra 
                letra_final = abecedario[indice]
                missatge_xifrat = missatge_xifrat + letra_final

            print("RESULTAT FINAL: " + missatge_xifrat)

            
            # Guardamos en archivo
            f_salida = open("text/Xifrat.txt", "w")
            f_salida.write(missatge_xifrat)
            f_salida.close()
            print("Guardado en text/Xifrat.txt")
                
            

        elif opcio == '2':
            print("Has triat desxifrar...")

            # Pedir posiciones
            pos1 = input("Lletra Rotor 1: ").upper()
            pos2 = input("Lletra Rotor 2: ").upper()
            pos3 = input("Lletra Rotor 3: ").upper()

            print("Configuracio guardada: " + pos1 + " " + pos2 + " " + pos3)

            # Leer fichero xifrado
            f = open("text/Xifrat.txt", "r")
            missatge = f.read()
            f.close()
            print("Missatge xifrat original: " + missatge)

            abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            missatge_desxifrat = ""
            
            cables1 = r1[0]
            cables2 = r2[0]
            cables3 = r3[0]

            # Convertir letras iniciales a números
            num1 = 0
            for lletra in abecedario:
                if lletra == pos1: break 
                num1 = num1 + 1
            
            num2 = 0
            for lletra in abecedario:
                if lletra == pos2: break
                num2 = num2 + 1
                
            num3 = 0
            for lletra in abecedario:
                if lletra == pos3: break
                num3 = num3 + 1

            for lletra_xifrada in missatge:
                num1 = num1 + 1
                if num1 == 26:
                    num1 = 0
                    num2 = num2 + 1
                    if num2 == 26:
                        num2 = 0
                        num3 = num3 + 1
                        if num3 == 26:
                            num3 = 0
                
                # Convertimos letra a numero
                indice = 0
                for l in abecedario:
                    if l == lletra_xifrada: break
                    indice = indice + 1

                # ROTOR 3
                indice = (indice + num3) % 26
                # Buscamos qué letra del abecedario corresponde a este indice
                letra_buscada = abecedario[indice]
                # Y ahora buscamos dónde está esa letra en los cables
                indice = 0
                for cable in cables3:
                    if cable == letra_buscada: break
                    indice = indice + 1
                indice = (indice - num3) % 26

                # ROTOR 2
                indice = (indice + num2) % 26
                letra_buscada = abecedario[indice]
                
                indice = 0
                for cable in cables2:
                    if cable == letra_buscada: break
                    indice = indice + 1
                
                indice = (indice - num2) % 26

                # ROTOR 1
                indice = (indice + num1) % 26
                letra_buscada = abecedario[indice]
                
                indice = 0
                for cable in cables1:
                    if cable == letra_buscada: break
                    indice = indice + 1
                
                indice = (indice - num1) % 26

                # Guardamos la letra final
                letra_final = abecedario[indice]
                missatge_desxifrat = missatge_desxifrat + letra_final
            
            print("MISSATGE ORIGINAL: " + missatge_desxifrat)
            
            # Guardamos en desxifrat.txt
            f_salida = open("text/desxifrat.txt", "w")
            f_salida.write(missatge_desxifrat)
            f_salida.close()
            print("Guardado en text/desxifrat.txt")
            
        elif opcio == '3':
            rotor = input("Quin rotor vols editar?: " )
            nom_fitxer = ""

            if rotor == '1':
                nom_fitxer = "text/Rotor1.txt"
            elif rotor == '2':
                nom_fitxer = "text/Rotor2.txt"
            elif rotor == '3':
                nom_fitxer = "text/Rotor3.txt"
            
            if nom_fitxer != "": #si ha escrit un numero diferent a res, o sigui 1 2 o 3, es segueix, si no surt error
                nou_cablejat = input("Escriu la nova llista de 26 lletres sense repetir: ")
                nou_cablejat = nou_cablejat.upper()

                
                notch = input("Escriu la lletra del Notch: ")
                notch = notch.upper()
                
                f_rotor = open(nom_fitxer, "w")
                f_rotor.write(nou_cablejat + "\n") # Guardem el fitxer
                f_rotor.write(notch)               
                f_rotor.close()
                
                print("Rotor guardat.")
                
                r1 = cargar_rotor("Rotor1.txt") #recarguem els rotors
                r2 = cargar_rotor("Rotor2.txt")
                r3 = cargar_rotor("Rotor3.txt")
            else:
                print("Rotor incorrecte.")

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

