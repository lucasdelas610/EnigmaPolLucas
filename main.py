import menu
import funciones 

def inicio(): #en aquest arxiu main tenim el codi net amb nomes una funcio per anar trucant les funcions de l'altre arxiu funciones 
    r1 = funciones.cargar_rotor("Rotor1.txt") #carreguem tots els rotors
    r2 = funciones.cargar_rotor("Rotor2.txt")
    r3 = funciones.cargar_rotor("Rotor3.txt")
    print("Rotores cargados")

    while True:
        menu.mostrar_menu()
        opcio = input("Tria una opcio: ")

        if opcio == '1':
            print("Has triat xifrar...")
            
            pos1 = input("Lletra Rotor 1: ").upper() #demanen les lletres dels rotos
            pos2 = input("Lletra Rotor 2: ").upper()
            pos3 = input("Lletra Rotor 3: ").upper()
            print("Configuracio guardada: " + pos1 + " " + pos2 + " " + pos3)

            print("Llegint el missatge...")
            
            f = open("text/Missatge.txt", "r") #llegeix l'arxiu de text de missatge (hola mundo)
            missatge = f.read()
            f.close()
            print("Missatge original: " + missatge)
            
            missatge_net = funciones.preprocesar_missatge(missatge) #truca la funcio preprocessar missatge
            print("Mensaje limpio: " + missatge_net)
            
            resultado = funciones.xifrar_logica(missatge_net, r1, r2, r3, pos1, pos2, pos3) #ara truca la funcio per poder xifrar el missatge
            
            print("Missatge xifrat: " + resultado)
            
            f_salida = open("text/Xifrat.txt", "w") #aqui es guarda el resultat del missatge xifrat
            f_salida.write(resultado)
            f_salida.close()
            print("Guardado en text/Xifrat.txt")

        elif opcio == '2':
            print("Has triat desxifrar...")
            # demanem la configuració inicial
            pos1 = input("Lletra Rotor 1: ").upper()
            pos2 = input("Lletra Rotor 2: ").upper()
            pos3 = input("Lletra Rotor 3: ").upper()
            
            f = open("text/Xifrat.txt", "r")
            missatge = f.read()
            f.close()
            print("Missatge xifrat original: " + missatge)
            
            resultado = funciones.desxifrar_logica(missatge, r1, r2, r3, pos1, pos2, pos3) #truquem la funcio de desxifrar el missatge
            
            print("MISSATGE ORIGINAL: " + resultado)
            
            f_salida = open("text/desxifrat.txt", "w")
            f_salida.write(resultado) # ho guardem en un fitxer nou
            f_salida.close()
            print("Guardado en text/desxifrat.txt")
            
            
        elif opcio == '3': #opcio d'editar rotors 
            rotor = input("Quin rotor vols editar? (1, 2, 3): " ) #esculls el rotor que vulguis
            nom_fitxer = "" 

            if rotor == '1': nom_fitxer = "text/Rotor1.txt"
            elif rotor == '2': nom_fitxer = "text/Rotor2.txt"
            elif rotor == '3': nom_fitxer = "text/Rotor3.txt"
            
            if nom_fitxer != "": 
                nou_cablejat = input("Escriu la nova llista de 26 lletres: ").upper() #demanem combinacio de lletres per canviar un rotor
                notch = input("Escriu la lletra del Notch: ").upper()
                
                exito = funciones.guardar_rotor_modificat(nom_fitxer, nou_cablejat, notch) #truquem aquesta funcio per guardar-la
                print("Rotor guardat.")
                
<<<<<<< HEAD
                r1 = funciones.cargar_rotor("Rotor1.txt") #tornem a carregar tots els rotors
                r2 = funciones.cargar_rotor("Rotor2.txt")
                r3 = funciones.cargar_rotor("Rotor3.txt")
=======
                if exito == True:
                    print("Rotor guardat correctament.")
          
                    r1 = funciones.cargar_rotor("Rotor1.txt") #tornem a carregar tots els rotors
                    r2 = funciones.cargar_rotor("Rotor2.txt")
                    r3 = funciones.cargar_rotor("Rotor3.txt")
                else:
                    print("ERROR: Has d'escriure exactament 26 lletres.") #Ha de tenir 26 lletres
>>>>>>> origin/dev
            else:
                print("Rotor incorrecte.")  
            

        elif opcio == '4': # Surt del programa al escollir aquesta funcio
            print("Has sortit del programa") 
            break
        else:
            print("Opcio no valida.") #si escrius un altre numero que no sigui de l'1 al 4, apareix aquest missatge

inicio()