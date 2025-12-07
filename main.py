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