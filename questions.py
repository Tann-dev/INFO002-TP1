from configGlobal import *
import math 

def hash(word):
    hashed_result = hash_SHA1(word)
    hex_representation = ''.join(format(byte, '02x') for byte in hashed_result)
    print(f"Empreinte de '{word}': {hex_representation}")

def showConfig(config):
    print("\nConfiguration courante :")
    print(f"Alphabet: {config.alphabet}")
    print(f"Taille: {config.taille}")
    print(f"N: {config.calculateN()}\n")

def i2c(config, wordIndex):
    print(f"i2c({wordIndex}) = {config.i2c(wordIndex)}")

def h2i(config, word):
    # Calcul de l'empreinte de "oups" avec SHA1
    hashed_value = hash_SHA1(word)

    # Utilisation de la fonction h2i
    result_h2i = config.h2i(hashed_value, 1)
    print(f"h2i(h({word}), 1) = {result_h2i}")


def nouvelleChaine(config, wordIndex, width):
    print(f"nouvelle_chaine({wordIndex}, {width}) = {config.nouvelle_chaine(wordIndex, width)}")

def creerTableFichier(config, largeur, hauteur):
    config.creer_table(largeur, hauteur)
    config.sauve_table()

def afficheTable(config):
    config.affiche_table()

def crack(config, hashToCrack, largeur):
    print(f"Les résultat trouvé est : {config.inverse(largeur, bytes.fromhex(hashToCrack))}")

def crackExhaustive(config, hashToCrack, largeur):
    print(f"Les résultat trouvé est : {config.exhaustiveInverse(largeur, bytes.fromhex(hashToCrack))}")

def stats(config, width, height):
    m = height
    v = 1.0
    for i in range (width):
        N = config.calculateN()
        v = v * (1 - m / N)
        m = N * (1 - math.exp(-m / N))
    couverture = 100 * (1-v)
    showConfig(config)
    print(f"Couverture : {couverture}")
