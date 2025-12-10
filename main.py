import menu
import funciones 

def inicio():
    # Cargamos rotores
    r1 = funciones.cargar_rotor("Rotor1.txt")
    r2 = funciones.cargar_rotor("Rotor2.txt")
    r3 = funciones.cargar_rotor("Rotor3.txt")
    print("Rotores cargados")

    while True:
        menu.mostrar_menu()
        opcio = input("Tria una opcio: ")

        if opcio == '1':
            print("Has triat xifrar...")
            
            # 1. Inputs
            pos1 = input("Lletra Rotor 1: ").upper()
            pos2 = input("Lletra Rotor 2: ").upper()
            pos3 = input("Lletra Rotor 3: ").upper()
            print("Configuracio guardada: " + pos1 + " " + pos2 + " " + pos3)

            print("Llegint el missatge...")
            
            # 2. Leemos archivo (Si no existe, el programa se cierra con error, igual que antes)
            f = open("text/Missatge.txt", "r")
            missatge = f.read()
            f.close()
            print("Missatge original: " + missatge)
            
            print("Limpiando el mensaje...")
            missatge_net = funciones.preprocesar_missatge(missatge)
            print("Mensaje limpio: " + missatge_net)

            print("Xifrant missatge...")
            
            # 3. Llamamos a la logica
            resultado = funciones.xifrar_logica(missatge_net, r1, r2, r3, pos1, pos2, pos3)
            
            print("RESULTAT FINAL: " + resultado)
            
            # 4. Guardamos
            f_salida = open("text/Xifrat.txt", "w")
            f_salida.write(resultado)
            f_salida.close()
            print("Guardado en text/Xifrat.txt")

        elif opcio == '2':
            print("Has triat desxifrar...")
            
            pos1 = input("Lletra Rotor 1: ").upper()
            pos2 = input("Lletra Rotor 2: ").upper()
            pos3 = input("Lletra Rotor 3: ").upper()

            print("Llegint el missatge xifrat...")
            
            f = open("text/Xifrat.txt", "r")
            missatge = f.read()
            f.close()
            print("Missatge xifrat original: " + missatge)
            
            # Llamamos a la logica
            resultado = funciones.desxifrar_logica(missatge, r1, r2, r3, pos1, pos2, pos3)
            
            print("MISSATGE ORIGINAL: " + resultado)
            
            f_salida = open("text/desxifrat.txt", "w")
            f_salida.write(resultado)
            f_salida.close()
            print("Guardado en text/desxifrat.txt")
            
        elif opcio == '3':
            rotor = input("Quin rotor vols editar? (1, 2, 3): " )
            nom_fitxer = ""

            if rotor == '1': nom_fitxer = "text/Rotor1.txt"
            elif rotor == '2': nom_fitxer = "text/Rotor2.txt"
            elif rotor == '3': nom_fitxer = "text/Rotor3.txt"
            
            if nom_fitxer != "": 
                nou_cablejat = input("Escriu la nova llista de 26 lletres: ").upper()
                notch = input("Escriu la lletra del Notch: ").upper()
                
                # Llamamos a la funcion (guardara lo que sea, aunque este mal)
                funciones.guardar_rotor_modificat(nom_fitxer, nou_cablejat, notch)
                print("Rotor guardat.")
                
                # Recargamos
                r1 = funciones.cargar_rotor("Rotor1.txt")
                r2 = funciones.cargar_rotor("Rotor2.txt")
                r3 = funciones.cargar_rotor("Rotor3.txt")
            else:
                print("Rotor incorrecte.")

        elif opcio == '4':
            print("Has sortit del programa")
            break
        else:
            print("Opcio no valida.")

if __name__ == "__main__":
    inicio()