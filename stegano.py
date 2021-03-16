####mini projet Stéganographie###
### Charline, Paul, Thomas  ###

from PIL import Image

def traitement_texte (text):
    """convertit le texte en binaire
    précondition:
        type text = str
    postconditions:
        type L = list
    Exemple:
        >>>traitenement_texte("Hello")
        ['0100', '1000', '0110', '0101', '0110', '1100', '0110', '1100', '0110', '1111']
    """
    L=[]
    for lettre in text:
        lettre_nb = ord(lettre)
        let_bin = bin(lettre_nb)
        lettre_bin = let_bin[2:]
        while len(lettre_bin) != 8:
            lettre_bin = "0" + lettre_bin

        L.append(lettre_bin[0:4])
        L.append(lettre_bin[4:])
    return L

    
def stegano(name_image, msg) :
    """cache le message msg dans la composante rouge
    des pixels de l'image de nom name_image dans les bits de poids faibles
    pre-conditions :
        name_image : str
        msg : str
    """
    liste_4bits = traitement_texte(msg)
    image = Image.open(name_image)
    #on récupère les dimensions
    w,h = image.size
    indice = 0
    image2 = Image.new("RGB",(w,h))
    long_secret = len(msg) #max 255 car on la met que dans un pixel codé sur 8 bits
    #cacher la longueur du secret dans la première composante rouge
    #puis cacher le message lettre par lettre en coupant en 2 les 8 bits
    #on utilise deux composante rouge pour enregistrer 1 lettre du message
    for y in range(h):
        for x in range(w):
            p = image.getpixel((x,y))
            r = p[0] # composante rouge comprise entre 0 et 255
            v = p[1] #composante verte comprise entre 0 et 255
            b = p[2] #composante bleue comprise entre 0 et 255
            if x == 0 and y == 0 :
                r = long_secret
            else :
                if indice < len(liste_4bits): 
                    print(r)
                    r=bin(r).lstrip('-0b').zfill(8)
                    print(r)
                    rouge=r[:4]
                    r2=rouge+liste_4bits[indice]
                    indice+=1
                    r=int(r2,2)
                    print(r)
                
                #si x est impair on met la première moitié du code de la lettre
                #dans les bits de pôids faibles de r
                #si x est pair on y met la deuxième moitié du code de la lettre
                #dans les bits de poids faibles de r
            image2.putpixel((x,y),(r,v,b)) #on met le code RGB au pixel (x,y) dans la nouvelle image
    image2.save("imageStega.jpg", type = 'JPG') #on sauvegarde l'image
    image2.show()
 #on ouvre l'image !
def search_msg(name_image) :
    """recherche le messge caché dans l'image
    précondition:
        type name_image = str
    postcondition:
        type msg = str
    """
    pass

#tests
stegano('saucisse.jpg','s')