from helper import *
from pathlib import Path
import random

class ConfigGlobal:
    def __init__(self):
        self.setABC("26")
        self.setTaille(4)
        self.table = {}
        self.file = "TableArcEnCiel.txt"

    def calculateN(self):
        N = 0
        if self.tailleMax != None and self.tailleMax != None:
            for i in range(self.tailleMin, self.tailleMax + 1):
                N += len(self.alphabet) ** i
            return N
        return len(self.alphabet) ** self.taille
    
    def i2c(self, wordIndex):
        result = []
        base = len(self.alphabet)
        taille = self.taille
        if self.tailleMax != None and self.tailleMax != None:
            for i in range(self.tailleMin, self.tailleMax + 1):
                currentSizeN = len(self.alphabet) ** i
                if wordIndex >= currentSizeN:
                    wordIndex -= currentSizeN
                else:
                    taille = i
                    break

        for _ in range(taille):
            result.insert(0, self.alphabet[wordIndex % base])
            wordIndex //= base

        return result

    def h2i(self, hashed_value, indice):
        y_as_int = int.from_bytes(hashed_value[:8], byteorder='little', signed=False)
        return ((y_as_int + indice)% 2**64) % self.calculateN()
    
    def i2i(self, wordIndex, h2iIndex):
        word = ''.join(self.i2c(wordIndex))
        empreinte = hash_SHA1(word)
        return self.h2i(empreinte, h2iIndex)
    
    def nouvelle_chaine(self, wordIndex, largeur):
        index = wordIndex
        for i in range(1, largeur):
            index = self.i2i(index, i)
        return index
    
    def index_aleatoire(self):
        return random.randint(0, self.calculateN())
    
    def creer_table(self, largeur, hauteur):
        self.table = {}
        for i in range(hauteur):
            while True:
                if len(self.table) == self.calculateN():
                    break
                currentIndex = self.index_aleatoire()
                if currentIndex not in self.table:
                    break
            self.table[currentIndex] = self.nouvelle_chaine(currentIndex, largeur)
        self.table = dict(sorted(self.table.items(), key=lambda x: x[1]))

    def sauve_table(self):
        tableToWrite = []
        for key, value in self.table.items():
            tableToWrite.append(str(key) + " " + str(value))
        stringToWrite = '\n'.join(tableToWrite)
        f = open(self.file, "w")
        f.write(stringToWrite)
        f.close()

    def ouvre_table(self):
        my_file = Path(self.file)
        if my_file.is_file():
            f = open(self.file, "r")
            stringToRead = f.read()
            tableToRead = stringToRead.split('\n')
            for value in tableToRead:
                key, val = value.split(' ')
                self.table[int(key)] = int(val)
            f.close()

    def affiche_table(self):
        keys = list(self.table.keys())
        for i in range (5):
            print(f"{i} : {keys[i]} --> {self.table[keys[i]]}")
        print(".\n.\n.")
        for i in range (len(self.table) - 5, len(self.table)):
            print(f"{i} : {keys[i]} --> {self.table[keys[i]]}")
    
    def exhaustiveSearch(self, indice):
        possibleCandidates = []
        for key, value in self.table.items():
            if value > indice:
                return possibleCandidates
            elif value == indice:
                possibleCandidates.append(key)
        return possibleCandidates
    
    def recherche(self, indice):
        possibleCandidates = []
        keys = list(self.table.keys())
        a = 0
        b = len(keys) - 1
        while a <= b:
            currentLine = (a + b) // 2
            if self.table[keys[currentLine]] == indice:
                possibleCandidates.append(keys[currentLine])
                linePrevious = currentLine - 1
                lineNext = currentLine + 1
                while self.table[keys[linePrevious]] == indice:
                    possibleCandidates.append(keys[linePrevious])
                    linePrevious -= 1
                while self.table[keys[lineNext]] == indice:
                    possibleCandidates.append(keys[lineNext])
                    lineNext += 1
                return possibleCandidates
            elif self.table[keys[currentLine]] < indice:
                a = currentLine + 1
            else:
                b = currentLine - 1
        return possibleCandidates
    
    
    # vérifie si un candidat est correct
    #   - h : empreinte à inverser
    #   - t : numéro de la colonne où a été trouvé le candidat
    #   - idx : indice candidat (de la colonne t)
    #   - clair : résultat : contient le texte clair obtenu
    def verifie_candidat(self, h, t, idx):
        for i in range(1, t):
            idx = self.i2i(idx, i)
        clair = ''.join(self.i2c(idx))
        h2 = hash_SHA1(clair)
        return clair if h2 == h else None
    
    # essaie d'inverser l'empreinte h
    #   - table : table arc-en-ciel
    #   - hauteur : nombre de chaines dans la table
    #   - largeur : longueur des chaines
    #   - h : empreinte à inverser
    #   - clair : (résultat) texte clair dont l'empreinte est h
    def exhaustiveInverse(self, largeur, h):
        for t in range(largeur - 1, 0, -1):
            idx = self.h2i(h, t)
            for i in range(t + 1, largeur):
                idx = self.i2i(idx, i)
            possibleCandidates = self.exhaustiveSearch(idx)
            for i in possibleCandidates:
                clair = self.verifie_candidat(h, t, i)
                if (clair != None):
                    return clair
                
    # essaie d'inverser l'empreinte h
    #   - table : table arc-en-ciel
    #   - hauteur : nombre de chaines dans la table
    #   - largeur : longueur des chaines
    #   - h : empreinte à inverser
    #   - clair : (résultat) texte clair dont l'empreinte est h
    def inverse(self, largeur, h):
        for t in range(largeur - 1, 0, -1):
            idx = self.h2i(h, t)
            for i in range(t + 1, largeur):
                idx = self.i2i(idx, i)
            possibleCandidates = self.recherche(idx)
            for i in possibleCandidates:
                clair = self.verifie_candidat(h, t, i)
                if (clair != None):
                    return clair

    def setAlphabet(self, alphabet):
        self.alphabet = alphabet
            
    def setABC(self, type):
        match type:
            case "26":
                self.alphabet = "abcdefghijklmnopqrstuvwxyz"
            case "26A":
                self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            case "36":
                self.alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
            case "40":
                self.alphabet = "abcdefghijklmnopqrstuvwxyz0123456789,;:$."
            case "52":
                self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            case "62":
                self.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            case "66":
                self.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,;:$."
            case _:
                raise Exception("L'argument pour l'alphabet n'est pas valide. Faites un --custom_help pour plus de détails")

    def setTaille(self, taille):
        self.taille = int(taille)
        self.tailleMax = None
        self.tailleMin = None
    
    def setTailleMin(self, taille):
        self.tailleMin = int(taille)

    def setTailleMax(self, taille):
        self.tailleMax = int(taille)
    
    def setFile(self, load):
        if load == ".":
            pass
        elif load != "":
            self.file = load
            self.ouvre_table()
        else:
            raise Exception("L'argument pour le fichier de load n'est pas valide, utilisez le paramètre --load=")