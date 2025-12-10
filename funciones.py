def cargar_rotor(nom):
    # Busca el archivo en la carpeta text/ directamente
    ruta = "text/" + nom
    f = open(ruta, "r")
    linies = f.readlines()
    f.close()
    

    cablejat = linies[0].strip()
    
    if len(linies) > 1:
        notch = linies[1].strip()
    else:
        notch = "Z"
        
    return cablejat, notch



def preprocesar_missatge(text):
    resultat = ""
    lletres_valides = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for lletra in text.upper():
        if lletra in lletres_valides:
            resultat = resultat + lletra
    return resultat



def guardar_rotor_modificat(nom_fitxer, nou_cablejat, notch):
    # Guarda lo que el usuario escriba, sin comprobar si esta bien (tu error a proposito)
    f_rotor = open(nom_fitxer, "w")
    f_rotor.write(nou_cablejat + "\n") 
    f_rotor.write(notch)               
    f_rotor.close()



def xifrar_logica(missatge_net, r1, r2, r3, pos1, pos2, pos3):
    # Esta es TU logica de bucles exacta, solo movida aqui
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat_xifrat = ""
    
    cables1 = r1[0]
    cables2 = r2[0]
    cables3 = r3[0]

    # Convertir letras iniciales a numeros
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

    # Bucle principal
    for lletra_original in missatge_net:
        # Giro
        num1 = num1 + 1
        if num1 == 26:
            num1 = 0
            num2 = num2 + 1
            if num2 == 26:
                num2 = 0
                num3 = num3 + 1
                if num3 == 26:
                    num3 = 0
        
        # Logica Xifrar
        indice = 0
        for l in abecedario:
            if l == lletra_original: break
            indice = indice + 1
        
        # Rotor 1
        indice = (indice + num1) % 26
        letra_salida = cables1[indice]
        indice = 0
        for l in abecedario:
            if l == letra_salida: break
            indice = indice + 1
        indice = (indice - num1) % 26
        
        # Rotor 2
        indice = (indice + num2) % 26
        letra_salida = cables2[indice]
        indice = 0
        for l in abecedario:
            if l == letra_salida: break
            indice = indice + 1
        indice = (indice - num2) % 26
        
        # Rotor 3
        indice = (indice + num3) % 26
        letra_salida = cables3[indice]
        indice = 0
        for l in abecedario:
            if l == letra_salida: break
            indice = indice + 1
        indice = (indice - num3) % 26
        
        # Resultado
        letra_final = abecedario[indice]
        resultat_xifrat = resultat_xifrat + letra_final
        
    return resultat_xifrat



def desxifrar_logica(missatge, r1, r2, r3, pos1, pos2, pos3):
    # TU logica de desxifrar exacta
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat_desxifrat = ""
    
    cables1 = r1[0]
    cables2 = r2[0]
    cables3 = r3[0]

    # Numeros iniciales
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
        # Giro
        num1 = num1 + 1
        if num1 == 26:
            num1 = 0
            num2 = num2 + 1
            if num2 == 26:
                num2 = 0
                num3 = num3 + 1
                if num3 == 26:
                    num3 = 0
        
        # Logica Desxifrar
        indice = 0
        for l in abecedario:
            if l == lletra_xifrada: break
            indice = indice + 1

        # Rotor 3 Inverso
        indice = (indice + num3) % 26
        letra_buscada = abecedario[indice]
        indice = 0
        for cable in cables3:
            if cable == letra_buscada: break
            indice = indice + 1
        indice = (indice - num3) % 26

        # Rotor 2 Inverso
        indice = (indice + num2) % 26
        letra_buscada = abecedario[indice]
        indice = 0
        for cable in cables2:
            if cable == letra_buscada: break
            indice = indice + 1
        indice = (indice - num2) % 26

        # Rotor 1 Inverso
        indice = (indice + num1) % 26
        letra_buscada = abecedario[indice]
        indice = 0
        for cable in cables1:
            if cable == letra_buscada: break
            indice = indice + 1
        indice = (indice - num1) % 26

        letra_final = abecedario[indice]
        resultat_desxifrat = resultat_desxifrat + letra_final
        
    return resultat_desxifrat