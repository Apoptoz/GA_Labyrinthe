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
PROBA_MUT = .15
TOURNAMENT_SIZE = 5
ELITISM = True






laby =["xxxxxxxxxxxsxxxxxxxxx",
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


coordEntree = (20,11)
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
    #Initialisation de l'ADN
    for i in range(TAILLE_ADN):
      #Ajoute un entier entre 0 et 3 (inclus) qui signifie la direction
      self.listeDir.append(randint(0,3))

  #Renvoie le point final du Chercheur après ses déplacements
  def moveInLab(self):
    cnt = 0
    x = self.x
    y = self.y
    listePossibleMoves = [el if ( 0 < el[0] < 20 and 0 < el[1] < 19 ) else None for el in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]]
    for moveNumber in self.listDir:
      cnt += 1
      nextMove = listePossibleMoves[moveNumber]
      if nextMove is not None and laby[nextMove[0]][nextMove[1]] != 'x':
        self.x = nextMove[0]
        self.y = nextMove[1]
        if laby[self.x][self.y] == 's':
          break
    lastPos = (self.x,self.y)
    self.x = coordEntree[0]
    self.y = coordEntree[1]
    return lastPos,cnt

  def getFitness(self):
    dist = 0
    posChercheur,pasEconomises = self.moveInLab()
    if pasEconomises == 0:
      dist = distance(posChercheur)
    return dist - pasEconomises



class Equipe:

  def __init_(self,tailleEquipe=50,init):
    if init:
      self.listeChercheur = [Chercheur() for i in range(tailleEquipe)]
      #for i in range(tailleEquipe):
        #self.listeChercheur.append(Chercheur())
    else:
      #self.listeChercheur = []
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


def distance(coord):
  x = pow((coord[0]-coordSortie[0]),2)
  y = pow((coord[1]-coordSortie[1]),2)
  return sqrt(x+y)

#Change une partie de l'ADN aléatoirement
def mutation(enfant):
	#Si l'enfant doit muter renvoie l'enfant modifier
  #sinon renvoie l'enfant tel quel

def crossover(parent1,parent2):
  #crée un enfant vide
  #rempli son adn a partir du génome des parents
  #renvoi l'enfant

def tournoi(equipe):
	#Trouve 5 chercheurs aléatoire
  #Compare leur fitness
  #Renvoi le meilleur chercheur

#crossover
'''
1) trouver deux parents
	On a besoin de l'équipe
  On a besoin de tournament_size
2) Faire s'acoupler ces parents
	Besoin d'une méthode d'accouplement
3) Muter l'enfant
	Besoin de la fonction de mutation
for chercheur in equipe:
  parent1 = tournoi(equipe)
  parent2 = tournoi(equipe)
  enfant = crossover(parent1,parent2)
  newEquipe.add(enfant)


  Je me fais de la place:

  Si le chercheur arrive en 20 déplacements
  Est-ce qu'on dit qu'il aura une meilleure fitness
  que celui qui arrive en 30 ?
  ou osef ?


'''
def evolveEquipe
