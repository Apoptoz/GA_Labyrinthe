from random import randint

#Genetic evolution :
'''
On doit : créer un labyrinthe avec un départ et une arrivée
Créer les individus : c'est quoi leur adn ? une liste de direction ?

Classes : Chercheurs(Individus), Équipes(Population), Algorithme

Chercheurs : contient un ADN : liste de direction ?

Équipes : Liste de chercheurs, getFittest renvoie le meilleur chercheur

Algorithme : mutation, crossover, evolution de la pop


Comment faire la fonction getFiness ? J'avoue
Soit on connait deja le resultat mais c'est pas interressant ===  exclure selon moi
soit on fait une distance parcouru, auquel on enleve la distance parcourue sur le meme chemin..
pathFinding ?

'''

TAILLE_ADN = 50

laby = ["xxxxxxxxxxxsxxxxxxxxx",
       "xoxxxxxxxxooxxxxxxxxx",
       "xoxxxxoxxxoxxxxxxxxox",
       "xoxxooooxxoxxxxxxxoox",
       "xooxoxxoxxoxxxxxxxoxx",
       "xxoooxxxxxoxxoxxxxoxx",
       "xxoxoxxxxxoooooxxxoxx",
       "xxxxoxxxxxoxxxooxxxxx",
       "xxoxooooxxxxxxxoxxxxx",
       "xxoxoxxooooooxxoxxoxx",
       "xxoooxxoxxxxooooxxoox",
       "xxxoxooooxxxoxxoxxxox",
       "xxxoxoxxoxooxxxoxxxox",
       "xoooooxxoxoxxooooooox",
       "xoxxxoxxoooxxxoxxxxxx",
       "xoxxooxxoxxxoooooooxx",
       "xxxxoxxxoooooxxxxxoxx",
       "xxxxoxxxoxxxooooxxxxx",
       "xxxxoxxxoxxxxxxooooox",
       "xxxxooooooooooooxxoxx",
       "xxxxxxxxxxxexxxxxxxxx"]


coordEntree = (11,20)
coordSortie = (0,12)

map_int_to_dir = { 0 : 'UP',
                   1 : 'DOWN',
                   2 : 'LEFT',
                   3 : 'RIGHT' }

class Chercheur:

  def __init__(self):
    self.listeDir = []
    self.x = coordEntree[0]
    self.y = coordEntree[1]
    for i in range(TAILLE_ADN):
      #Ajoute un entier entre 0 et 3 (inclus) qui signifie la direction
      self.listeDir.append(randint(0,3))


  def getFitness(self):
    print("A implémenter")



class Equipe:

  def __init_(self,tailleEquipe=50,init):
    if init:
      self.listeChercheur = [Chercheur() for i in range(tailleEquipe)]
      #for i in range(tailleEquipe):
        #self.listeChercheur.append(Chercheur())
    else:
      self.listeChercheur = [None for chercheur in range(tailleEquipe)]

  #Méthode pour faire equipe[i]
  def __getitem__(self,index):
    return self.listeChercheur[index]

  #Méthode pour faire equipe[i] = chercheur
  def __setitem__(self,index,chercheur):
    self.listeChercheur[index] = chercheur

  #Méthode pour faire len(equipe)
  def __len__(self):
    return len(self.listeChercheur)

  #Méthode pour faire for chercheur in equipe:
  def __iter__(self): return iter(self.listeChercheur)
  def __next__(self): return next(self.listeChercheur)

  #Méthode pour avoir le best du best de l'équipe
  def getFittest(self):
    maxFitness = 0
    bestChercheur = None
    for chercheur in self:
      if maxFitness > chercheur.getFitness():
        maxFitness = chercheur.getFitness()
        bestChercheur = chercheur
    return bestChercheur
