import random as rd
import csv
from tqdm import tqdm

print("Bienvenue sur l'interface de Defensio pour la phase 1. Votre but est de maximiser vos jauges, bon courage ! \n")

#Intro

#Phase 0 de tutoriel avec des cartes prédéfinies

popularite = 50
relations = 50
finances = 50
defenses = {"feu" : 0, "terre" : 0, "eau" : 0, "air" : 0}

print("Voici les valeurs de vos 3 jauges :", "Popularité", popularite, "Relations", relations, "Finances", finances, "\n")

#chaque carte dans cartes est un dictionnaire avec les clés ['Choix', 'Oui R', 'Oui C', 'Oui I ', 'Non R', 'Non C ', 'Non I ', 'feu', 'terre', 'eau', 'air', 'intro', 'outro', '', 'index']

cartes = []
with open("../static/cartes_action.tsv", "r", newline = "") as mycsv:
  reader = csv.DictReader(mycsv, delimiter = "\t")
  for idx, row in enumerate(reader):
    if row['Oui R']=='':
      break
    row['index'] = idx
    cartes.append(row)

rd.shuffle(cartes)
continuer = True

while continuer == True:
    for i, carte in enumerate(cartes):
        print(f"Voici la carte numéro {i + 1} \n")
        print("Voulez-vous : " +carte["Choix"] +"\n")
        print("Effet sur la popularité :", carte["Oui C"])
        print("Effet sur les relations :", carte["Oui R"])
        print("Effet sur les finances :", carte["Oui I "])

        magnet = ''
        temp = [(0, 'feu'), (0, 'terre'), (0, 'eau'), (0, 'air')]
        for i, defense in enumerate(temp):
          if carte[defense[1]]!='':
            magnet+= '+ 1 défense ' + defense[1]
            temp[i]=(int(carte[defense[1]]), temp[i][1])
        if magnet!='':
          print(magnet)


        choix = input("Oui ou non ? ")
        peutAccepter = True
        peutRefuser = True
        if choix.lower() == "oui":
            oC = int(carte["Oui C"])
            oR = int(carte["Oui R"])
            oI = int(carte["Oui I "])
            if (popularite+oC<0) or (relations+oR<0) or (finances+oI<0):
              print("Vous ne pouvez pas accepter cela.")
              choix = "non"
              peutAccepter = False
              break
            popularite += oC
            relations += oR
            finances += oI
            if magnet!='':
              for i, elt in enumerate(temp):
                if elt[0]>0:
                  defenses[elt[1]]+=elt[0]

        elif choix.lower() == "non":
            nC = int(carte["Non C "])
            nR = int(carte["Non R"])
            nI = int(carte["Non I "])
            if (popularite+nC<0) or (relations+nR<0) or (finances+nI<0):
              print("Vous ne pouvez pas refuser cela.")
              peutRefuser = False
              break
            popularite += nC
            relations += nR
            finances += nI
        else:
          if peutRefuser == False:
            break
          else:
            choix = input("Oui ou non ? ")

        print("\n Popularité", popularite, "Relations", relations, "Finances", finances, "\n")
        print("Réserve : " + str(defenses["feu"]) + " défenses feu, " +str(defenses["terre"])+ " défenses terre, " +str(defenses["eau"])+ " défenses eau, " +str(defenses["air"])+ " défenses air.\n")

        while continuer:
          try:
            continuer = bool(int(input("Veux-tu continuer à tirer des cartes ? 1 pour oui et 0 pour non ? ")))
            break
          except:
            None

        if not continuer:
            break