def cargar_rotor(nom):
    ruta = "text/" + nom # busquem l'arxiu a la carpeta
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

def guardar_rotor_modificat(nom_fitxer, nou_cablejat, notch): # aqui guardem lo que l'usuari escrigui
    f_rotor = open(nom_fitxer, "w")
    f_rotor.write(nou_cablejat + "\n") 
    f_rotor.write(notch)               
    f_rotor.close()

def xifrar_logica(missatge_net, r1, r2, r3, pos1, pos2, pos3): #funcio entera per poder xifrar el missatge
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat_xifrat = ""
    cables1 = r1[0]
    cables2 = r2[0]
    cables3 = r3[0]

    num1 = 0 # ara passem les lletres a numeros
    for lletra in abecedario:
        if lletra == pos1: 
            break 
        num1 = num1 + 1
    
    num2 = 0 # fem el mateix amb la resta
    for lletra in abecedario:
        if lletra == pos2: 
            break 
        num2 = num2 + 1
        
    num3 = 0
    for lletra in abecedario:
        if lletra == pos3: 
            break 
        num3 = num3 + 1

    # bucle per cada lletra del missatge
    for lletra_original in missatge_net: # fem girar els rotors
        num1 = num1 + 1
        if num1 == 26:
            num1 = 0
            num2 = num2 + 1
            if num2 == 26:
                num2 = 0
                num3 = num3 + 1
                if num3 == 26:
                    num3 = 0

        indice = 0 # busquem la posició a l'abecedari
        for l in abecedario:
            if l == lletra_original: 
                break
            indice = indice + 1

        """(en aquesta part hem fet servir ajuda de l'IA per solucionar un error ja que la nostra logica implementada no funcionava del tot)"""
        # Rotor 1
        indice = (indice + num1) % 26
        letra_salida = cables1[indice]
        indice = 0
        for l in abecedario:
            if l == letra_salida: 
                break
            indice = indice + 1
        indice = (indice - num1) % 26
        """(en aquesta part hem fet servir ajuda de l'IA per solucionar un error ja que la nostra logica implementada no funcionava del tot)"""

        
        # Rotor 2
        indice = (indice + num2) % 26
        letra_salida = cables2[indice]
        indice = 0
        for l in abecedario:
            if l == letra_salida: 
                break
            indice = indice + 1
        indice = (indice - num2) % 26
        
        # Rotor 3
        indice = (indice + num3) % 26
        letra_salida = cables3[indice]
        indice = 0
        for l in abecedario:
            if l == letra_salida: 
                break
            indice = indice + 1
        indice = (indice - num3) % 26
        
        # resultat final
        letra_final = abecedario[indice]
        resultat_xifrat = resultat_xifrat + letra_final
        
    return resultat_xifrat



def desxifrar_logica(missatge, r1, r2, r3, pos1, pos2, pos3): # funcio entera per desxifrar

    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat_desxifrat = ""
    
    cables1 = r1[0]
    cables2 = r2[0]
    cables3 = r3[0]

# canviem les lletres a numeros
    num1 = 0  
    for lletra in abecedario:
        if lletra == pos1: 
            break 
        num1 = num1 + 1
    
    num2 = 0
    for lletra in abecedario:
        if lletra == pos2: 
            break 
        num2 = num2 + 1
        
    num3 = 0
    for lletra in abecedario:
        if lletra == pos3:
            break 
        num3 = num3 + 1



    for lletra_xifrada in missatge: # recorrem tot el text xifrat
        num1 = num1 + 1 # actualitzem posicio dels rotors
        if num1 == 26:
            num1 = 0
            num2 = num2 + 1
            if num2 == 26:
                num2 = 0
                num3 = num3 + 1
                if num3 == 26:
                    num3 = 0
        
        indice = 0 # busquem index de la lletra xifrada
        for l in abecedario:
            if l == lletra_xifrada: 
                break
            indice = indice + 1

        indice = (indice + num3) % 26 # passem pel tercer rotor al reves
        letra_buscada = abecedario[indice]
        indice = 0
        for cable in cables3:
            if cable == letra_buscada: 
                break
            indice = indice + 1
        indice = (indice - num3) % 26

        indice = (indice + num2) % 26 # passem pel segon rotor al reves
        letra_buscada = abecedario[indice]
        indice = 0
        for cable in cables2:
            if cable == letra_buscada: 
                break
            indice = indice + 1
        indice = (indice - num2) % 26

        indice = (indice + num1) % 26 # i finalment amb el primer rotor
        letra_buscada = abecedario[indice]
        indice = 0
        for cable in cables1:
            if cable == letra_buscada: 
                break
            indice = indice + 1
        indice = (indice - num1) % 26

        letra_final = abecedario[indice] # guardem la lletra ja desxifrada
        resultat_desxifrat = resultat_desxifrat + letra_final
        
    return resultat_desxifrat