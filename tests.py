from configGlobal import *
from questions import showConfig

def hashTest():
    word = "Bob"
    hashed_result = hash_SHA1(word)
    hex_representation = ''.join(format(byte, '02x') for byte in hashed_result)
    print(f"Empreinte de '{word}': {hex_representation}")

def i2cTest():
    config = ConfigGlobal()
    showConfig(config)
    wordIndex = 1234
    print(f"Nous choisissons de trouver le mot numéro {wordIndex}")
    print(f"i2c({wordIndex}) = {config.i2c(wordIndex)}")

def h2iTest():
    config = ConfigGlobal()
    config.setTaille(5)
    showConfig(config)
    word = "oups"
    print(f"Nous choisissons le mot {word}")
    hashed_value = hash_SHA1(word)
    result_h2i = config.h2i(hashed_value, 1)
    print(f"h2i(h({word}), 1) = {result_h2i}")

def nouvelleChaineTest():
    config = ConfigGlobal()
    showConfig(config)
    wordIndex = 1234
    width = 10
    print(f"Nous choisissons le mot numéro {wordIndex} et une chaine de {width}")
    print(f"nouvelle_chaine({wordIndex}, {width}) = {config.nouvelle_chaine(wordIndex, width)}")

def creerTableFichierTest():
    config = ConfigGlobal()
    showConfig(config)
    largeur = 200
    hauteur = 1000
    print(f"Nous choisissons une table avec {largeur} pour largeur, et {hauteur} pour hauteur")
    print("Les données seront sauvegardées dans le fichier 'TableArcEnCiel.txt'")
    config.creer_table(largeur, hauteur)
    config.sauve_table()

def afficheTableTest():
    config = ConfigGlobal()
    showConfig(config)
    largeur = 200
    hauteur = 1000
    print(f"Nous choisissons une table avec {largeur} pour largeur, et {hauteur} pour hauteur")
    config.creer_table(largeur, hauteur)
    config.affiche_table()

def crackTest():
    config = ConfigGlobal()
    config.setAlphabet("abcd")
    config.setTaille(2)
    showConfig(config)
    largeur = 200
    hauteur = 1000
    print(f"Nous choisissons une table avec {largeur} pour largeur")
    config.creer_table(largeur, hauteur)
    word = "ab"
    hashed_result = hash_SHA1(word)
    hash = ''.join(format(byte, '02x') for byte in hashed_result)
    print(f"Nous allons essayer de trouver l'inverse du hash {hash}, qui est {word}")
    clair = config.inverse(largeur, bytes.fromhex(hash))
    print(f"Les résultat trouvé est : {clair}")